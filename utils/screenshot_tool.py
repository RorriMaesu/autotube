import time
from PIL import ImageGrab
import pyperclip
import tempfile
import os

def main():
    print("Get ready, Morty! Screenshot incoming in 7 seconds!")
    time.sleep(7)
    
    # Take the screenshot
    screenshot = ImageGrab.grab()
    
    # Create a temporary file to save the screenshot
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        screenshot.save(temp_file.name)
    
    # Copy the temporary file path to the clipboard
    pyperclip.copy(temp_file.name)

    print(f"Screenshot saved and path copied to clipboard, Morty! File path: {temp_file.name}")

main()