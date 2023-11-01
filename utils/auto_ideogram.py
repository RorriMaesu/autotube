# Import the essential libraries for automation and timing
import pyautogui
import keyboard
import time
from PIL import Image, ImageDraw
# Import specific functions from browser_utils; keeps the browser in check
from .browser_utils import start_browser, goto_settings, click_change_button, click_nakshatra_folder, switch_download_folder_for_still_images, click_select_folder_button, new_tab, exit_tab, close_browser

# Custom images that need to be set.
# Replace this image with your profile image from ideogram. Look at mine and screenshot yours and crop to select a small uniqe set of pixels like mine.
profile_icon = 'images/me.png'

# Flags to check if it's the first run or subsequent runs; not boolean because why make life easy?
first_run = False
rest_of_runs = False

# Initialize the timer; you've got 300 seconds, make 'em count
start_time = time.time()
timeout_seconds = 300

# PyAutoGUI settings; don't touch unless you know what you're doing
pyautogui.PAUSE = .72  # pause between actions; tailor to your machine's speed
pyautogui.FAILSAFE = True  # fail-safe feature; moves the mouse to corner to abort

# Searches for and clicks an 'Ignore' button within 3 seconds.
# Update the image path 'images/ignore_image.png' if you're using a different screenshot.
def click_ignore():
    print("Searching for the ignore button...")
    start_time = time.time()  # Record the start time; you've got 3 seconds, buddy!
    timeout = 3  # The clock is ticking; 3 seconds before it gives up
    
    # Look for that elusive ignore button until time runs out
    while time.time() - start_time < timeout:
        ignore_button_visible = pyautogui.locateOnScreen('images/ignore_image.png', confidence=.9)
        
        # Found it? Great! Click it and end this madness.
        if ignore_button_visible:
            ignore_button_center = pyautogui.center(ignore_button_visible)
            print("Ignore button found! Clicking the ignore button.")
            pyautogui.click(ignore_button_center)
            return True  # Mission accomplished, return True
        
        # Can't find it? What a surprise! Let's try again in a second.
        else:
            print("Ignore button not visible, double checking and retrying in 1 second...")
            time.sleep(1)
    
    # If you're here, you've failed, and the function times out.
    if time.time() - start_time >= timeout:
        print("Timeout reached: Could not locate ignore button on screen within 3 seconds.")
        return False  # You get a False, as in "you've failed to find it."


# Navigates to the Ideogram website.
# If you're using a different URL, make sure to update it, genius.
def goto_ideogram_url():
    print("Going to the ideogram url...")
    # The URL you want to navigate to; update it if it's different
    ideogram_url = "https://ideogram.ai/?fbclid=IwAR3hZgtapT-Utwy9QUbeAQ6eRLCPjA7aAFeIAbAEx_DerN8_wHQfpKTvxQo"
    pyautogui.write(ideogram_url)  # Types out the URL
    pyautogui.press('enter')  # Hits the Enter key to go to the website


# Locates and clicks the 16x10 aspect ratio button.
# If you're using a different screenshot, you're gonna want to update the path 'images/sixteenX10_image.png'.
def click_16X10_button():
    print("Searching for the aspect ratio button...")
    # Infinite loop because we're living on the edge, baby!
    while True:
        # Look for the 16x10 aspect ratio button image with a 90% confidence level
        sixteenX10_image = pyautogui.locateOnScreen('images/sixteenX10_image.png', confidence=.9)
        
        # Found it? Sweet, let's click it.
        if sixteenX10_image:
            pyautogui.click(sixteenX10_image)
            print("Aspect ratio button found! Clicking.")
            break  # Get out of this never-ending loop
        
        # Didn't find it? Ah, the eternal struggle. Wait a second and try again.
        else:
            print("Aspect ratio button not found! Retrying in 1 second...")
            time.sleep(1)  # Chill out for a second to not overload your potato PC

                
