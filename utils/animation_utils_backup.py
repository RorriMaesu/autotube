import pyautogui
import time
import queue
import threading
import keyboard
from .tkinter_windows import TkinterManager  # Import the TkinterManager class
from config import ANIMATION_DURATION  # Importing from config.py
from .browser_utils import click_nakshatra_folder, goto_url  # Relative import
from config import animated_counter
pyautogui.PAUSE = .72  # pause for each action

#This will need to be set to your own still images folder path
still_images_path = r'C:\Users\autotube\Documents\Dhanishta\still images'

def click_message_box():
    prompt_box_location = None
    while not prompt_box_location:
        prompt_box_location = pyautogui.locateOnScreen('images/prompt_box.png', confidence=0.8)
        if not prompt_box_location:
            print("Message box image not found! Retrying in .1 second...")
            time.sleep(.1)  # Wait for a short period before trying again to reduce CPU usage

    prompt_box_center = pyautogui.center(prompt_box_location)
    pyautogui.click(prompt_box_center)
    print("Message box clicked!")

def increment_animated_counter(animation_queue):
    global animated_counter
    animated_counter += 1
    animation_queue.put(animated_counter)

def animate():
    pyautogui.write('/animate')
    time.sleep(1)
    pyautogui.press('enter')

def upload_image():
    select_image_location = None
    while not select_image_location:
        select_image_location = pyautogui.locateOnScreen('images/select_image.png', confidence=0.7)
        if not select_image_location:
            print("Select Image Button not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    select_image_location_center = pyautogui.center(select_image_location)
    pyautogui.click(select_image_location_center)
    time.sleep(.5)


def click_desktop_icon(first_upload):
    start_time = time.time()  # Get the current time, Morty
    search_region = (0, 0, 153, 73)  # This time we'll actually use it
    desktop_image_location = None
    
    while not desktop_image_location:
        current_time = time.time()
        elapsed_time = current_time - start_time  # How much time has passed, Morty?

        if first_upload == 0 or elapsed_time > 3:  # If more than 3 seconds have passed
            print("Time's up! Moving on.")
            return  # Get outta here!
        
        desktop_image_location = pyautogui.locateOnScreen('images/desktop_icon_image.png', region=search_region, confidence=0.8)
        
        if not desktop_image_location:
            print("Desktop Icon not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    desktop_image_location_center = pyautogui.center(desktop_image_location)
    pyautogui.click(desktop_image_location_center)
    time.sleep(.5)

def click_folder_icon(first_upload):
    start_time = time.time()  # Get the current time, Morty
    search_region = (0, 0, 163, 67)  # This time we'll actually use it
    folder_icon_image_location = None
    
    while not folder_icon_image_location:
        current_time = time.time()
        elapsed_time = current_time - start_time  # How much time has passed, Morty?

        if first_upload == 0 or elapsed_time > 3:  # If more than 3 seconds have passed
            print("Time's up! Moving on.")
            return  # Get outta here!
        
        folder_icon_image_location = pyautogui.locateOnScreen('images/folder_icon_image.png', region=search_region, confidence=0.8)
        
        if not folder_icon_image_location:
            print("Desktop Icon not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    folder_icon_image_location_center = pyautogui.center(folder_icon_image_location)
    pyautogui.click(folder_icon_image_location_center)
    time.sleep(.5)


# Make sure to change this path to fit your pc file path. The variable to edit is at the top of this script and called still_images_path
def goto_still_images_path():
    pyautogui.write(still_images_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)


def select_image(timeout=3):
    end_time = time.time() + timeout  # Define the end time based on the provided timeout
    first_image_location = None
    search_region = (194, 118, 449, 383)
    
    while time.time() < end_time:
        first_image_location = pyautogui.locateOnScreen('images/ideogram_image.png', confidence=0.9, region = search_region)
        if first_image_location:
            break  # Exit the loop if the image is found
        print("First file in folder not found. Trying again...")
        time.sleep(0.5)  # Wait for a short period before trying again to reduce CPU usage

    if first_image_location:
        first_image_location_center = pyautogui.center(first_image_location)
        time.sleep(0.2)
        print("Clicked the first image in the folder!")
        pyautogui.doubleClick(first_image_location_center)
        time.sleep(1)
    else:
        # If the image was not found within the timeout, click on the specified coordinates
        print("Image not found after 3 seconds. Clicking default coordinates.")
        pyautogui.doubleClick(x=324, y=234)

def type_animation_prompt():
    pyautogui.write("-neg morphing, erratic fluctuation in motion, noisy, bad quality, distorted, poorly drawn, blurry, grainy, low resolution, oversaturated, lack of detail, inconsistent lighting.")
    pyautogui.press('enter')
    
def click_1more():
    one_more_location = None
    while not one_more_location:
        one_more_location = pyautogui.locateOnScreen('images/one_more.png', confidence=0.8)
        if not one_more_location:
            print("1more button image not found! Retrying in .5 seconds...")
            time.sleep(.5)  # Wait for a short period before trying again to reduce CPU usage

    one_more_button_center = pyautogui.center(one_more_location)
    time.sleep(.2)
    pyautogui.click(one_more_button_center)
    print("Clicked 1more")

def click_prompt_option():
    prompt_option_location = None
    while not prompt_option_location:
        prompt_option_location = pyautogui.locateOnScreen('images/prompt_option.png', confidence=0.8)
        if not prompt_option_location:
            print("Prompt option image not found! Retrying in .5 seconds...")
            time.sleep(.5)  # Wait for a short period before trying again to reduce CPU usage

    prompt_option_location_center = pyautogui.center(prompt_option_location)
    x, y = prompt_option_location_center
    pyautogui.click(x, y + 33)
    time.sleep(0.5)  # Sleep for a short period to allow the click action to be recognized

def move_image_to_processed_folder():
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(0.1)
    pyautogui.click(234, 162)
    pyautogui.hotkey('ctrl', 'x')
    click_nakshatra_folder()

    processed_images_folder_location = None
    while not processed_images_folder_location:
        processed_images_folder_location = pyautogui.locateOnScreen('images/processed_images.png', confidence=0.9)
        if not processed_images_folder_location:
            print("Processed Images Folder not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage
    
    processed_images_center = pyautogui.center(processed_images_folder_location)
    pyautogui.doubleClick(processed_images_center)
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('esc')
    # pyautogui.click(1859, 953)

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
        print("I clicked the 1 more image from within the main animation loop.")  # Click the prompt box to start the animation
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
        select_image()

        # Click 1more.png
        click_1more()

        # Click Prompt Option
        click_prompt_option()

        # Type the animation prompt
        type_animation_prompt()

        # Wait for half a second
        time.sleep(.5)

        # Move the image to the processed folder
        move_image_to_processed_folder()