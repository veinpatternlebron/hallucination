# 🎮 Usage Guide - Hallucination

Complete guide to using Hallucination controller mapper for FPS gaming.

## 🚀 Quick Start

1. **Launch Hallucination**
   ```bash
   python src/main.py
   ```

2. **Open your target game** (e.g., Roblox)

3. **Press F8** to enable input mapping

4. **Start playing** with keyboard and mouse!

5. **Press F8 again** to disable when done

## 🎯 Complete Keybind Reference

### Movement Controls

| Key | Controller Output | Function |
|-----|------------------|----------|
| W | Left Stick Up | Move Forward |
| A | Left Stick Left | Move Left |
| S | Left Stick Down | Move Backward |
| D | Left Stick Right | Move Right |
| W+A | Left Stick Up-Left | Diagonal Movement |
| W+D | Left Stick Up-Right | Diagonal Movement |
| S+A | Left Stick Down-Left | Diagonal Movement |
| S+D | Left Stick Down-Right | Diagonal Movement |

**Note**: Diagonal movement is automatically normalized to prevent faster diagonal speed.

### Camera/Aim Controls

| Input | Controller Output | Function |
|-------|------------------|----------|
| Mouse Movement | Right Stick | Camera/Aim Control |
| Move Mouse Left | Right Stick Left | Look Left |
| Move Mouse Right | Right Stick Right | Look Right |
| Move Mouse Up | Right Stick Up | Look Up |
| Move Mouse Down | Right Stick Down | Look Down |

### Action Buttons

| Key | Controller | Common Use |
|-----|-----------|-----------|
| Left Click | Right Trigger | Shoot/Primary Fire |
| Right Click | Left Trigger | Aim Down Sights/Secondary |
| Space | A Button | Jump |
| E | X Button | Interact/Use |
| R | Y Button | Reload |
| Q | B Button | Switch/Cancel |
| Shift | Left Bumper | Sprint/Run |
| Ctrl | Right Bumper | Crouch/Slide |
| C | Left Stick Click | Toggle Crouch |
| F | Right Stick Click | Melee Attack |
| Tab | Back Button | Scoreboard/Map |

### D-Pad Shortcuts

| Key | Controller | Common Use |
|-----|-----------|-----------|
| 1 | D-Pad Up | Weapon/Item Slot 1 |
| 2 | D-Pad Down | Weapon/Item Slot 2 |
| 3 | D-Pad Left | Weapon/Item Slot 3 |
| 4 | D-Pad Right | Weapon/Item Slot 4 |

### System Controls

| Key | Function |
|-----|----------|
| F8 | Toggle Hallucination On/Off |
| ESC | Close UI (stops mapping) |

## ⚙️ Sensitivity Adjustment

### Via UI Slider

1. Look at the Hallucination window
2. Move the "Sensitivity" slider
3. Changes apply immediately
4. Setting is auto-saved to config

### Via Config File

Edit `config.json`:

```json
{
  "sensitivity": 1.5
}
```

**Sensitivity Guide**:
- **0.1 - 0.5**: Very slow, precise aiming (sniping)
- **0.6 - 1.0**: Slow to medium (tactical games)
- **1.1 - 2.0**: Medium (most FPS games) ⭐ **Recommended**
- **2.1 - 3.5**: Fast (competitive play)
- **3.6 - 5.0**: Very fast (twitch shooters)

### Tips for Finding Your Sensitivity

1. Start at **1.5** (default)
2. Test a 180° turn - should be comfortable
3. If too slow, increase by 0.3
4. If too fast, decrease by 0.3
5. Fine-tune in 0.1 increments

## 🎪 Window Locking Explained

**Window locking** means Hallucination only sends controller input when the target game window is focused.

### How It Works

1. Hallucination checks active window every 0.5 seconds
2. If window title contains target name (e.g., "Roblox"), input is active
3. If you Alt+Tab away, input automatically stops
4. When you return to game, input resumes

### Configuring Target Window

Edit `config.json`:

```json
{
  "target_window": "Roblox"
}
```

**Finding Your Game's Window Name**:

Run this Python script:
```python
import pygetwindow as gw
for window in gw.getAllWindows():
    if window.title:
        print(window.title)
```

Look for your game's window title and use a unique part of it.

**Examples**:
- Roblox: `"target_window": "Roblox"`
- Fortnite: `"target_window": "Fortnite"`
- Call of Duty: `"target_window": "Call of Duty"`
- Apex Legends: `"target_window": "Apex Legends"`

