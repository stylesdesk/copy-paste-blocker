import tkinter as tk
from tkinter import messagebox
import keyboard
import threading

def block_copy_paste():
    """Block copy, cut, and paste commands using add_hotkey."""
    def on_blocked_key(): # No 'event' argument needed for add_hotkey's callback
        """Show warning message in red on the screen."""
        show_warning_message()

    # Use add_hotkey for robust combination detection AND suppress the original key event
    keyboard.add_hotkey("ctrl+c", on_blocked_key, suppress=True) # ADDED suppress=True
    keyboard.add_hotkey("ctrl+v", on_blocked_key, suppress=True) # ADDED suppress=True
    keyboard.add_hotkey("ctrl+x", on_blocked_key, suppress=True) # ADDED suppress=True
    
    keyboard.wait("esc")  # Stop blocking when 'Esc' is pressed

def show_warning_message():
    """Display a warning message in the center of the screen."""
    warning_window = tk.Toplevel(root)
    warning_window.title("Blocked Command")
    warning_window.geometry("400x200")
    warning_window.resizable(False, False)
    
    # Make the window appear on top
    warning_window.attributes("-topmost", True)
    
    # Calculate position to center the window (optional, but nice for popups)
    screen_width = warning_window.winfo_screenwidth()
    screen_height = warning_window.winfo_screenheight()
    
    x = (screen_width / 2) - (400 / 2) # 400 is window width
    y = (screen_height / 2) - (200 / 2) # 200 is window height
    warning_window.geometry(f'+{int(x)}+{int(y)}') # Set position

    # Create a red warning message
    warning_label = tk.Label(
        warning_window, 
        text="YOU CAN NOT USE THIS COMMAND", 
        font=("Arial", 18, "bold"), 
        fg="red" 
    )
    warning_label.pack(expand=True)

    # Automatically close the warning after a short delay (e.g., 2000 milliseconds = 2 seconds)
    warning_window.after(2000, warning_window.destroy)

# --- Main application setup ---
root = tk.Tk()
root.withdraw() # Hide the main window to keep it in the background

blocking_thread = threading.Thread(target=block_copy_paste, daemon=True)
blocking_thread.start()

root.mainloop()
