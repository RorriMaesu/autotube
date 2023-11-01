import pyautogui
import time

# Set the pause time between each PyAutoGUI command
pyautogui.PAUSE = 1  # pause for each action

#This will need to be custom set for your setup, it is the path to the folder where you are holding everything for the project.
# Rename every occurance of "nakshatra_file_path" to subject_file_path or leave it if you like.
nakshatra_file_path = "C:\\Users\\autotube\\Documents\\shravana"

# All functions related to browser automation
def find_question_mark_icon_click_drop_down_to_the_left():
    question_mark_location = None
    while not question_mark_location:
        question_mark_location = pyautogui.locateOnScreen('images/question_mark_image.png', confidence=0.9)
        if not question_mark_location:
            print("Question Mark image not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    question_mark_location_center = pyautogui.center(question_mark_location)
    
    # Move 50 pixels to the left of the center
    click_location = (question_mark_location_center.x - 69, question_mark_location_center.y)
    
    pyautogui.click(click_location)
    print("Clicked the icon resizer dropdown.")




def start_browser():
    """
    Open the Edge browser either by locating its logo image or using the Windows key search method if not found.
    
    This function attempts to locate the Edge browser logo image on the screen. If found, it clicks on the logo to open Edge.
    If the logo image is not found after a certain number of attempts, it resorts to using the Windows key search method
    to open Edge.

    Raises:
        None

    Returns:
        None
    """
    print("starting browser!")
    edge_logo_location = None
    attempt_count = 0
    max_attempts = 5  # Set the number of attempts you want before using the alternative method

    # Try to locate the Edge logo image for a maximum number of attempts
    while not edge_logo_location and attempt_count < max_attempts:
        edge_logo_location = pyautogui.locateOnScreen('images/edge.png', confidence=0.8)
        if not edge_logo_location:
            # If the logo image is not found, print a message and wait before retrying
            print(f"Edge logo image not found! Attempt {attempt_count + 1}/{max_attempts}. Retrying in .5 seconds...")
            time.sleep(.5)  # Wait for a short period before trying again to reduce CPU usage
            attempt_count += 1

    if edge_logo_location:
        # If the Edge logo image is found, click on it to open Edge
        edge_logo_center = pyautogui.center(edge_logo_location)
        pyautogui.click(edge_logo_center)
        print("Clicked the browser icon!")
        time.sleep(3)
    else:
        # If the logo image is still not found after the maximum attempts, use an alternative method to open Edge
        print("Failed to find Edge logo image after maximum attempts. Opening Edge using Windows key.")
        pyautogui.hotkey('win')  # Press the Windows key to open the Start menu
        time.sleep(0.5)  # Optional: Adding a short delay to ensure the Start menu has time to open
        pyautogui.write('Microsoft Edge')  # Type "Microsoft Edge" into the search
        time.sleep(0.5)  # Optional: Adding a short delay to ensure the text has time to be entered
        pyautogui.press('enter')  # Press Enter to launch Edge

def goto_url():
    """
    Navigate to the specified URL in a web browser.

    This function uses PyAutoGUI to type the URL into the browser's address bar and then presses Enter to navigate to the URL.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    # URL to navigate to
    gen1_url = "https://discord.com/channels/1123665496148017235/1123665843365093487"

    # Type the URL into the browser's address bar and press Enter
    pyautogui.write(gen1_url)
    pyautogui.press('enter')

def goto_settings():
    """
    Navigate to the browser settings page.

    This function uses PyAutoGUI to type the settings URL into the browser's address bar and then presses Enter to navigate to the settings page.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    # URL for browser settings
    settings_url = "edge://settings/downloads#All"

    # Type the settings URL into the browser's address bar and press Enter
    pyautogui.write(settings_url)
    pyautogui.press('enter')
    print("Going to settings!")

def click_change_button():
    """
    Click the 'Change' button in a settings page.

    This function continuously looks for the 'Change' button image on the screen using PyAutoGUI.
    Once the button is found, it clicks on it.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    change_button_location = None

    # Continuously look for the 'Change' button image
    while not change_button_location:
        change_button_location = pyautogui.locateOnScreen('images/change_button.png', confidence=0.7)
        if not change_button_location:
            print("Change button image not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    # Click on the center of the 'Change' button once found
    change_button_center = pyautogui.center(change_button_location)
    pyautogui.click(change_button_center)
    time.sleep(1)
    print("Clicked the change button!")

def click_nakshatra_folder():
    """
    Click the 'Nakshatra' folder in a file selection dialog.

    This function continuously looks for the 'Nakshatra' folder image on the screen using PyAutoGUI.
    If the folder is not found within a certain time limit, it moves on to clicking the general folder icon
    and entering the Nakshatra folder path manually.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    nakshatra_folder_location = None
    start_time = time.time()
    
    while not nakshatra_folder_location:
        current_time = time.time()
        elapsed_time = current_time - start_time
    
        #This part will need to be custom set to a screenshot of the name of your folder. Look at the original screenshot as an example.
        nakshatra_folder_location = pyautogui.locateOnScreen('images/shravana_folder.png', confidence=0.8)
        if not nakshatra_folder_location:
            print("Shravana folder image not found! Retrying in 1 second...")

        # If a certain time limit is exceeded, move on to clicking the general folder icon and entering the path manually
        if elapsed_time > 7:
            print("Time's up! Moving on to click_folder_icon.")
            click_folder_icon()
            time.sleep(.5)
            type_nakshatra_file_path_and_enter()
            return False
        
    # Click on the center of the 'Nakshatra' folder once found
    nakshatra_center = pyautogui.center(nakshatra_folder_location)
    pyautogui.click(nakshatra_center)
    time.sleep(1)
    print("Clicked the Nakshatra folder!")


def click_left_of_the_refresh_button():
    folder_refresh_button_image_location = None
    
    while not folder_refresh_button_image_location:
        folder_refresh_button_image_location = pyautogui.locateOnScreen('images/folder_refresh_button_image.png', confidence=0.9)
        
        if not folder_refresh_button_image_location:
            print("Folder Refresh Icon not found! Retrying in 1 second...")
            time.sleep(1)

    # Find the center of the folder icon once found
    folder_refresh_button_image_location_center = pyautogui.center(folder_refresh_button_image_location)

    # Calculate the new coordinates to click 100 pixels to the left
    new_x = folder_refresh_button_image_location_center.x - 100
    new_y = folder_refresh_button_image_location_center.y

    # Now click it, you dingus
    pyautogui.click(x=new_x, y=new_y)

def click_folder_icon():
    folder_icon_image_location = None
    attempts = 0  # Initialize a counter for attempts
    
    while not folder_icon_image_location:
        folder_icon_image_location = pyautogui.locateOnScreen('images/folder_icon_image.png', confidence=0.7)
        
        if not folder_icon_image_location:
            print("Folder Icon not found! Retrying in 1 second...")
            attempts += 1  # Increment the counter
            
            if attempts >= 3:  # Check if 3 or more attempts have been made
                print("This is pointless. Clicking the refresh button instead.")
                click_left_of_the_refresh_button()
                return
            
            time.sleep(.5)  # Wait for a short period before trying again to reduce CPU usage

    # Do the clicky thing, as if you have a choice
    folder_icon_image_location_center = pyautogui.center(folder_icon_image_location)
    pyautogui.click(folder_icon_image_location_center)
    print("Clicked the Folder Icon!")

def type_nakshatra_file_path_and_enter():
    """
    Type the Nakshatra file path and press Enter in a file selection dialog.

    This function types the specified file path (nakshatra_file_path) and presses Enter in a file selection dialog using PyAutoGUI.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    pyautogui.write(nakshatra_file_path)
    pyautogui.press('enter')

def click_animated_images_folder():
    """
    Double-click the animated images folder icon.

    This function double-clicks the animated images folder icon using PyAutoGUI.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    animated_images_folder_location = None
    while not animated_images_folder_location:
        animated_images_folder_location = pyautogui.locateOnScreen('images/animated_images_folder.png', confidence=0.9)
        if not animated_images_folder_location:
            print("Animated images folder image not found! Retrying in 1 second...")
            time.sleep(.5)  # Wait for a short period before trying again to reduce CPU usage
    animated_images_folder_location_center = pyautogui.center(animated_images_folder_location)
    pyautogui.doubleClick(animated_images_folder_location_center)

def click_select_folder_button():
    """
    Click the select folder button.

    This function clicks the select folder button using PyAutoGUI.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    select_folder_button_location = None
    while not select_folder_button_location:
        select_folder_button_location = pyautogui.locateOnScreen('images/select_folder_button.png', confidence=0.8)
        if not select_folder_button_location:
            print("Select Folder Button image not found! Retrying in 1 second...")
            time.sleep(.5)  # Wait for a short period before trying again to reduce CPU usage

    select_folder_button_location_center = pyautogui.center(select_folder_button_location)
    pyautogui.click(select_folder_button_location_center)
    print("Clicked the Select Folder button!")

def new_tab():
    """
    Open a new tab in the web browser.

    This function presses the Ctrl+T hotkey combination to open a new tab in the web browser.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    pyautogui.hotkey('ctrl', 't')

def exit_tab():
    """
    Close the current tab in the web browser.

    This function looks for the settings icon on the screen and clicks it to close the current tab in the web browser.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    settings_button_location = None
    while not settings_button_location:
        settings_button_location = pyautogui.locateOnScreen('images/settings.png', confidence=0.9)
        if not settings_button_location:
            print("Settings icon not found on screen! Retrying in 1 second...")
            time.sleep(.5)  # Wait for a short period before trying again to reduce CPU usage

    settings_button_center = pyautogui.center(settings_button_location)
    eks, why = settings_button_center
    pyautogui.click(eks + 204, why)

# Define a function to close the browser
def close_browser():
    max_attempts = 5
    while True:  # Loop until you click that exit button, Morty!
        for attempt in range(max_attempts):
            edge_exit_image_location = pyautogui.locateOnScreen('images/edge_exit_image.png', confidence=0.8)
            if edge_exit_image_location:
                print("edge_exit_image.png found. Clicking...")
                center_edge_exit_image = pyautogui.center(edge_exit_image_location)
                pyautogui.click(center_edge_exit_image)
                time.sleep(1)
                return True
            else:
                if attempt < max_attempts - 1:
                    print("edge_exit_image not found. Retrying...")
                    time.sleep(1)
                else:
                    print(f"edge_exit_image not found after {max_attempts} attempts. Calling start_browser()...")
                    start_browser()
                    time.sleep(1)
                    break  # Breaks the inner for-loop, but not the outer while-loop. Get it, Morty?


# Switches the default download folder in the browser to the 'still_images' folder.
# Note: Make sure the browser automation steps match your specific setup or it'll all go south.
def switch_download_folder_for_still_images():
    start_browser()  # Starts the web browser; make sure your browser is supported
    goto_settings()  # Navigates to the settings page of the browser
    click_change_button()  # Clicks the "Change" button to switch the download folder
    click_nakshatra_folder()  # Clicks the 'nakshatra' folder; must be in your directory tree
    click_still_images_folder()  # Clicks the 'still_images' folder; must be a sub-folder in 'nakshatra'
    click_select_folder_button()  # Confirms the folder change
    new_tab()  # Opens a new browser tab; not sure why you're doing this, but okay
    exit_tab()  # Closes the new tab; seriously, why?


# Locates and double-clicks the 'still_images' folder in the file explorer.
# Make sure you've got an accurate screenshot at 'images/still_images_folder.png'.


def click_still_images_folder():
    still_images_folder_location = None  # Initialize the variable to store the folder's screen location
    # Keep searching for the image until it's found
    while not still_images_folder_location:
        # Locate the folder image on screen with a 90% confidence level
        still_images_folder_location = pyautogui.locateOnScreen('images/still_images_folder.png', confidence=0.9)
        # If the image isn't found, wait a second and try again
        if not still_images_folder_location:
            print("still images folder image not found! Retrying in 1 second...")
            time.sleep(1)  # Pause for a bit to not hammer the CPU

    # Once the folder is located, find its center
    still_images_folder_location_center = pyautogui.center(still_images_folder_location)
    # Double-click the center of the folder to open it
    pyautogui.doubleClick(still_images_folder_location_center)


def click_extra_large_icon_button():
    extra_large_icon_button_location = None
    while not extra_large_icon_button_location:
        extra_large_icon_button_location = pyautogui.locateOnScreen('images/extra_large_icons_button_image.png', confidence=0.9) 
        if not extra_large_icon_button_location:
            print("Extra large icons button image image not found! Retrying in 1 second...")
            time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

    extra_large_icon_button_location_center = pyautogui.center(extra_large_icon_button_location)
    pyautogui.click(extra_large_icon_button_location_center)
    print("Clicked extra large icon button!")

def switch_download_folders():
    """
    Switch the download folder to a specific location.

    This function opens a web browser, navigates to the browser settings, and changes the download folder location
    to a specific directory.

    Parameters:
        None

    Raises:
        None

    Returns:
        None
    """
    print("Switching download folders for animated images...")
    start_browser()
    goto_settings()
    click_change_button()
    click_nakshatra_folder()
    click_animated_images_folder()
    click_select_folder_button()
    new_tab()
    exit_tab()