## 🗺️ Custom Key Mapping Guide

### Basic Mapping Format

In `config.json`:

```json
{
  "key_mappings": {
    "keyboard_key": "controller_button"
  }
}
```

### Available Controller Buttons

- **Face Buttons**: `a`, `b`, `x`, `y`
- **Bumpers**: `lb`, `rb`
- **Stick Clicks**: `ls`, `rs`
- **Menu**: `back`, `start`
- **D-Pad**: `dpad_up`, `dpad_down`, `dpad_left`, `dpad_right`

### Example Custom Mappings

**For Battle Royale Games**:
```json
{
  "key_mappings": {
    "space": "a",
    "e": "x",
    "r": "y",
    "q": "b",
    "shift": "lb",
    "ctrl": "ls",
    "v": "rs",
    "f": "rb",
    "tab": "back",
    "m": "start",
    "1": "dpad_up",
    "2": "dpad_right"
  }
}
```

**For Parkour Games**:
```json
{
  "key_mappings": {
    "space": "a",
    "shift": "rb",
    "ctrl": "ls",
    "e": "x",
    "f": "y"
  }
}
```

**For Racing Games**:
```json
{
  "key_mappings": {
    "space": "a",
    "shift": "x",
    "ctrl": "b",
    "e": "y"
  }
}
```

## 🔄 Smoothing Toggle

Smoothing affects mouse-to-stick conversion.

### Smoothing ON (Default)

```json
{
  "smoothing": true
}
```

**Characteristics**:
- Gradual aim movement
- Reduces jitter and micro-adjustments
- Feels more like a real controller
- Better for consistent tracking

**Best for**:
- Tactical shooters
- Long-range engagements
- Controller-native games
- Players who prefer smooth aim

### Smoothing OFF

```json
{
  "smoothing": false
}
```

**Characteristics**:
- Instant aim response
- Direct mouse input
- More precise for quick flicks
- Can feel jittery

**Best for**:
- Fast-paced shooters
- Twitch aiming
- Competitive play
- Experienced KB/M players

## 💡 Pro Tips & Tricks

### For FPS Games

1. **Lower Sensitivity**: Start at 1.0-1.5 for better accuracy
2. **Enable Smoothing**: Makes aim feel more natural
3. **Practice Tracking**: Use training modes to adjust
4. **Use Right Click for ADS**: Matches standard FPS controls

### For Parkour/Movement Games

1. **Higher Sensitivity**: 2.0-3.0 for faster camera movement
2. **Disable Smoothing**: More responsive for quick adjustments
3. **Map Jump to A**: Standard jump button
4. **Map Sprint to LB**: Easy thumb access while moving

### For Third-Person Games

1. **Medium Sensitivity**: 1.5-2.0 for balance
2. **Enable Smoothing**: Smoother camera rotation
3. **Map Context Actions**: E to X for interact
4. **Use All Bumpers**: Map both LB and RB for quick access

### For Stealth Games

1. **Low Sensitivity**: 0.8-1.2 for precise camera control
2. **Enable Smoothing**: Smooth, controlled camera movement
3. **Map Crouch to LS**: Toggle crouch easily
4. **Map Use/Interact to X**: Standard interact button

## 🎯 Why Controller Mapping Gives an Advantage

### Aim Assist

Many games provide **aim assist** when using controllers:
- **Bullet Magnetism**: Shots slightly curve toward targets
- **Rotation Aim Assist**: Camera slows down when over enemies
- **Reticle Stickiness**: Crosshair "sticks" to targets

**With Hallucination**:
- You get KB/M precision
- **PLUS** controller aim assist
- Best of both worlds!

### Movement Options

Controller left stick allows:
- **Variable speed**: Tilt amount = move speed
- **Silent walking**: Slight tilt for quiet movement
- **Precise angles**: Any direction, not just 8-way

**With KB/M + Hallucination**:
- Full analog movement from WASD
- Diagonal normalization prevents speed exploits
- Smooth transitions between directions

### Game-Specific Benefits

**Roblox**:
- Some games have controller-only features
- Better vehicle control
- Smoother animations
- Native aim assist on shooter games

**Fortnite**:
- Strong aim assist on console/controller
- Building still precise with mouse
- Movement feels natural

**Apex Legends**:
- Aim assist on console lobbies
- Precise tracking with mouse
- Better recoil control

