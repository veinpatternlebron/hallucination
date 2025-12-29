"""
InputHandler - Mouse and Keyboard Input Capture and Mapping
"""
import threading
import time
import math
from pynput import mouse, keyboard


class InputHandler:
    """
    Handles mouse and keyboard input capture and mapping to virtual controller.
    Runs at 120Hz for ultra-responsive input.
    """

    def __init__(self, virtual_controller, window_manager, config):
        """
        Initialize input handler.
        
        Args:
            virtual_controller: VirtualController instance
            window_manager: WindowManager instance
            config: ConfigManager instance
        """
        self.controller = virtual_controller
        self.window_manager = window_manager
        self.config = config
        
        # Mouse state
        self.mouse_dx = 0.0
        self.mouse_dy = 0.0
        self.mouse_lock = threading.Lock()
        self.left_click_pressed = False
        self.right_click_pressed = False
        
        # Keyboard state
        self.key_state = {}
        
        # Settings
        self.sensitivity = config.get("sensitivity", 1.5)
        self.smoothing = config.get("smoothing", True)
        self.key_mappings = config.get("key_mappings", {})
        
        # Threads
        self.active = False
        self.update_thread = None
        self.mouse_listener = None
        self.keyboard_listener = None

    def start(self):
        """Start mouse and keyboard listeners and update thread."""
        if self.active:
            return
        
        self.active = True
        
        # Start mouse listener
        self.mouse_listener = mouse.Listener(
            on_move=self._on_mouse_move,
            on_click=self._on_mouse_click
        )
        self.mouse_listener.daemon = True
        self.mouse_listener.start()
        
        # Start keyboard listener
        self.keyboard_listener = keyboard.Listener(
            on_press=self._on_key_press,
            on_release=self._on_key_release
        )
        self.keyboard_listener.daemon = True
        self.keyboard_listener.start()
        
        # Start update thread
        self.update_thread = threading.Thread(target=self._update_loop, daemon=True)
        self.update_thread.start()
        
        print("✅ Input handler started")

    def stop(self):
        """Stop all listeners and threads."""
        if not self.active:
            return
        
        self.active = False
        
        # Stop listeners
        if self.mouse_listener:
            self.mouse_listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        
        # Wait for update thread to finish
        if self.update_thread and self.update_thread.is_alive():
            self.update_thread.join(timeout=1.0)
        
        # Reset controller
        self.controller.reset()
        
        print("⏸️  Input handler stopped")

    def set_sensitivity(self, value: float):
        """
        Update sensitivity multiplier.
        
        Args:
            value: Sensitivity value (typically 0.1 to 5.0)
        """
        self.sensitivity = value

    def _on_mouse_move(self, x, y):
        """
        Mouse movement callback.
        Accumulates mouse delta for processing in update loop.
        
        Args:
            x: Absolute X position
            y: Absolute Y position
        """
        # pynput gives us absolute position, but we need delta
        # We'll use a different approach in the update loop
        pass

    def _on_mouse_click(self, x, y, button, pressed):
        """
        Mouse button callback.
        Maps mouse clicks to triggers.
        
        Args:
            x: X position
            y: Y position
            button: Mouse button
            pressed: True if pressed, False if released
        """
        if button == mouse.Button.left:
            self.left_click_pressed = pressed
        elif button == mouse.Button.right:
            self.right_click_pressed = pressed

    def _on_key_press(self, key):
        """
        Key press callback.
        Updates key state and maps to controller buttons.
        
        Args:
            key: Key that was pressed
        """
        try:
            # Get key name
            if hasattr(key, 'char') and key.char:
                key_name = key.char.lower()
            elif hasattr(key, 'name'):
                key_name = key.name.lower()
            else:
                return
            
            # Update key state
            self.key_state[key_name] = True
            
            # Map to controller button
            if key_name in self.key_mappings:
                button = self.key_mappings[key_name]
                self.controller.press_button(button)
        except Exception:
            pass

    def _on_key_release(self, key):
        """
        Key release callback.
        Updates key state and releases controller buttons.
        
        Args:
            key: Key that was released
        """
        try:
            # Get key name
            if hasattr(key, 'char') and key.char:
                key_name = key.char.lower()
            elif hasattr(key, 'name'):
                key_name = key.name.lower()
            else:
                return
            
            # Update key state
            self.key_state[key_name] = False
            
            # Release controller button
            if key_name in self.key_mappings:
                button = self.key_mappings[key_name]
                self.controller.release_button(button)
        except Exception:
            pass

    def _update_loop(self):
        """
        Main update loop running at 120Hz.
        Processes input and updates virtual controller.
        """
        last_mouse_pos = None
        
        # Get mouse controller for tracking position
        mouse_controller = mouse.Controller()
        
        while self.active:
            try:
                # Check if target window is active
                if not self.window_manager.is_target_active():
                    # Reset inputs when window not active
                    self.controller.reset()
                    with self.mouse_lock:
                        self.mouse_dx = 0.0
                        self.mouse_dy = 0.0
                    time.sleep(1.0 / 120.0)
                    continue
                
                # Get current mouse position for delta calculation
                try:
                    current_mouse_pos = mouse_controller.position
                    if last_mouse_pos is not None:
                        dx = current_mouse_pos[0] - last_mouse_pos[0]
                        dy = current_mouse_pos[1] - last_mouse_pos[1]
                        with self.mouse_lock:
                            self.mouse_dx += dx
                            self.mouse_dy += dy
                    last_mouse_pos = current_mouse_pos
                except Exception:
                    pass
                
                # Update movement stick (WASD)
                self._update_movement_stick()
                
                # Update aim stick (mouse)
                self._update_aim_stick()
                
                # Update triggers (mouse buttons)
                if self.left_click_pressed:
                    self.controller.set_right_trigger(255)
                else:
                    self.controller.set_right_trigger(0)
                
                if self.right_click_pressed:
                    self.controller.set_left_trigger(255)
                else:
                    self.controller.set_left_trigger(0)
                
                # Send all updates to controller
                self.controller.update()
                
                # Sleep for 120Hz update rate
                time.sleep(1.0 / 120.0)
            except Exception as e:
                print(f"⚠️  Error in update loop: {e}")
                time.sleep(1.0 / 120.0)

    def _update_movement_stick(self):
        """
        Convert WASD key state to left stick values with diagonal normalization.
        """
        x = 0.0
        y = 0.0
        
        # Horizontal movement (A/D)
        if self.key_state.get('a', False):
            x -= 1.0
        if self.key_state.get('d', False):
            x += 1.0
        
        # Vertical movement (W/S)
        if self.key_state.get('w', False):
            y += 1.0
        if self.key_state.get('s', False):
            y -= 1.0
        
        # Normalize diagonal movement to prevent faster diagonal speed
        if x != 0.0 and y != 0.0:
            length = math.sqrt(x * x + y * y)
            if length > 0:
                x /= length
                y /= length
        
        self.controller.set_left_stick(x, y)

    def _update_aim_stick(self):
        """
        Convert mouse delta to right stick values with smoothing and sensitivity.
        """
        with self.mouse_lock:
            dx = self.mouse_dx
            dy = self.mouse_dy
            
            if self.smoothing:
                # Apply decay for smoothing
                self.mouse_dx *= 0.7
                self.mouse_dy *= 0.7
            else:
                # Reset delta after reading
                self.mouse_dx = 0.0
                self.mouse_dy = 0.0
        
        # Apply sensitivity
        x = dx * self.sensitivity * 0.01
        y = dy * self.sensitivity * 0.01
        
        # Invert Y for FPS controls
        y = -y
        
        # Clamp to [-1.0, 1.0]
        x = max(-1.0, min(1.0, x))
        y = max(-1.0, min(1.0, y))
        
        self.controller.set_right_stick(x, y)
