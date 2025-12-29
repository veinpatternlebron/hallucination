"""
VirtualController - Xbox 360 Controller Emulation using vgamepad
"""
import vgamepad as vg


class VirtualController:
    """
    Manages virtual Xbox 360 controller using vgamepad library.
    Provides high-level interface for setting sticks, buttons, and triggers.
    """

    def __init__(self):
        """Initialize the virtual Xbox 360 controller."""
        self.gamepad = vg.VX360Gamepad()
        self.button_map = {
            'a': vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
            'b': vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
            'x': vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
            'y': vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
            'lb': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
            'rb': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
            'back': vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
            'start': vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
            'ls': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
            'rs': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
            'dpad_up': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
            'dpad_down': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
            'dpad_left': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
            'dpad_right': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
        }

    def set_left_stick(self, x: float, y: float):
        """
        Set left stick position.
        
        Args:
            x: Horizontal position from -1.0 (left) to 1.0 (right)
            y: Vertical position from -1.0 (down) to 1.0 (up)
        """
        # Convert from -1.0/1.0 range to -32768/32767 range
        x_value = int(x * 32767)
        y_value = int(y * 32767)
        self.gamepad.left_joystick(x_axis=x_value, y_axis=y_value)

    def set_right_stick(self, x: float, y: float):
        """
        Set right stick position.
        
        Args:
            x: Horizontal position from -1.0 (left) to 1.0 (right)
            y: Vertical position from -1.0 (down) to 1.0 (up)
        """
        # Convert from -1.0/1.0 range to -32768/32767 range
        x_value = int(x * 32767)
        y_value = int(y * 32767)
        self.gamepad.right_joystick(x_axis=x_value, y_axis=y_value)

    def press_button(self, button_name: str):
        """
        Press a button by name.
        
        Args:
            button_name: Button name (a, b, x, y, lb, rb, back, start, ls, rs, dpad_up, etc.)
        """
        if button_name.lower() in self.button_map:
            self.gamepad.press_button(button=self.button_map[button_name.lower()])

    def release_button(self, button_name: str):
        """
        Release a button by name.
        
        Args:
            button_name: Button name (a, b, x, y, lb, rb, back, start, ls, rs, dpad_up, etc.)
        """
        if button_name.lower() in self.button_map:
            self.gamepad.release_button(button=self.button_map[button_name.lower()])

    def set_left_trigger(self, value: int):
        """
        Set left trigger value.
        
        Args:
            value: Trigger value from 0 (released) to 255 (fully pressed)
        """
        value = max(0, min(255, value))
        self.gamepad.left_trigger(value=value)

    def set_right_trigger(self, value: int):
        """
        Set right trigger value.
        
        Args:
            value: Trigger value from 0 (released) to 255 (fully pressed)
        """
        value = max(0, min(255, value))
        self.gamepad.right_trigger(value=value)

    def update(self):
        """Send all input changes to the virtual controller."""
        self.gamepad.update()

    def reset(self):
        """Reset all inputs to neutral state."""
        self.set_left_stick(0, 0)
        self.set_right_stick(0, 0)
        self.set_left_trigger(0)
        self.set_right_trigger(0)
        # Release all buttons
        for button_name in self.button_map.keys():
            self.release_button(button_name)
        self.update()

    def disconnect(self):
        """Cleanup and disconnect the virtual controller."""
        self.reset()
        del self.gamepad
