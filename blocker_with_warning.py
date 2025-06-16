import tkinter as tk
from tkinter import messagebox
import keyboard
import tkinter as tk
from tkinter import messagebox
import keyboard
import threading

def block_copy_paste():
    """Block copy, cut, and paste commands."""
    def on_blocked_key(event):
        """Show warning message in red on the screen."""
        show_warning_message()

    keyboard.on_press_key("ctrl+c", on_blocked_key)
    keyboard.on_press_key("ctrl+v", on_blocked_key)
    keyboard.on_press_key("ctrl+x", on_blocked_key)
    keyboard.wait("esc")  # Stop blocking when 'Esc' is pressed

def show_warning_message():
    """Display a warning message in the center of the screen."""
    warning_window = tk.Toplevel(root)
    warning_window.title("Blocked Command")
    warning_window.geometry("400x200")
    warning_window.resizable(False, False)
    
    # Make the window appear on top
    warning_window.attributes("-topmost", True)
    
    # Create a red warning message
    warning_label = tk.Label(
        warning_window, 
        text="YOU CAN NOT USE THIS COMMAND", 
        font=("Arial", 18, "b