# Clicks on a text box, assuming you've got an image of it.
# Update 'images/see_image.png' to your own screenshot of the text box if it's different.
def click_text_box():
    print("Trying to click the text box...")
    start_time = time.time()  # Start the clock, time's a-wasting
    
    timeout = 10  # You've got 10 seconds to find this thing, or it's game over

    # Start looking for that elusive text box
    while time.time() - start_time < timeout:
        # Try finding the text box image with 90% confidence
        see_image = pyautogui.locateOnScreen('images/see_image.png', confidence=.9)
        
        # Found it? Great, click it and get out
        if see_image:
            pyautogui.click(see_image)
            print("Text box clicked!")
            break  # We're done here, roll credits

        # Didn't find it? You've got to be kidding me. Wait a second and try again.
        else:
            print("From within click_text_box(): images/see_image.png not found, Retrying in 1 second...")
            time.sleep(1)  # Give the CPU a little breather

    # If you're here, you either clicked the text box or you're a failure. Check which one.
    if time.time() - start_time >= timeout:
        print("Timeout reached: images/see_image.png was not found within 10 seconds.")


# Searches for a 'Generation Completed' image. Replace 'images/gen_completed.png' with your own screenshot.
def search_for_generation_completed():
    start_time = time.time()  # Clock's ticking, buddy
    
    timeout = 300  # You've got a luxurious 5 minutes to find this. No pressure.
    
    # Loop until you find that 'Generation Completed' image or you run out of time
    while time.time() - start_time < timeout:
        # Try finding the image on screen with 90% confidence
        generation_completed = pyautogui.locateOnScreen('images/gen_completed.png', confidence=.9)
        
        # Found it? Good job, Sherlock. Now move the mouse and get outta here.
        if generation_completed:
            print("Generation Completed image found, moving mouse to the right of the ideogram logo by 484 pixels, and then clicking the text box.")
            move_mouse_to_ideogram_logo()
            return True  # You did it. Take a bow or something.

        # Didn't find it? Boo! Try again in a second.
        else:
            print("Could not locate generation completed, retrying in 1 second...")
            time.sleep(1)  # Let the CPU contemplate its existence for a sec
    
    # If you got here, you failed to find it within the time limit. So much for that.
    if time.time() - start_time >= timeout:
        print("Timeout reached: Could not locate generation completed on screen within 300 seconds.")
        return False  # You get a big fat F for failure.


# Looks for the 'Generation Complete' image and returns its location. Replace 'images/gen_completed.png' with your specific image.
def gen_completed_location():
    start_time = time.time()  # Start the stopwatch, no time to waste
    
    # Go on a never-ending loop to find this elusive image
    while True:
        print("Searching for Generation Complete image...")
        
        # Try to find the image with a confidence level of 0.7. Yeah, I said it, 0.7. Live a little.
        gen_completed_location = pyautogui.locateOnScreen('images/gen_completed.png', confidence=0.7)
        
        # If you found it, great. Let's not make a big deal out of it.
        if gen_completed_location:
            print("Generation Complete Image found at location:", gen_completed_location)
            return gen_completed_location  # Congrats, you win... nothing.
        
        # If 300 seconds have passed and you still can't find it, maybe it's just not that into you.
        elif time.time() - start_time > 300:
            print("Timeout: Image not found within 300 seconds")
            return None  # Return None, like the void of your failure.
        
        # Give the CPU a second to catch its breath. It's hard work being this useless.
        time.sleep(1)


def gen_button_click():
    start_time = time.time()
    busy_timeout = 60  # Set a timeout for busy image loop
    screenshot_count = 0  # Counter for screenshot files
    
    while True:
        busy_start_time = time.time()  # Reset the busy image timer
        
        # Check for the busy image first
        print("Searching for busy_image.png...")
        busy_image = pyautogui.locateOnScreen('images/busy_image.png', confidence=0.7)
        
        # If the busy image is found, print its location and wait for 3 seconds
        while busy_image:
            print(f"Busy image found at: ({busy_image.left}, {busy_image.top})")
            print("System is busy, waiting for 3 seconds...")
            
            # Take a screenshot
            screenshot = pyautogui.screenshot()
            
            # Draw a red circle around the busy image
            draw = ImageDraw.Draw(screenshot)
            top_left = (busy_image.left, busy_image.top)
            bottom_right = (busy_image.left + busy_image.width, busy_image.top + busy_image.height)
            draw.ellipse([top_left, bottom_right], outline="red", width=3)
            
            # Save the screenshot
            screenshot_count += 1
            screenshot.save(f"screenshot_{screenshot_count}.png")
            
            # Inner Timeout condition for busy image
            if time.time() - busy_start_time > busy_timeout:
                print(f"Busy image still present after {busy_timeout} seconds. Breaking out.")
                break
                
            time.sleep(3)
            busy_image = pyautogui.locateOnScreen('images/busy_image.png', confidence=0.9)
        
        # After the busy image is gone, check for the generate button
        print("Searching for gen_button_click.png...")
        generate_button = pyautogui.locateOnScreen('images/gen_button_click.png', confidence=0.9)
        
        # If the generate button is found, click it
        if generate_button:
            print("Generate button found at:", generate_button)
            generate_button_center = pyautogui.center(generate_button)
            pyautogui.click(generate_button_center)
            break
        
        # Outer Timeout condition
        elif time.time() - start_time > 300:
            print("Timeout: Generate button not found within 300 seconds")
            return None
        
        time.sleep(1)

