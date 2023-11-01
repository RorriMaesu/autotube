# Import necessary modules and utilities
from utils import auto_ideogram, browser_utils, animation_utils, download_utils, video_editor_utils
from utils.tkinter_windows import TkinterManager
import config
import pyautogui
import logging
import pygame.mixer
from utils.browser_utils import close_browser
import time

# Initialize the pygame mixer for sound playback
pygame.mixer.init()

# Load sound files; replace with your own if you want
start_script_sound = pygame.mixer.Sound("sounds/meseeks_can_do.mp3")
stop_script_sound = pygame.mixer.Sound("sounds/pickle_rick.mp3")

# Play the startup sound
start_script_sound.play()

# Wait for the sound to finish playing
while pygame.mixer.get_busy():
    pygame.time.Clock().tick(10)

# Set pyautogui pause time between actions; adjust as needed
pyautogui.PAUSE = .72

# Initialize logging with INFO level
logging.basicConfig(level=logging.INFO)

# Initialize animated_counter from config; purpose unclear
config.animated_counter = 0

# Main function where all the magic happens
def main():
    try:
        # Run the initial script; needs clarification
        auto_ideogram.auto_ideogram_script()
        
        # Initialize Tkinter window manager; replace if using another GUI library
        tkinter_manager = TkinterManager()

        user_input = auto_ideogram.item_count
        
        browser_utils.switch_download_folders()
        
        # Flag for first upload; consider using a boolean
        first_upload = 1
        
        # Start animation phase; clarify purpose and functionality
        animation_utils.animation_phase(user_input, tkinter_manager, first_upload)
        
        # Initialize and start the download manager
        download_manager = download_utils.DownloadManager(user_input)
        time.sleep(3)
        download_manager.download_phase()
        
        # Pause for 2 seconds; reason for the user to read the console.
        time.sleep(2)
        

        # Run video editor utility; clarify what it edits
        video_editor_utils.run_video_editor_utility()
        
        # Play the stop sound
        stop_script_sound.play()

    # Basic exception handling
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()