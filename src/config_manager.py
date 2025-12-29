"""
ConfigManager - JSON Configuration Management
"""
import json
import os


class ConfigManager:
    """
    Manages configuration loading, saving, and access.
    Auto-creates default config if missing.
    """

    DEFAULT_CONFIG = {
        "sensitivity": 1.5,
        "smoothing": True,
        "toggle_key": "f8",
        "target_window": "Roblox",
        "key_mappings": {
            "space": "a",
            "e": "x",
            "r": "y",
            "q": "b",
            "shift": "lb",
            "ctrl": "rb",
            "c": "ls",
            "f": "rs",
            "tab": "back",
            "1": "dpad_up",
            "2": "dpad_down",
            "3": "dpad_left",
            "4": "dpad_right"
        }
    }

    def __init__(self, config_file: str = "config.json"):
        """
        Initialize config manager.
        
        Args:
            config_file: Path to config file (default: "config.json")
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> dict:
        """
        Load configuration from JSON file.
        Creates default config if file doesn't exist.
        
        Returns:
            Configuration dictionary
        """
        if not os.path.exists(self.config_file):
            print(f"📄 Config file not found, creating default: {self.config_file}")
            self.save_config(self.DEFAULT_CONFIG)
            return self.DEFAULT_CONFIG.copy()
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                print(f"✅ Loaded config from: {self.config_file}")
                return config
        except Exception as e:
            print(f"⚠️  Error loading config: {e}")
            print(f"📄 Using default configuration")
            return self.DEFAULT_CONFIG.copy()

    def save_config(self, config: dict = None):
        """
        Save configuration to JSON file.
        
        Args:
            config: Configuration dictionary to save (default: current config)
        """
        if config is None:
            config = self.config
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print(f"⚠️  Error saving config: {e}")

    def get(self, key: str, default=None):
        """
        Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        return self.config.get(key, default)

    def set(self, key: str, value):
        """
        Set configuration value and auto-save.
        
        Args:
            key: Configuration key
            value: Value to set
        """
        self.config[key] = value
        self.save_config()
