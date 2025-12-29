"""
WindowManager - Active Window Detection
"""
import time
try:
    import pygetwindow as gw
except ImportError:
    gw = None


class WindowManager:
    """
    Manages window detection and targeting.
    Caches active window checks to reduce performance impact.
    """

    def __init__(self, target_window_name: str = "Roblox"):
        """
        Initialize window manager.
        
        Args:
            target_window_name: Name of the target window to detect (default: "Roblox")
        """
        self.target_window_name = target_window_name
        self._last_check_time = 0
        self._last_check_result = False
        self._check_interval = 0.5  # Check every 0.5 seconds
        
        if gw is None:
            print("⚠️  Warning: pygetwindow not available, window locking disabled")

    def is_target_active(self) -> bool:
        """
        Check if target window is currently active.
        Uses caching to reduce performance impact.
        
        Returns:
            True if target window is active, False otherwise
        """
        if gw is None:
            return True  # If pygetwindow not available, always return True
        
        current_time = time.time()
        
        # Use cached result if within check interval
        if current_time - self._last_check_time < self._check_interval:
            return self._last_check_result
        
        # Perform actual check
        self._last_check_time = current_time
        
        try:
            active_window = gw.getActiveWindow()
            if active_window is None:
                self._last_check_result = False
                return False
            
            # Check if target window name is in the active window title
            active_title = active_window.title
            self._last_check_result = self.target_window_name.lower() in active_title.lower()
            return self._last_check_result
        except Exception:
            # If there's an error getting window info, default to False
            self._last_check_result = False
            return False

    def get_active_window_title(self) -> str:
        """
        Get the title of the currently active window.
        
        Returns:
            Title of active window, or empty string if unavailable
        """
        if gw is None:
            return ""
        
        try:
            active_window = gw.getActiveWindow()
            if active_window is None:
                return ""
            return active_window.title
        except Exception:
            return ""