# Looks for the profile image and clicks it. Simple, right? But you'd be amazed how often it screws up.
def click_profile_image():
    timeout = 30  # You've got 30 seconds. It's like a microwaveable dinner for your code.
    start_time = time.time()  # Start the timer, let the games begin.
    
    # Loop until the sands of time run out.
    while time.time() - start_time < timeout:
        # Look for the 'me.png' image on the screen. Good luck.
        me_location = pyautogui.locateOnScreen(profile_icon, confidence=0.9)
        
        # Found it? Great, you win nothing. Click it.
        if me_location:
            print("Profile image found. Clicking it.")
            center_me = pyautogui.center(me_location)
            pyautogui.click(center_me)
            print("Clicked profile image!")
            return True  # Yay, you did a thing.
        
        # If not, back to square one.
        else:
            print("Profile image not found. Retrying...")
            time.sleep(1)  # Take a one-second nap, you've earned it.
    
    # If you're still here, you've failed.
    print("Timeout reached. Profile image not found.")
    return False  # Game over, man.


# Scrolls down like a maniac for 10 seconds. Why? Because it can.
def scroll():
    end_time = time.time() + 10  # 10 seconds from now. Yeah, I can add.
    
    # Keep scrolling until you hit that 10-second mark.
    while time.time() < end_time:
        pyautogui.scroll(-10)  # Scrolls down. Why negative? Ask PyAutoGUI, not me.
        time.sleep(0.05)  # Takes a tiny 0.05-second nap between scrolls. Adorable.


# Scrolls down even harder this time, for an extra second, like it's trying to prove a point.
def scroll_again():
    end_time = time.time() + 11  # 11 seconds now. Yeah, one whole extra second. Big whoop.
    
    # Keep scrolling until you hit that 11-second mark.
    while time.time() < end_time:
        pyautogui.scroll(-22)  # Scrolls down 22 units. Because 10 wasn't cutting it, apparently.
        time.sleep(0.05)  # Still napping for 0.05 seconds between scrolls. Even rebels need their beauty sleep.


# Moves the mouse to some arbitrary coordinates like it's going on a treasure hunt or something.
def move_mouse_to_first_image():
    pyautogui.moveTo(432, 864)  # Moves to x=432, y=864. No, these aren't secret coordinates to a hidden vault.
    # time.sleep(2)  # Pauses for 2 seconds. Maybe it's admiring the view? Or it's just lazy.


# Mimics a bored office worker selecting all the text in a document. Ctrl+A, baby!
def select_all():
    print("Selecting all text...")  # Because who wouldn't want to be alerted of this thrilling action?
    keyboard.press_and_release('ctrl+a')  # Simulates pressing 'Ctrl + A' keys to select all text, as if you're about to do something important.


# This function takes the excitement of pressing the 'Delete' key to a whole new level.
def delete_old_prompt():
    print("Deleting old prompt...")  # Get ready for the thrill of erasing text!
    pyautogui.press('del')  # Simulates the pressing of the 'Delete' key, wiping out whatever was in that text box. Who needs history anyway?


