# 📖 Setup Guide - Hallucination

Complete step-by-step installation guide for Hallucination controller mapper.

## 📋 Prerequisites

Before installing Hallucination, ensure you have:

- **Windows 10 or Windows 11** (64-bit)
- **Python 3.8 or higher**
- **Administrator privileges** (for ViGEm driver installation)
- **Stable internet connection** (for downloading dependencies)

## 🔧 Step 1: Install ViGEm Bus Driver

The ViGEm Bus Driver is **required** for virtual controller emulation.

### Download

1. Visit the official ViGEm releases page:
   - https://github.com/ViGEm/ViGEmBus/releases

2. Download the latest `ViGEmBus_Setup_x64.msi` installer

### Installation

1. **Run the installer** as Administrator
   - Right-click the downloaded file
   - Select "Run as administrator"

2. **Follow the installation wizard**
   - Accept the license agreement
   - Use default installation path
   - Click "Install"

3. **Restart your computer**
   - This is **required** for the driver to load properly

### Verification

After restart, verify the installation:

1. Open **Device Manager** (Win + X → Device Manager)
2. Look for "System devices" category
3. You should see "Virtual Gamepad Emulation Bus"

If you don't see it, the driver installation failed. Try:
- Running the installer again as Administrator
- Disabling Secure Boot in BIOS (if enabled)
- Checking Windows Event Viewer for error messages

## 🐍 Step 2: Install Python

### Check if Python is Already Installed

Open Command Prompt or PowerShell and run:

```bash
python --version
```

If you see `Python 3.8.x` or higher, skip to Step 3.

### Install Python

1. **Download Python**
   - Visit: https://www.python.org/downloads/
   - Download Python 3.8 or higher (latest stable recommended)

2. **Run the installer**
   - ✅ **IMPORTANT**: Check "Add Python to PATH"
   - Select "Install Now"
   - Wait for installation to complete

3. **Verify installation**
   ```bash
   python --version
   pip --version
   ```

Both commands should display version information.

## 📦 Step 3: Install Hallucination

### Download Hallucination

Clone or download the repository:

```bash
git clone https://github.com/veinpatternlebron/hallucination.git
cd hallucination
```

Or download the ZIP file and extract it.

### Install Python Dependencies

Open a terminal in the Hallucination directory and run:

```bash
pip install -r requirements.txt
```

This installs:
- `vgamepad==0.0.8` - Virtual controller library
- `pynput==1.7.6` - Input capture library
- `pygetwindow==0.0.9` - Window management
- `pywin32==306` - Windows API access
- `pillow==10.1.0` - Image processing (UI support)

### Verify Installation

Run Hallucination:

```bash
python src/main.py
```

You should see:
- Console output with "🎮 Hallucination" header
- A dark-themed UI window
- No error messages

If it works, **installation complete!** 🎉

## 🚨 Troubleshooting

### Error: "No module named 'vgamepad'"

**Problem**: vgamepad failed to install

**Solutions**:
1. Ensure ViGEm driver is installed first
2. Run pip with admin privileges:
   ```bash
   pip install --user -r requirements.txt
   ```
3. Try installing vgamepad separately:
   ```bash
   pip install vgamepad==0.0.8
   ```

### Error: "ViGEmClient.dll not found"

**Problem**: ViGEm driver not properly installed

**Solutions**:
1. Reinstall ViGEm driver as Administrator
2. Restart your computer
3. Check Device Manager for "Virtual Gamepad Emulation Bus"
4. Download Visual C++ Redistributable:
   - https://aka.ms/vs/17/release/vc_redist.x64.exe

### Error: "ModuleNotFoundError: No module named 'win32api'"

**Problem**: pywin32 not properly installed

**Solutions**:
1. Reinstall pywin32:
   ```bash
   pip uninstall pywin32
   pip install pywin32==306
   ```
2. Run post-install script:
   ```bash
   python Scripts/pywin32_postinstall.py -install
   ```

### Error: High CPU Usage (100%)

**Problem**: Update loop running too fast or smoothing issues

**Solutions**:
1. Disable smoothing in `config.json`:
   ```json
   "smoothing": false
   ```
2. Close other background applications
3. Lower sensitivity in UI
4. Check for other programs using mouse/keyboard hooks

### Controller Not Detected in Game

**Problem**: Game doesn't recognize virtual controller

**Solutions**:
1. Restart the game after starting Hallucination
2. Enable controller support in game settings
3. Test controller in Windows Game Controllers:
   - Run `joy.cpl` in Windows Run dialog
   - You should see "Xbox 360 Controller"
4. Some games require enabling "Steam Input" or similar

### Permission Errors

**Problem**: Access denied when running

**Solutions**:
1. Run terminal as Administrator
2. Check antivirus/firewall isn't blocking vgamepad
3. Add exception for Python and Hallucination folder
4. Temporarily disable antivirus to test

### UI Window Doesn't Appear

**Problem**: Tkinter issues or window rendering problems

**Solutions**:
1. Check if Python has Tkinter:
   ```bash
   python -m tkinter
   ```
   A small window should appear
2. Reinstall Python with Tkinter option enabled
3. Update graphics drivers
4. Try running without UI (edit code to skip UI initialization)

### Mouse Input Not Working

**Problem**: Mouse events not captured

**Solutions**:
1. Run as Administrator
2. Check if other programs are hooking mouse input
3. Disable mouse acceleration in Windows settings
4. Test with different mouse/drivers
5. Check `pynput` installation:
   ```bash
   pip uninstall pynput
   pip install pynput==1.7.6
   ```

### Target Window Not Detected

**Problem**: Window locking not working

**Solutions**:
1. Change `target_window` in `config.json` to exact window title
2. Find exact window name:
   ```python
   import pygetwindow as gw
   print([w.title for w in gw.getAllWindows()])
   ```
3. Make sure game window is in focus
4. Try running game in windowed/borderless mode

## ✅ Post-Installation Checklist

After installation, verify everything works:

- [ ] ViGEm driver installed (check Device Manager)
- [ ] Python 3.8+ installed (`python --version`)
- [ ] All dependencies installed (`pip list`)
- [ ] Hallucination launches without errors
- [ ] UI window appears with dark theme
- [ ] Virtual controller visible in `joy.cpl`
- [ ] Target window detected when focused
- [ ] F8 toggle works
- [ ] Sensitivity slider responds

## 🎯 Next Steps

Once installation is complete:

1. Read [USAGE.md](USAGE.md) for complete usage guide
2. Configure `config.json` for your game
3. Test with target game
4. Adjust sensitivity and key mappings
5. Enjoy KB/M precision with controller input! 🎮

## 🔄 Updating Hallucination

To update to the latest version:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## 🗑️ Uninstalling

To completely remove Hallucination:

1. Delete the Hallucination folder
2. Uninstall Python packages:
   ```bash
   pip uninstall vgamepad pynput pygetwindow pywin32 pillow
   ```
3. Optionally uninstall ViGEm driver:
   - Control Panel → Programs → Uninstall "ViGEm Bus Driver"

## 💬 Getting Help

If you're still having issues:

1. Check [USAGE.md](USAGE.md) FAQ section
2. Search existing GitHub issues
3. Create a new issue with:
   - Your Python version
   - Full error message
   - Steps to reproduce
   - Your OS version

---

**Installation complete? Head to [USAGE.md](USAGE.md) to learn how to use Hallucination!**
