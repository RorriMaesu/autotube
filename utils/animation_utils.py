import pyautogui
import shutil
import pytesseract
import time
import os
import queue
import threading
import keyboard
from .tkinter_windows import TkinterManager  # Import the TkinterManager class
from config import ANIMATION_DURATION  # Importing from config.py
from .browser_utils import click_nakshatra_folder, goto_url # Relative import
from config import animated_counter
from .video_editor_utils import find_question_mark_icon_click_drop_down_to_the_left


# Update this path to where you've installed Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

pyautogui.PAUSE = 1  # pause for each action

#This will need to be set to your own still images folder path
still_images_path = 'C:\\Users\\autotube\\Documents\\Shravana\\still images'

def click_message_box():
    prompt_box_location = None
    while not prompt_box_location:
        prompt_box_location = pyautogui.locateOnScreen('images/prompt_box.png', confidence=0.8)
        if not prompt_box_location:
            print("Message box image not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    prompt_box_center = pyautogui.center(prompt_box_location)
    pyautogui.click(prompt_box_center)
    print("Message box clicked!")
    time.sleep(1)
    

def increment_animated_counter(animation_queue):
    global animated_counter
    animated_counter += 1
    animation_queue.put(animated_counter)

def animate():
    pyautogui.write('/animate')
    time.sleep(1)
    pyautogui.press('enter')
    print("Typed /animate prompt.")

def upload_image():
    select_image_location = None
    while not select_image_location:
        select_image_location = pyautogui.locateOnScreen('images/select_image.png', confidence=0.8)
        if not select_image_location:
            print("Select Image Button not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    select_image_location_center = pyautogui.center(select_image_location)
    pyautogui.click(select_image_location_center)
    print("Image upload button clicked!")
    time.sleep(.5)


def click_icon_size_dropdown():
    search_region = [231, 18, 1900, 500]
    drop_down_location = None
    while not drop_down_location:
        drop_down_location = pyautogui.locateOnScreen('images/file_preview_drop_down_image.png', confidence=0.9, region = search_region)
        if not drop_down_location:
            print("Icon dropdown not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    drop_down_location_center = pyautogui.center(drop_down_location)
    pyautogui.click(drop_down_location_center)
    print("Clicked the icon size drop down.")


def click_extra_large_icon_button():
    extra_large_icon_button_location = None
    while not extra_large_icon_button_location:
        extra_large_icon_button_location = pyautogui.locateOnScreen('images/extra_large_icons_button_image.png', confidence=0.9) 
        if not extra_large_icon_button_location:
            print("Extra large icons button image image not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    extra_large_icon_button_location_center = pyautogui.center(extra_large_icon_button_location)
    pyautogui.click(extra_large_icon_button_location_center)
    print("Clicked the extra large icon button!")


def click_desktop_icon(first_upload):
    start_time = time.time()  # Get the current time
    search_region = (0, 0, 153, 73)
    desktop_image_location = None
    
    while not desktop_image_location:
        current_time = time.time()
        elapsed_time = current_time - start_time  # Calculate elapsed time

        # Check if the image is found in the given region
        desktop_image_location = pyautogui.locateOnScreen('images/desktop_icon_image.png', region=search_region, confidence=0.8)
        
        # If the image is not found and the elapsed time is greater than 3 seconds or first_upload is 0
        if not desktop_image_location and (first_upload == 0 or elapsed_time > 3):
            print("Could not find a desktop icon. Moving on.")
            return
        elif not desktop_image_location:
            print("Desktop Icon not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    desktop_image_location_center = pyautogui.center(desktop_image_location)
    pyautogui.click(desktop_image_location_center)
    print("Clicked desktop icon!")
    time.sleep(.5)

def click_folder_icon(first_upload):
    start_time = time.time()  # Get the current time, Morty
    search_region = (0, 0, 318, 150)  # This time we'll actually use it
    folder_icon_image_location = None
    
    while not folder_icon_image_location:
        current_time = time.time()
        elapsed_time = current_time - start_time  # How much time has passed, Morty?

        if first_upload == 0 or elapsed_time > 10:  # If more than 10 seconds have passed
            print("No folder icon! Moving on.")
            return  # Get outta here!
        
        folder_icon_image_location = pyautogui.locateOnScreen('images/folder_icon_image.png', region=search_region, confidence=0.9)
        
        if not folder_icon_image_location:
            print("Folder Icon not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    folder_icon_image_location_center = pyautogui.center(folder_icon_image_location)
    pyautogui.click(folder_icon_image_location_center)
    time.sleep(.5)


# Make sure to change this path to fit your pc file path. The variable to edit is at the top of this script and called still_images_path
def goto_still_images_path():
    pyautogui.write(still_images_path)
    time.sleep(1)
    pyautogui.press('enter')

def select_image(first_upload):
    if first_upload == 1:
        print("On first upload, so making sure the icons are max size!")
        click_icon_size_dropdown()
        click_extra_large_icon_button()
    pyautogui.doubleClick(x=328, y=300)
    print("Clicked default coordinates.")

def type_animation_prompt():
    pyautogui.write("-neg morphing, erratic fluctuation in motion, noisy, bad quality, distorted, poorly drawn, blurry, grainy, low resolution, oversaturated, lack of detail, inconsistent lighting.")
    pyautogui.press('enter')
    print("Typed video animation instructions.")
    
def click_1more():
    one_more_location = None
    while not one_more_location:
        one_more_location = pyautogui.locateOnScreen('images/one_more.png', confidence=0.8)
        if not one_more_location:
            print("1more button image not found! Retrying in .5 seconds...")
            time.sleep(.5)  # Wait for a short period before trying again to reduce CPU usage

    one_more_button_center = pyautogui.center(one_more_location)
    pyautogui.click(one_more_button_center)
    print("Clicked 1more")

def click_prompt_option():
    prompt_option_location = None
    while not prompt_option_location:
        prompt_option_location = pyautogui.locateOnScreen('images/prompt_option.png', confidence=0.8)
        if not prompt_option_location:
            print("Prompt option image not found! Retrying in .5 seconds...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    prompt_option_location_center = pyautogui.center(prompt_option_location)
    x, y = prompt_option_location_center
    pyautogui.click(x, y + 33)
    time.sleep(0.5)  # Sleep for a short period to allow the click action to be recognized

# Function to move the image to the processed folder
def move_first_image_to_processed_folder():
    still_images_folder = "C:\\Users\\autotube\\Documents\\Shravana\\still images"
    processed_images_folder = "C:\\Users\\autotube\\Documents\\Shravana\\processed images"
    
    # List all files in the still images folder
    files = [f for f in os.listdir(still_images_folder) if os.path.isfile(os.path.join(still_images_folder, f))]
    
    # Sort files based on their last modification time, starting with the newest
    files.sort(key=lambda x: os.path.getmtime(os.path.join(still_images_folder, x)), reverse=True)

    # Check if there are any files to process
    if files:
        first_image = files[0]
        source_path = os.path.join(still_images_folder, first_image)
        destination_path = os.path.join(processed_images_folder, first_image)
        
        # Move the first image to the processed images folder
        shutil.move(source_path, destination_path)
        print(f"Moved {first_image} to the processed images folder.")
    else:
        print("No images found to process. Maybe next time.")


# Main animation loop
def animation_phase(item_count, tkinter_manager, first_upload):
    global animated_counter
    print("Entering animation_phase")  # Debugging print statement
    print(f"Checking conditions: keyboard.is_pressed('f1')={keyboard.is_pressed('f1')}, animated_counter={animated_counter}, item_count={item_count}")  # Debugging print statement
    goto_url()
    animation_queue = queue.Queue()

    animation_window_thread = threading.Thread(target=tkinter_manager.create_animation_window, args=(animation_queue,))
    #Decrease first upload after the first loop so it does not keep setting the image path.
    while not keyboard.is_pressed('f1') and animated_counter < item_count:
        print("In animation loop")  # Debugging print statement
        click_message_box()
        time.sleep(2)
        # Increment the counter and put it in the queue
        animated_counter += 1
        animation_queue.put(animated_counter)

        # Start the Tkinter window thread if this is the first image
        if animated_counter == 1:
            animation_window_thread.start()

        # Animate the image
        animate()
        time.sleep(.5)

        # Upload the image
        upload_image()

        # Call the function to make sure the universe doesn't implode or something
        click_desktop_icon(first_upload)
        if first_upload == 1:
            click_folder_icon(first_upload)
            goto_still_images_path()
            # Now set it to zero so we don't keep running that part, Morty!
            first_upload = 0
            
        select_image(first_upload)

        # Click 1more.png
        click_1more()

        # Click Prompt Option
        click_prompt_option()

        # Type the animation prompt
        type_animation_prompt()

        # Wait for half a second
        time.sleep(.5)

        # Move the image to the processed folder
        move_first_image_to_processed_folder()