## 🚨 Troubleshooting

### Input Not Working

**Check**:
1. Is Hallucination enabled? (Status shows "🔥 ENABLED")
2. Is target window in focus? (Click on game window)
3. Does config `target_window` match game window name?
4. Press F8 to toggle on

### Aim Feels Wrong

**Solutions**:
- **Too Slow**: Increase sensitivity
- **Too Fast**: Decrease sensitivity
- **Jittery**: Enable smoothing
- **Laggy**: Disable smoothing

### Movement Feels Weird

**Check**:
- Make sure WASD keys are not mapped in game settings
- Verify key_state is updating (check console output)
- Try pressing one key at a time
- Restart Hallucination

### Controller Not Detected in Game

**Solutions**:
1. Start Hallucination BEFORE launching game
2. Or restart game after starting Hallucination
3. Enable controller support in game settings
4. Test in Windows Game Controllers (`joy.cpl`)

### F8 Toggle Not Working

**Solutions**:
- Check if another program uses F8
- Change toggle key in config:
  ```json
  {
    "toggle_key": "f9"
  }
  ```
- Run as Administrator

### High CPU/Lag

**Solutions**:
1. Disable smoothing
2. Lower sensitivity
3. Close other programs
4. Check for conflicting input software

## 📊 FAQ

### Q: Is this allowed in online games?

**A**: Check each game's Terms of Service. Some games prohibit input remapping tools. Use at your own risk.

### Q: Does this work on Linux/Mac?

**A**: No, ViGEm driver is Windows-only. This tool requires Windows 10/11.

### Q: Can I use this with Steam games?

**A**: Yes! Disable Steam Input for the game or set it to "Forced Off" in Steam game properties.

### Q: Will I get banned for using this?

**A**: Potentially, depending on the game. Some games consider input remapping cheating. Check ToS and use at your own risk.

### Q: Can I map more than one key to the same button?

**A**: Currently no. Each keyboard key maps to one controller button.

### Q: How do I switch between profiles quickly?

**A**: Create multiple config files (config_game1.json, config_game2.json) and manually copy to config.json, or edit the file between games.

### Q: Does mouse DPI affect sensitivity?

**A**: Yes, higher DPI = more sensitive. Adjust in-app sensitivity to compensate.

### Q: Can I use this with a controller plugged in?

**A**: Yes, but the game may detect both controllers. You may need to unplug the physical controller.

### Q: Does this work with wireless keyboard/mouse?

**A**: Yes, as long as they appear as standard HID devices in Windows.

### Q: Can I change the update rate from 120Hz?

**A**: Yes, edit `input_handler.py` and change `time.sleep(1.0 / 120.0)` to your desired Hz.

## 🔧 Advanced Usage

### Debug Mode

Add print statements in `input_handler.py` to debug:

```python
def _update_movement_stick(self):
    x = 0.0
    y = 0.0
    # ... existing code ...
    print(f"Movement: x={x}, y={y}")  # Add this
```

### Multiple Profiles

Create profile files:

```bash
config_roblox.json
config_fortnite.json
config_apex.json
```

Copy to `config.json` when switching games:

```bash
copy config_roblox.json config.json
```

### Custom Toggle Key

Change `toggle_key` in config:

```json
{
  "toggle_key": "f9"
}
```

Available keys: `f1`-`f12`, `insert`, `home`, `end`, `pageup`, `pagedown`, etc.

### Adjusting Smoothing Decay

Edit `input_handler.py`:

```python
def _update_aim_stick(self):
    # ...
    if self.smoothing:
        self.mouse_dx *= 0.7  # Change 0.7 to adjust (0.0-1.0)
        self.mouse_dy *= 0.7  # Lower = more smoothing
```

## 🎓 Best Practices

1. **Start Disabled**: Launch Hallucination but keep it disabled (F8) until you're in-game
2. **Test in Training**: Always test new settings in practice/training modes
3. **Backup Config**: Save your working config.json before experimenting
4. **Gradual Changes**: Adjust sensitivity in small increments
5. **Take Breaks**: Switch back to normal controls occasionally to avoid muscle memory issues

## 🎉 Enjoy!

You're now ready to dominate with KB/M precision and controller benefits!

For issues or questions:
- Check [SETUP.md](SETUP.md) for installation problems
- Create a GitHub issue for bugs
- Share your config files with the community!

---

**Happy Gaming! 🎮**
