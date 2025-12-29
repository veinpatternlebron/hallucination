"""
Main Entry Point - Hallucination Controller Mapper
"""
import sys
from pynput import keyboard

from src.virtual_controller import VirtualController
from src.window_manager import WindowManager
from src.config_manager import ConfigManager
from src.input_handler import InputHandler
from src.ui.main_window import MainWindow


class Hallucination:
    """
    Main application class for Hallucination controller mapper.
    Orchestrates all components and manages the application lifecycle.
    """

    def __init__(self):
        """Initialize all components."""
        print("🎮 Hallucination - FPS Controller Mapper")
        print("=" * 50)
        
        # Load configuration
        self.config = ConfigManager()
        print(f"⚙️  Sensitivity: {self.config.get('sensitivity')}")
        print(f"🎯 Target Window: {self.config.get('target_window')}")
        print(f"🔑 Toggle Key: {self.config.get('toggle_key').upper()}")
        
        # Initialize components
        self.controller = VirtualController()
        print("✅ Virtual controller initialized")
        
        self.window_manager = WindowManager(self.config.get('target_window', 'Roblox'))
        print("✅ Window manager initialized")
        
        self.input_handler = InputHandler(self.controller, self.window_manager, self.config)
        print("✅ Input handler initialized")
        
        # State
        self.enabled = False
        
        # Setup toggle hotkey
        self.setup_toggle_hotkey()
        
        # Create UI
        self.ui = None

    def setup_toggle_hotkey(self):
        """Setup global toggle hotkey listener."""
        toggle_key_name = self.config.get('toggle_key', 'f8').lower()
        
        def on_press(key):
            try:
                if hasattr(key, 'name') and key.name.lower() == toggle_key_name:
                    self.toggle()
                elif hasattr(key, 'char') and key.char and key.char.lower() == toggle_key_name:
                    self.toggle()
            except Exception:
                pass
        
        # Start hotkey listener
        self.hotkey_listener = keyboard.Listener(on_press=on_press)
        self.hotkey_listener.daemon = True
        self.hotkey_listener.start()
        print(f"✅ Toggle hotkey ({toggle_key_name.upper()}) registered")

    def toggle(self):
        """Toggle input handler on/off."""
        self.enabled = not self.enabled
        
        if self.enabled:
            self.input_handler.start()
            print("🔥 Hallucination ENABLED")
        else:
            self.input_handler.stop()
            print("⏸️  Hallucination DISABLED")
        
        # Update UI if available
        if self.ui:
            self.ui.update_status(self.enabled)

    def update_sensitivity(self, value: float):
        """
        Update sensitivity setting.
        
        Args:
            value: New sensitivity value
        """
        self.config.set('sensitivity', value)
        self.input_handler.set_sensitivity(value)

    def run(self):
        """Start the application."""
        print("=" * 50)
        print(f"🚀 Starting Hallucination UI...")
        print(f"💡 Press {self.config.get('toggle_key', 'f8').upper()} to toggle input mapping")
        print(f"💡 Only works when '{self.config.get('target_window')}' window is active")
        print("=" * 50)
        
        # Create and run UI
        self.ui = MainWindow(self)
        self.ui.run()

    def shutdown(self):
        """Cleanup and shutdown all components."""
        print("\n🛑 Shutting down...")
        
        if self.enabled:
            self.input_handler.stop()
        
        if self.hotkey_listener:
            self.hotkey_listener.stop()
        
        self.controller.disconnect()
        print("✅ Shutdown complete")


def main():
    """Main entry point."""
    app = None
    try:
        app = Hallucination()
        app.run()
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if app:
            app.shutdown()


if __name__ == "__main__":
    main()
