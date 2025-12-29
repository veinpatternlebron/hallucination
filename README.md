# 🎮 Hallucination - FPS Keyboard/Mouse to Xbox Controller Mapper

A sophisticated input remapping tool that converts keyboard and mouse inputs into Xbox controller signals, enabling controller-only games to be played with KB/M precision.

## ✨ Features

- 🎯 **Virtual Xbox 360 Controller** - Creates a virtual controller using ViGEm driver
- 🖱️ **Mouse to Right Stick** - Ultra-responsive mouse aim with configurable sensitivity
- ⌨️ **WASD to Left Stick** - Smooth movement with diagonal normalization
- 🎪 **Window Locking** - Only active when target game window is focused
- ⚡ **120Hz Update Rate** - Ultra-low latency for competitive gaming
- 🎨 **Dark Themed UI** - Clean, modern interface with real-time status
- ⚙️ **JSON Configuration** - Fully customizable key mappings and settings
- 🔥 **Global Hotkey Toggle** - Quick enable/disable with F8 (configurable)
- 🔄 **Smooth Aim** - Optional smoothing to reduce jitter at high sensitivity
- 📊 **Performance Optimized** - Efficient threading and minimal CPU usage

## 🚀 Quick Start

1. **Install ViGEm Driver** (see [Setup Guide](docs/SETUP.md))
2. **Install Python 3.8+**
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Hallucination:**
   ```bash
   python src/main.py
   ```
5. **Press F8 to toggle** (only works when target window is active)

## 📋 Installation

### Prerequisites

- Windows 10/11
- Python 3.8 or higher
- ViGEm Bus Driver

### Step 1: Install ViGEm Driver

Download and install the ViGEm Bus Driver from:
https://github.com/ViGEm/ViGEmBus/releases

Run the installer and restart your computer if prompted.

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python src/main.py
```

## 🎮 Default Keybinds

| Keyboard Input | Controller Output | Purpose |
|---------------|------------------|---------|
| WASD | Left Stick | Movement |
| Mouse Movement | Right Stick | Camera/Aim |
| Left Click | Right Trigger | Shoot/Primary |
| Right Click | Left Trigger | ADS/Secondary |
| Space | A Button | Jump |
| E | X Button | Interact |
| R | Y Button | Reload |
| Q | B Button | Switch/Back |
| Shift | Left Bumper | Sprint |
| Ctrl | Right Bumper | Crouch |
| C | Left Stick Click | Crouch (alt) |
| F | Right Stick Click | Melee |
| Tab | Back Button | Scoreboard |
| 1 | D-Pad Up | Item/Slot 1 |
| 2 | D-Pad Down | Item/Slot 2 |
| 3 | D-Pad Left | Item/Slot 3 |
| 4 | D-Pad Right | Item/Slot 4 |
| F8 | Toggle On/Off | Enable/Disable |

## ⚙️ Configuration

Edit `config.json` to customize settings:

```json
{
  "sensitivity": 1.5,
  "smoothing": true,
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
```

### Configuration Options

- **sensitivity** (0.1 - 5.0): Mouse sensitivity multiplier
- **smoothing** (true/false): Enable smooth aim to reduce jitter
- **toggle_key**: Key to enable/disable mapping (default: f8)
- **target_window**: Game window name to detect (e.g., "Roblox", "Fortnite")
- **key_mappings**: Custom key to button mappings

### Controller Button Names

Use these in key_mappings:
- `a`, `b`, `x`, `y` - Face buttons
- `lb`, `rb` - Bumpers
- `ls`, `rs` - Stick clicks
- `back`, `start` - Menu buttons
- `dpad_up`, `dpad_down`, `dpad_left`, `dpad_right` - D-Pad

## 📊 How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    Hallucination Flow                        │
└─────────────────────────────────────────────────────────────┘

  Keyboard Input (WASD)          Mouse Input (Movement/Clicks)
         │                                    │
         ├────────────────┬───────────────────┤
         │                │                   │
         ▼                ▼                   ▼
   Key Mappings    WASD→Left Stick    Mouse→Right Stick
         │                │                   │
         └────────────────┴───────────────────┘
                          │
                          ▼
                 Window Active Check
                          │
                          ▼
                Virtual Xbox Controller
                          │
                          ▼
                   Game Receives Input
```

## 🔧 Advanced Usage

### Custom Key Profiles

Create multiple config files for different games:

```bash
python src/main.py  # Uses config.json
# Manually edit config.json for each game profile
```

### Adjusting Sensitivity

- Use the UI slider for real-time adjustment
- Or edit `config.json` and restart
- Range: 0.1 (slow) to 5.0 (fast)
- Recommended: 1.0 - 2.0 for most games

### Smoothing vs Raw Input

- **Smoothing ON**: Reduces jitter, feels more like controller
- **Smoothing OFF**: More responsive, direct mouse input
- Toggle in `config.json`: `"smoothing": true/false`

## ⚠️ Disclaimer

This tool is for educational and accessibility purposes. Using input remapping tools may violate the Terms of Service of some games. Use at your own risk. The authors are not responsible for any consequences of using this software.

## 🐛 Troubleshooting

### Controller Not Detected
- Ensure ViGEm driver is installed
- Restart computer after ViGEm installation
- Check Windows Device Manager for "Virtual Gamepad Emulation Bus"

### Input Not Working
- Check that target window name matches in config
- Ensure window is focused (click on game)
- Press F8 to toggle on (check UI for ENABLED status)

### High CPU Usage
- Increase sleep time in update loop (edit source)
- Disable smoothing in config
- Close other background applications

### Permission Errors
- Run as Administrator
- Check antivirus isn't blocking vgamepad

See [SETUP.md](docs/SETUP.md) and [USAGE.md](docs/USAGE.md) for more details.

## 📚 Documentation

- [Setup Guide](docs/SETUP.md) - Detailed installation instructions
- [Usage Guide](docs/USAGE.md) - Complete usage documentation and tips

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Credits

- **vgamepad** - Virtual controller emulation
- **pynput** - Keyboard and mouse input capture
- **ViGEm** - Virtual gamepad driver

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

---

**Made with ❤️ for the gaming community** 
