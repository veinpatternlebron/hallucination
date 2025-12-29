"""
MainWindow - Tkinter UI with Dark Theme
"""
import tkinter as tk
from tkinter import ttk


class MainWindow:
    """
    Main UI window for Hallucination.
    Dark themed interface with status, sensitivity slider, and toggle button.
    """

    def __init__(self, app):
        """
        Initialize main window.
        
        Args:
            app: Main Hallucination application instance
        """
        self.app = app
        self.root = tk.Tk()
        self.root.title("Hallucination")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg='#1a1a1a')
        
        # Setup styles
        self.setup_styles()
        
        # Build UI
        self.build_ui()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def setup_styles(self):
        """Setup dark theme with ttk.Style."""
        style = ttk.Style()
        
        # Configure dark theme colors
        style.theme_use('clam')
        
        # Configure scale (slider) style
        style.configure(
            "Horizontal.TScale",
            background='#1a1a1a',
            troughcolor='#333333',
            bordercolor='#1a1a1a',
            lightcolor='#1a1a1a',
            darkcolor='#1a1a1a'
        )

    def build_ui(self):
        """Create all UI elements."""
        # Title
        title_label = tk.Label(
            self.root,
            text="🎮 Hallucination",
            font=("Arial", 20, "bold"),
            fg="#00ff00",
            bg="#1a1a1a"
        )
        title_label.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="⏸️ DISABLED",
            font=("Arial", 16, "bold"),
            fg="#ff0000",
            bg="#1a1a1a"
        )
        self.status_label.pack(pady=10)
        
        # Sensitivity frame
        sensitivity_frame = tk.Frame(self.root, bg='#1a1a1a')
        sensitivity_frame.pack(pady=15, padx=20, fill='x')
        
        sensitivity_label = tk.Label(
            sensitivity_frame,
            text="Sensitivity:",
            font=("Arial", 10),
            fg="#ffffff",
            bg="#1a1a1a"
        )
        sensitivity_label.pack(side='left')
        
        # Sensitivity value display
        self.sensitivity_value_label = tk.Label(
            sensitivity_frame,
            text=f"{self.app.config.get('sensitivity', 1.5):.1f}",
            font=("Arial", 10),
            fg="#00ff00",
            bg="#1a1a1a"
        )
        self.sensitivity_value_label.pack(side='right')
        
        # Sensitivity slider
        self.sensitivity_slider = ttk.Scale(
            self.root,
            from_=0.1,
            to=5.0,
            orient='horizontal',
            command=self.on_sensitivity_change,
            style="Horizontal.TScale"
        )
        self.sensitivity_slider.set(self.app.config.get('sensitivity', 1.5))
        self.sensitivity_slider.pack(pady=5, padx=20, fill='x')
        
        # Toggle button
        self.toggle_button = tk.Button(
            self.root,
            text="Enable",
            font=("Arial", 12, "bold"),
            fg="#ffffff",
            bg="#00aa00",
            activebackground="#00ff00",
            command=self.on_toggle,
            width=15,
            height=2
        )
        self.toggle_button.pack(pady=15)
        
        # Info text
        info_text = (
            "Hotkey: F8 to toggle\n"
            f"Target: {self.app.config.get('target_window', 'Roblox')}\n"
            "Mouse: Right stick (aim)\n"
            "WASD: Left stick (move)"
        )
        info_label = tk.Label(
            self.root,
            text=info_text,
            font=("Arial", 8),
            fg="#666666",
            bg="#1a1a1a",
            justify='center'
        )
        info_label.pack(pady=10)

    def on_sensitivity_change(self, value):
        """
        Slider callback for sensitivity changes.
        
        Args:
            value: New sensitivity value
        """
        sens_value = float(value)
        self.sensitivity_value_label.config(text=f"{sens_value:.1f}")
        self.app.update_sensitivity(sens_value)

    def on_toggle(self):
        """Toggle button callback."""
        self.app.toggle()

    def update_status(self, enabled: bool):
        """
        Update UI status display.
        
        Args:
            enabled: True if enabled, False if disabled
        """
        if enabled:
            self.status_label.config(text="🔥 ENABLED", fg="#00ff00")
            self.toggle_button.config(text="Disable", bg="#aa0000", activebackground="#ff0000")
        else:
            self.status_label.config(text="⏸️ DISABLED", fg="#ff0000")
            self.toggle_button.config(text="Enable", bg="#00aa00", activebackground="#00ff00")

    def on_close(self):
        """Window close callback."""
        self.app.shutdown()
        self.root.destroy()

    def run(self):
        """Start Tkinter mainloop."""
        self.root.mainloop()