# This function takes you on a thrilling journey to find and click the visual search element.
def move_mouse_to_visual_search_element():
    global first_run, rest_of_runs  # We're going global, Morty!
    start_time = time.time()  # Record the start time
    timeout = 30  # Set a timeout of 30 seconds (adjust as needed)
    time.sleep(1)  # Give it a moment to breathe
    
    while time.time() - start_time < timeout:  # Keep searching until the timeout is reached
        verified_image_location = pyautogui.locateOnScreen('images/verify_image.png', confidence=0.5)
        if verified_image_location:  # Huzzah! The image is found
            print("Verify image found. Clicking it.")
            
            x, y = pyautogui.center(verified_image_location)
            pyautogui.moveTo(x - 45, y)  # Move a little to the left (because why not?)
            pyautogui.click()  # Click it like it's hot
            return True  # Success! We found and clicked it!
        else:
            print("Verify image not found. Initiating scrolling protocol...")
            
            if first_run:
                x, y = pyautogui.position()
                pyautogui.moveTo(x - 45, y)  # A slight move to the left (just for fun)
                pyautogui.scroll(-180)  # Scroll down like you're scrolling through ancient scrolls
                first_run = False  # No more first run, Morty!
                rest_of_runs = False
                
            if rest_of_runs:
                print("Rest of runs was True. Continuing the scroll journey.")
                pyautogui.scroll(-180)  # Keep on scrolling

            else:
                pyautogui.scroll(-18)  # Regular scrolling, nothing fancy
            
            move_mouse_back_and_forth()  # A little back and forth to keep things interesting
            time.sleep(0.1)  # A tiny pause to catch our breath

    print("Timeout reached. Verify image not found.")
    return False  # We gave it our best shot, Morty!

# This function makes the mouse move back and forth, like a jittery, caffeinated Morty!
def move_mouse_back_and_forth():
    # Get the current mouse position, Morty!
    x, y = pyautogui.position()

    # Move the mouse 3 pixels to the left, like it's dodging a laser beam or something
    pyautogui.moveTo(x - 3, y)

    # Move it back to the original position, Morty. Back to square one!
    pyautogui.moveTo(x, y)

def show_some_love():
    timeout = 30  # Set timeout to 30 seconds
    start_time = time.time()  # Record start time
    
    while time.time() - start_time < timeout:  # Continue looping until timeout is reached
        heart_image_location = pyautogui.locateOnScreen('images/heart_image.png', confidence=0.9)
        
        if heart_image_location:  # Image is found
            print("Heart image found. Clicking it to show some love to the A.I...")
            heart_center = pyautogui.center(heart_image_location)
            pyautogui.click(heart_center)
            return True  # Return True to indicate success

        already_loved = pyautogui.locateOnScreen('images/already_loved_image.png', confidence=0.9)
        
        if already_loved:    # Image is found
            print("This image already has enough love for now...")
            return True

        else:
            print("Heart image not found. Retrying...")
            time.sleep(1)  # Sleep for a short duration before retrying

    print("Timeout reached. Heart image not found.")
    return False  # Return False to indicate failure

def click_the_X():
    timeout = 3  # Set timeout to 3 seconds (adjust as needed)
    start_time = time.time()  # Record start time
    
    # Define the region to search
    left = 825  # x-coordinate of the top-left corner of the region
    top = 112   # y-coordinate of the top-left corner of the region
    width = 1043  # width of the region
    height = 167  # height of the region
    region_to_search = (left, top, width, height)
    
    while time.time() - start_time < timeout:  # Continue looping until timeout is reached
        x_image_location = pyautogui.locateOnScreen('images/x_image.png', confidence=0.9, region=region_to_search)
        
        if x_image_location:  # Image is found
            print("X image found. Clicking it to exit out of the preview screen.")
            x_center = pyautogui.center(x_image_location)
            pyautogui.click(x_center)
            return True  # Return True to indicate success
        else:
            print("X image not found. Retrying...")
            time.sleep(1)  # Sleep for a short duration before retrying

    print("Timeout reached. X image not found.")
    return False  # Return False to indicate failure


def search_and_click_download():
    timeout = 300  # Set timeout to 300 seconds
    start_time = time.time()  # Record start time

    while time.time() - start_time < timeout:  # Continue looping until timeout is reached
        print("Searching for ideogram_download.png...")
        download_location = pyautogui.locateOnScreen('images/ideogram_download.png', confidence=0.8)
        
        if download_location:  # Image is found
            print("ideogram_download.png found. Clicking...")
            center_download = pyautogui.center(download_location)
            pyautogui.click(center_download)
            return True  # Return True to indicate success
        else:
            print("ideogram_download.png not found. Retrying...")
            time.sleep(1)  # Sleep for a short duration before retrying

    print("Timeout reached. ideogram_download.png not found.")
    return False  # Return False to indicate failure


