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
        font=("Arial", 18, "bold"), # CORRECTED: Added closing quote and 'bold'
        fg="red" # Added text color red for emphasis
    )
    warning_label.pack(expand=True)

    # Automatically close the warning after a short delay (e.g., 2000 milliseconds = 2 seconds)
    warning_window.after(2000, warning_window.destroy)

# --- Main application setup ---
# Initialize the main Tkinter window (it can be hidden if you only want the blocker)
root = tk.Tk()
root.withdraw() # Hide the main window

# Start the copy-paste blocking in a separate thread
# This prevents the blocking from freezing the Tkinter GUI (though it's hidden)
blocking_thread = threading.Thread(target=block_copy_paste, daemon=True)
blocking_thread.start()

# Start the Tkinter event loop
# This is necessary for the warning messages to appear
root.mainloop()