def escape():
    print("Pressing the escape key...")
    time.sleep(1)
    pyautogui.press('esc')

def move_mouse_to_ideogram_logo():
    print("Trying to move the mouse to the Ideogram logo")
    start_time = time.time()  # Record the start time
    timeout = 10  # Set your timeout value in seconds
    # Keep trying to find the image until the timeout is reached
    while time.time() - start_time < timeout:
        ideogram_logo = pyautogui.locateOnScreen('images/ideogram_logo_image.png', confidence=0.9)
        if ideogram_logo:
            print("Ideogram logo found!")
            # Get the center of the found image
            x, y = pyautogui.center(ideogram_logo)
            
            # Move to the right of the image center by 484 pixels
            print("Moving mouse to the right of the logo by 484 pixels...")
            pyautogui.moveTo(x + 484, y)
            
            # Click the left mouse button once
            print("Trying to click the text box...")
            pyautogui.click()
            print("Moved mouse to the right of the logo, text box clicked!")
            return True  # Return True to indicate success
        else:
            print("ideogram_logo not found, Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    # Check if loop exited due to timeout
    if time.time() - start_time >= timeout:
        print("Timeout reached: ideogram_logo was not found within 10 seconds.")
        return False  # Return False to indicate failure


def click_lucky_style():
    timeout = 30  # Set timeout to 30 seconds
    start_time = time.time()  # Record start time
    while time.time() - start_time < timeout:  # Continue looping until timeout is reached
        lucky_location = pyautogui.locateOnScreen('images/lucky.png', confidence=0.8)
        if lucky_location:  # Image is found
            print("lucky.png found. Clicking lucky style prompt.")
            center_lucky_button = pyautogui.center(lucky_location)
            pyautogui.click(center_lucky_button)
            print("Clicked the lucky style prompt button!")
            return True  # Return True to indicate success
        else:
            print("lucky.png not found. Retrying...")
            time.sleep(1)  # Sleep for a short duration before retrying

    print("Timeout reached. lucky.png not found.")
    return False  # Return False to indicate failure


def waiting_location():
    waiting_screenshot_count = 0  # Counter for waiting screenshot files

    # Set a reasonable timeout for waiting.png search, adjust as needed
    timeout_for_waiting = 1
    # Record start time for waiting.png search
    waiting_start_time = time.time()
    
    while time.time() - waiting_start_time < timeout_for_waiting:
        # Search for the 'waiting.png' image with confidence level 0.8
        waiting_location = pyautogui.locateOnScreen('waiting.png', confidence=0.8)
        
        if waiting_location:
            # 'waiting.png' is found
            print("waiting.png found. Now searching for gen_button_click.png...")
            
            # Take a screenshot
            waiting_screenshot = pyautogui.screenshot()
            
            # Draw a red circle around the waiting image
            draw = ImageDraw.Draw(waiting_screenshot)
            top_left = (waiting_location.left, waiting_location.top)
            bottom_right = (waiting_location.left + waiting_location.width, waiting_location.top + waiting_location.height)
            draw.ellipse([top_left, bottom_right], outline="red", width=3)
            
            # Save the screenshot
            waiting_screenshot_count += 1
            waiting_screenshot.save(f"waiting_screenshot_{waiting_screenshot_count}.png")
            
            # Set timeout for gen_button_click.png search
            timeout_for_gen_button = 300
            # Record start time for gen_button_click.png search
            gen_button_start_time = time.time()
            
            while time.time() - gen_button_start_time < timeout_for_gen_button:
                # Search for the 'gen_button_click.png' image with confidence level 0.7
                generate_button = pyautogui.locateOnScreen('images/gen_button_click.png', confidence=0.7)
                if generate_button:
                    # 'gen_button_click.png' is found
                    print("gen_button_click.png found. Calling gen_button_click function...")
                    # Call your gen_button_click function
                    gen_button_click()
                    return True  # Return True to indicate success
                
                print("gen_button_click.png not found. Retrying...")
                time.sleep(1)  # Sleep for a short duration before retrying
            
            print("Timeout reached for gen_button_click.png search.")
            return False  # Return False to indicate failure

        print("waiting.png not found. Retrying...")
        time.sleep(1)  # Sleep for a short duration before retrying

    print("Timeout reached for waiting.png search. Proceeding with the rest of the script...")
    # Call the gen_button_click function (assuming it's defined elsewhere)
    gen_button_click()



def first_prompt():
    # Read prompts from file and split them into a list
    with open('utils/prompts.txt', 'r') as file:
        prompts = file.read().split(',')

    # Process only the first prompt if it exists
    if prompts:
        first_prompt = prompts[0]
        print(f"Processing first prompt: {first_prompt}")
        
        # Add a small delay before typing the prompt
        time.sleep(0.5)
        
        # Type the first prompt
        pyautogui.write(first_prompt)
        
        # Add a delay after typing the prompt (adjust as needed)
        time.sleep(1)


def next_prompt(prompts, current_index):
    """
    Get the next prompt from the list of prompts.

    Args:
    prompts (list): A list of prompts.
    current_index (int): The current index of the prompt to retrieve.

    Returns:
    str or None: The next prompt if available, or None if all prompts are exhausted.
    """
    if current_index >= len(prompts):
        print("All prompts are exhausted, Morty. Time to chill.")
        return None  # No more prompts

    # Print and return the next prompt
    print(f"Fetching the next mind-blowing prompt: {prompts[current_index]}")
    return prompts[current_index]


def rest_of_prompts():
    current_index = 1  # Starting from the second prompt because you've already used the first one, Morty!
    while True:
        print("Attempting to write the next prompt...")

        # Read prompts from file and split them into a list
        with open('utils/prompts.txt', 'r') as file:
            prompts = file.read().split(',')

        # Get the next prompt
        prompt = next_prompt(prompts, current_index)
        
        if prompt is None:
            print("That's it, Morty! We're outta prompts!")
            break

        print(f"Processing prompt: {prompt}")

        # The following steps simulate the interaction with the ideogram AI
        move_mouse_to_ideogram_logo()  # Move mouse to ideogram logo
        select_all()  # Select all text in the text box
        time.sleep(0.5)
        delete_old_prompt()  # Delete the old prompt text
        time.sleep(0.5)
        pyautogui.write(prompt)  # Write the new prompt
        click_lucky_style()  # Click the lucky style prompt button
        gen_button_click()  # Click the generate button
        click_profile_image()  # Click the profile image
        move_mouse_to_first_image()  # Move mouse to the first image
        move_mouse_to_visual_search_element()  # Move mouse to the visual search element
        show_some_love()  # Show some love by clicking the heart
        search_and_click_download()  # Search and click the download button
        time.sleep(1)  # Sleep for a second
        escape()  # Press the escape key
        click_the_X()  # Click the X to exit the preview

        current_index += 1  # Move on to the next prompt, Morty!



def download_remaining_images_1():
    # Click the profile image
    click_profile_image()

    # Move the mouse down under the profile image
    move_mouse_down_under_profile_image()

    # Move the mouse to the visual search element
    move_mouse_to_visual_search_element()

    # Show some love by clicking the heart
    show_some_love()

    # Search and click the download button
    search_and_click_download()

    # Click the back arrow to go back
    click_back_arrow()



def download_remaining_images_2():
    # Click the profile image
    click_profile_image()

    # Move the mouse down under the profile image
    move_mouse_down_under_profile_image()

    # Move the mouse left by 330 pixels
    move_mouse_left_330_pixels()

    # Move the mouse to the visual search element
    move_mouse_to_visual_search_element()

    # Show some love by clicking the heart
    show_some_love()

    # Search and click the download button
    search_and_click_download()

    # Click the back arrow to go back
    click_back_arrow()


def download_remaining_images_3():
    # Click the profile image
    click_profile_image()

    # Move the mouse down under the profile image
    move_mouse_down_under_profile_image()

    # Move the mouse left by 330 pixels
    move_mouse_left_330_pixels()

    # Move the mouse left by 300 more pixels
    move_mouse_left_300_pixels()

    # Move the mouse to the visual search element
    move_mouse_to_visual_search_element()

    # Show some love by clicking the heart
    show_some_love()

    # Search and click the download button
    search_and_click_download()

    # Click the back arrow to go back
    click_back_arrow()


def download_remaining_images_4():
    # Click the profile image
    click_profile_image()

    # Move the mouse down under the profile image
    move_mouse_down_under_profile_image()

    # Move the mouse left by 330 pixels
    move_mouse_left_330_pixels()

    # Move the mouse left by 300 pixels
    move_mouse_left_300_pixels()

    # Move the mouse left by another 300 pixels
    move_mouse_left_300_pixels()

    # Move the mouse to the visual search element
    move_mouse_to_visual_search_element()

    # Show some love by clicking the heart
    show_some_love()

    # Search and click the download button
    search_and_click_download()

    # Click the back arrow to go back
    click_back_arrow()



def download_all_4_remaining_images():
    global rest_of_runs, first_run

    # Set the initial state for the 'first_run' and 'rest_of_runs' variables
    first_run = True

    # Download the first image
    download_remaining_images_1()

    # Set 'rest_of_runs' to True to enable additional scrolling
    rest_of_runs = True

    # Download the second image
    download_remaining_images_2()

    # Download the third image
    download_remaining_images_3()

    # Download the fourth image
    download_remaining_images_4()



def move_mouse_left_330_pixels():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Move the mouse left by 330 pixels on the x-axis
    pyautogui.moveTo(x - 330, y)



def move_mouse_left_300_pixels():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Move the mouse left by 300 pixels on the x-axis
    pyautogui.moveTo(x - 300, y)


def move_mouse_down_under_profile_image():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Move the mouse down by 108 pixels on the y-axis
    pyautogui.moveTo(x, y + 108)


def click_back_arrow():
    timeout = 30  # Set timeout to 30 seconds
    start_time = time.time()  # Record start time

    while time.time() - start_time < timeout:  # Continue looping until timeout is reached
        print("Searching for back_arrow_image.png...")
        back_arrow_location = pyautogui.locateOnScreen('images/back_arrow_image.png', confidence=0.8)
        if back_arrow_location:  # Image is found
            print("back_arrow_image.png found. Clicking...")
            center_back_arrow = pyautogui.center(back_arrow_location)
            pyautogui.click(center_back_arrow)
            return True  # Return True to indicate success
        else:
            print("back_arrow_image not found. Retrying...")
            time.sleep(1)  # Sleep for a short duration before retrying

    print("Timeout reached. back_arrow_image.png not found.")
    return False  # Return False to indicate failure


# Define the function like before, Morty!
def count_items_in_file(file_path):
    try:
        # Try to open the file at the specified path
        with open(file_path, 'r') as f:
            # Read the contents of the file
            text = f.read()
            # Split the text into items using ',' as a delimiter
            items = text.split(',')
            # Count the number of items
            num_items = len(items)
        # Print the number of items found
        print(f"Found {num_items} items, Morty! We did it!")
        # Return the number of items
        return num_items
    except FileNotFoundError:
        # Handle the case when the file is not found
        print("File's not there, Morty! It's like it entered another dimension!")
        # Return 0 to indicate that no items were found due to the missing file
        return 0


# Call the function to count items in a file and store the result in the variable item_count
item_count = count_items_in_file('utils/prompts.txt')

def auto_ideogram_script():
    global first_run, rest_of_runs
    # Beginning of script
    switch_download_folder_for_still_images()  # Switch the download folder for still images
    goto_ideogram_url()  # Go to the ideogram URL
    click_16X10_button()  # Click the 16x10 button
    click_text_box()  # Click the text box
    first_prompt()  # Input the first prompt
    click_lucky_style()  # Click the lucky style prompt
    gen_button_click()  # Click the generate button
    click_profile_image()  # Click the profile image
    move_mouse_to_first_image()  # Move the mouse to the first image
    move_mouse_to_visual_search_element()  # Move the mouse to the visual search element
    first_run = False  # Set the first_run flag to False
    rest_of_runs = True  # Set the rest_of_runs flag to True
    show_some_love()  # Show some love to the AI
    search_and_click_download()  # Search and click the download button
    escape()  # Press the escape key
    click_the_X()  # Click the X button
    rest_of_prompts()  # Continue with the rest of the prompts
    download_all_4_remaining_images()  # Download the remaining images
    close_browser()  # Close the browser
    print("All images have been generated and downloaded, preparing to switch to the video animation module...")
    time.sleep(3)  # Sleep for 1 second