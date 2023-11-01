import pyautogui
import time
from .browser_utils import (
    start_browser,
    goto_settings,
    click_change_button,
    click_nakshatra_folder,
    click_folder_icon,
    click_select_folder_button,
    new_tab,
    exit_tab,
    click_animated_images_folder,
    click_nakshatra_folder,
    find_question_mark_icon_click_drop_down_to_the_left,
    click_extra_large_icon_button,
)

# Replace these with the actual paths to your icon images, these below are in the images folder. 
video_editor_icon = 'images/movavi_video_editor_icon_image.png'  # Path to the video editor icon image
exit_icon = 'images/movavi_exit_icon_image.png'  # Path to the exit icon image
open_image = 'images/movavi_open_image.png'  # Path to the open image icon
wait_image = 'images/wait_image.png'  # Path to the wait image icon
loading_image = 'images/loading_image.png'  # Path to the loading image icon
video_icon = 'images/video_icon_image.png'  # Path to the video icon image
video_track_icon = 'images/video_track_plus_icon_image.png'  # Path to the video track icon image
movavi_change_button = 'images/movavi_change_button_image.png'  # Path to the Movavi change button image
audio_folder = 'images/audio_folder_image.png'  # Path to the audio folder image
music_icon = 'images/music_icon_image.png'  # Path to the music icon image
audio_track_icon = 'images/speaker_track_icon_image.png'  # Path to the audio track icon image
save_image = 'images/save_image.png'  # Path to the save image icon
add_files_image = 'images/add_files_image.png'  # Path to the add files image icon
file_image = 'images/file_image.png'  # Path to the file image icon
ctrl_s_image = 'images/ctrl_s_image.png'  # Path to the ctrl+s image icon  
more_tools_icon = 'images/more_tools_icon_image.png'  # Path to the more tools icon image
video_editing_button = 'images/video_editing_button_image.png'  # Path to the video editing button image
logo_text = 'images/logo_text_image.png'  # Path to the logo text image
add_logo_button = 'images/add_logo_button_image.png'  # Path to the add logo button image
corner_dot = '/images/corner_dot_image.png'  # Path to the corner dot image
file_name_text_box = 'images/file_name_image.png'  # Path to the file name text box image

# Path to the file directory. Set this to the path of your subject folder, the default is shravana, but you will still need to ch
# This needs to be the subject folder, replace all occurances of "shravana" with your subject name, and then take a small screen shot similar to the file "shravana_folder.png" for it to search for and rename it to your subject. To do this quickly in visual studio, simply press 'ctrl+H', this will bring up a search window, in the top box type shravana, in the bottom field type the name of your subject folder. This will replace every use of shravana in the code with your ubject. Just remember to update the image too!
nakshatra_file_path = "C:\\Users\\autotube\\Documents\\shravana"  

#This will need to be custom set to the path of YOUR LOGO FILE
logo_path = "C:\\Users\\autotube\\Documents\\shravana\\channel_logo\\channel_logo.png"

# Path to the logo movement handle image, this needs to be a small screenshot of the center of your logo.
logo_movement_handle = 'images/logo_move_image.png' 

# Path to the channel logo icon image, this needs to be another screenshot of your logo from the folder it will be found in, you can try to reuse the same image as before, but it may not work. Essentially a small screenshot of the center few pixels for it to doubleclick.
channel_logo_icon = 'images/channel_logo_icon_image.png'

#This will need to be custom set to the path of YOUR MOVAVI VIDEO PROJECTS FOLDER
movavi_project_path = 'C:\\Users\\autotube\\Videos\\Movavi Video Editor\\Projects'

# Set a pause duration for each action performed by pyautogui
pyautogui.PAUSE = .72  # Pause for each action

# This section imports necessary modules and sets a pause duration for pyautogui.

# pyautogui.PAUSE is set to 0.72 seconds, which means there will be a 0.72-second pause
# between each action performed by pyautogui. This pause can help ensure that the
# automation script doesn't execute actions too quickly, allowing time for the
# computer to respond to each action.

# The imported functions are from a module named "browser_utils," which is used
# to interact with a web browser and perform various actions within it. These actions
# include starting the browser, navigating to settings, clicking buttons, and more.

def start_video_editor(icon_image):
    """
    Start the video editor by locating its shortcut.

    Args:
        icon_image (str): The filename of the image containing the video editor shortcut icon.

    Returns:
        None
    """
    while True:
        location = pyautogui.locateOnScreen(icon_image, confidence=0.9)
        if location:
            # Click on the center of the located icon to start the video editor
            pyautogui.click(pyautogui.center(location))
            print("Video editor started, Morty!")
            break
        else:
            print("Still looking for the video editor icon, give it a sec...")
            time.sleep(1)


def exit_popup(exit_icon_image):
    """
    Exit any annoying pop-ups that show up.

    Args:
        exit_icon_image (str): The filename of the image containing the exit icon for the pop-up.

    Returns:
        None
    """
    while True:
        location = pyautogui.locateOnScreen(exit_icon_image, confidence=0.9)
        if location:
            # Click on the center of the located exit icon to close the pop-up
            pyautogui.click(pyautogui.center(location))
            print("Exited the pop-up like a boss.")
            break
        else:
            print("Where's that exit icon? Gah! Wait up...")
            time.sleep(6)

def create_new_project():
    """
    Create a new project.

    Returns:
        None
    """
    pyautogui.hotkey('ctrl+N')
    print("New project, new possibilities, eh Morty?")



def initial_add_files(add_files_image):
    """
    Click the 'Add Files' button to start adding files to the project.

    Args:
        add_files_image (str): The path to the image of the 'Add Files' button.

    Returns:
        None
    """
    while True:
        add_files_image_location = pyautogui.locateOnScreen(add_files_image, confidence=0.9)
        if add_files_image_location:
            pyautogui.click(pyautogui.center(add_files_image_location))
            print("HER WE GOOOOOOOOOOO!")
            break
        else:
            print("Where's that add files icon? Fuck!, Wait up...")
            time.sleep(0.5)

def add_media_hotkey():
    """
    Open the media folder in the video editor using a hotkey.

    Args:
        None

    Returns:
        None
    """
    print("Opening media folder, Morty!")
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(2)


def enter_file_path(nakshatra_file_path):
    """
    Enter the file path to the media in the file dialog.

    Args:
        file_path (str): The file path to be entered.

    Returns:
        None
    """
    pyautogui.write(nakshatra_file_path)
    print(f"Entered the path: {nakshatra_file_path}")


def press_enter():
    """
    Press the Enter key.

    Returns:
        None
    """
    pyautogui.press('enter')
    print("Pressed Enter, Morty. We're diving in!")


def select_all():
    """
    Select all items in the current context.

    This function simulates pressing the 'Ctrl + A' keyboard shortcut.

    Returns:
        None
    """
    # Give it 5 seconds in case the videos need to load.
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'a')
    print("Pressed ctrl+a to select all of the stuffs, Morty! This will wait for about 5 seconds to make sure the files all load, this is incase there are many.")


def click():
    """
    Perform a simple mouse click.

    This function simulates a left mouse click.

    Returns:
        None
    """
    pyautogui.click()
    print("Clicking!")

def click_open(open_image):
    """
    Click the "Open" button.

    This function searches for the specified image on the screen and clicks it.

    Args:
        open_image (str): The filename of the image to click.

    Returns:
        None
    """
    while True:
        location = pyautogui.locateOnScreen(open_image, confidence=0.9)
        if location:
            pyautogui.click(pyautogui.center(location))
            print("Clicking open!")
            break
        else:
            print("Still looking for the open button, give it a sec...")
            time.sleep(0.5)

def wait(wait_image):
    """
    Wait until a specified image disappears from the screen.

    This function continuously checks if a specified image is present on the screen.
    It waits until the image disappears before proceeding.

    Args:
        wait_image (str): The filename of the image to wait for.

    Returns:
        None
    """
    while True:
        location = pyautogui.locateOnScreen(wait_image, confidence=0.9)
        if location:
            print("Can't you read, Morty? It says PLEASE WAIT!")
            time.sleep(1)
        else:
            print("There, was that so hard, Morty? Wait time is over, now let's move on to the next task.")
            time.sleep(0.5)
            break


def move_mouse_to_icon(video_icon):
    """
    Move the mouse to a specified icon on the screen.

    This function continuously checks if a specified icon is present on the screen.
    It moves the mouse to the center of the icon once it's found.

    Args:
        video_icon (str): The filename of the icon to move the mouse to.

    Returns:
        None
    """
    while True:
        location = pyautogui.locateOnScreen(video_icon, confidence=0.7)
        if location:
            print("Let's move the mouse to the video icon and prepare to drag it like Jerry through a Nickelback concert!")
            pyautogui.moveTo(pyautogui.center(location))
            time.sleep(.5)
            break
        else:
            print("Stop distracting me, Morty! I'm trying to find the damn video icon!")
            time.sleep(0.5)

def drag_videos(video_icon, video_track_icon):
    """
    Drag a video icon onto a video track icon on the screen.

    This function first finds the video icon and the video track icon within a specified region.
    Then, it simulates dragging the video icon to the video track icon and releasing it.

    Args:
        video_icon (str): The filename of the video icon to be dragged.
        video_track_icon (str): The filename of the video track icon where the video will be dropped.

    Returns:
        None
    """
    search_region = (59, 613, 233, 678)
    
    # First, find the video icon
    video_location = pyautogui.locateOnScreen(video_icon, confidence=0.8)
    if video_location:
        video_center = pyautogui.center(video_location)
        
        # Then, find the video track icon
        video_track_location = pyautogui.locateOnScreen(video_track_icon, confidence=0.8, region=search_region)
        if video_track_location:
            video_track_center = pyautogui.center(video_track_location)
            
            # Move the mouse to the video icon and press the mouse button to start dragging
            pyautogui.mouseDown(x=video_center.x, y=video_center.y, button='left')
            print("Grabbing the video icon like it's a flask of Mega Seeds!")
            
            # Move the mouse to the video track icon, while holding the button down
            pyautogui.moveTo(video_track_center.x, video_track_center.y, duration=1)
            time.sleep(25)
            
            # Release the mouse button to drop the video icon onto the video track icon
            pyautogui.mouseUp(button='left')
            time.sleep(5)
            print("Dropped the video into the track like it's hot, Morty!")
        else:
            print("Where's that video track icon, Morty? I can't drag without a target!")
    else:
        print("Video icon's playing hide and seek, Morty. Can't drag what I can't find!")

def locate_video_track(video_track_icon):
    """
    Locate the video track plus icon on the screen within a specified region.

    This function searches for the video track plus icon by comparing it to an image file within a defined region.

    Args:
        video_track_icon (str): The filename of the video track plus icon to locate.

    Returns:
        tuple or None: The location (left, top, width, height) of the video track plus icon if found, or None if not found.
    """
    # Define the search region (left, top, width, height)
    search_region = (59, 613, 233, 678)

    while True:
        video_track_location = pyautogui.locateOnScreen(video_track_icon, confidence=0.9, region=search_region)
        if video_track_location:
            print("I found it Morty!, I fucking found it!!! The videos track plus icon Morty, it's right fucking there!!")
            return video_track_location
        else:
            print("Stop distracting me Morty, I'm trying to find the damn video track plus icon!")
            time.sleep(0.5)

def click_movavi_change_button(movavi_change_button):
    start_time = time.time()  # Note the starting time
    while True:
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f"Elapsed time: {elapsed_time}")  # Debugging, because clearly something's off
        
        if elapsed_time > 3:  # If more than 3 seconds have passed
            print("Gave up on finding the change button. Moving on.")
            break

        movavi_change_button_location = pyautogui.locateOnScreen(movavi_change_button, confidence=0.9)
        if movavi_change_button_location:
            movavi_change_button_center = pyautogui.center(movavi_change_button_location)
            pyautogui.click(movavi_change_button_center)
            print("Clicked the button. Finally!")
            break
        else:
            print("Still can't find the damn button...")

def double_click_audio_folder(audio_folder):
    """
    Double-click the audio folder in the Movavi Video Editor to open it.

    This function searches for the audio folder by comparing it to an image file and double-clicks it when found.

    Args:
        audio_folder (str): The filename of the audio folder image to locate and double-click.

    Returns:
        None
    """
    while True:
        audio_folder_location = pyautogui.locateOnScreen(audio_folder, confidence=0.9)
        if audio_folder_location:
            audio_folder_center = pyautogui.center(audio_folder_location)
            pyautogui.doubleClick(audio_folder_center)
            print("Clicking the audio folder so we can add some tunes, Morty!")
            break
        else:
            print("I know you hate good music Morty, but just wait a minute while I find the folder.")
            time.sleep(0.5)

def move_mouse_to_audio_file(music_icon):
    """
    Move the mouse cursor to an audio file icon in the Movavi Video Editor interface.

    This function searches for the audio file icon by comparing it to an image file and moves the mouse cursor
    to the center of the found icon.

    Args:
        music_icon (str): The filename of the audio file icon image to locate.

    Returns:
        None
    """
    while True:
        audio_file_location = pyautogui.locateOnScreen(music_icon, confidence=0.9)
        if audio_file_location:
            audio_file_center = pyautogui.center(audio_file_location)
            pyautogui.moveTo(audio_file_center)
            print("Moving the mouse to the audio file so we can prepare to drag it.")
            break
        else:
            print("I know you hate good music Morty, but just wait a minute while I find the file.")
            time.sleep(0.5)

def drag_audio_files(music_icon, audio_track_icon):
    """
    Drag an audio file to the audio track in the Movavi Video Editor interface.

    This function first locates the music icon and the audio track icon in the interface, then drags the music icon
    to the audio track icon, effectively adding the audio to the project.

    Args:
        music_icon (str): The filename of the music icon image to locate.
        audio_track_icon (str): The filename of the audio track icon image to locate.

    Returns:
        None
    """
    # First, find that elusive music icon
    music_location = pyautogui.locateOnScreen(music_icon, confidence=0.9)
    if music_location:
        music_center = pyautogui.center(music_location)
        
        # Next, get the location of the audio track icon
        audio_track_location = pyautogui.locateOnScreen(audio_track_icon, confidence=0.9)
        if audio_track_location:
            audio_track_center = pyautogui.center(audio_track_location)
            
            # Press the mouse button down on the music icon
            pyautogui.mouseDown(x=music_center.x, y=music_center.y, button='left')
            print("Grabbing the music icon like it's a sweet, sweet tune, Morty!")
            
            # Drag that bad boy over to the audio track icon
            pyautogui.moveTo(audio_track_center.x, audio_track_center.y, duration=1)
            
            # Release the mouse button to drop it like it's hot
            pyautogui.mouseUp(button='left')
            print("Dropped the music into the audio track, Morty! Let's get schwifty!")
            
        else:
            print("I can't find the audio track icon, Morty! What's the point of music without a track?")
            
    else:
        print("The music icon's gone rogue, Morty! No music for you!")

def type_project_name():
    """
    Type the project name in the Movavi Video Editor interface.

    This function simulates typing the project name 'shravana' in the appropriate field in the Movavi Video Editor
    interface.

    Args:
        None

    Returns:
        None
    """
    print("Typing the project name...")
    pyautogui.write('shravana')
    time.sleep(1)

def click_save(save_image):
    """
    Click the 'Save' button in the Movavi Video Editor interface.

    This function locates and clicks the 'Save' button in the Movavi Video Editor interface based on the provided image
    location.

    Args:
        save_image (str): The filename of the image representing the 'Save' button.

    Returns:
        None
    """
    while True:
        save_image_location = pyautogui.locateOnScreen(save_image, confidence=0.9)
        if save_image_location:
            save_image_center = pyautogui.center(save_image_location)
            print("About to save the project, Morty!")
            pyautogui.click(save_image_center)
            break
        else:
            print("Hang on you little dork, saving our progress is important and I'm trying to find the save button!")
            time.sleep(0.5)

def click_file_image(file_image):
    """
    Click the 'File' menu in the Movavi Video Editor interface.

    This function locates and clicks the 'File' menu in the Movavi Video Editor interface based on the provided image
    location.

    Args:
        file_image (str): The filename of the image representing the 'File' menu.

    Returns:
        None
    """
    while True:
        file_image_location = pyautogui.locateOnScreen(file_image, confidence=0.9)
        if file_image_location:
            file_image_center = pyautogui.center(file_image_location)
            print("About to click File.")
            pyautogui.click(file_image_center)
            break
        else:
            print("Hang on you little dork, accessing the File menu is important, and I'm trying to find it!")
            time.sleep(0.5)

def click_ctrl_s_image(ctrl_s_image):
    """
    Click the 'Ctrl + S' shortcut in the Movavi Video Editor interface.

    This function locates and clicks the 'Ctrl + S' shortcut in the Movavi Video Editor interface based on the provided
    image location.

    Args:
        ctrl_s_image (str): The filename of the image representing the 'Ctrl + S' shortcut.

    Returns:
        None
    """
    while True:
        click_ctrl_s_image_location = pyautogui.locateOnScreen(ctrl_s_image, confidence=0.9)
        if click_ctrl_s_image_location:
            click_ctrl_s_image_center = pyautogui.center(click_ctrl_s_image_location)
            print("About to click Ctrl + S!")
            pyautogui.click(click_ctrl_s_image_center)
            time.sleep(2)
            break
        else:
            print("Hang on you little dork, saving our progress is important, and I'm trying to find the shortcut!")
            time.sleep(0.5)

def press_spacebar_to_play():
    """
    Press the spacebar key to play the video in Movavi Video Editor.

    This function simulates pressing the spacebar key to play or pause the video playback in Movavi Video Editor.

    Returns:
        None
    """
    pyautogui.press('space')

def click_logo_text():
    """
    Click the logo text within Movavi Video Editor.

    This function searches for the logo text within the Movavi Video Editor interface and clicks on it.

    Returns:
        None
    """
    while True:
        logo_text_image_location = pyautogui.locateOnScreen(logo_text, confidence=0.8)
        if logo_text_image_location:
            logo_text_center = pyautogui.center(logo_text_image_location)
            print("About to click Logo...")
            pyautogui.click(logo_text_center)
            break
        else:
            print("I have not seen the logo button yet, hang on!")
            time.sleep(0.5)

def click_add_logo_button():
    """
    Click the "Add Logo" button within Movavi Video Editor.

    This function searches for the "Add Logo" button within the Movavi Video Editor interface and clicks on it.

    Returns:
        None
    """
    while True:
        add_logo_location = pyautogui.locateOnScreen(add_logo_button, confidence=0.8)
        if add_logo_location:
            add_logo_center = pyautogui.center(add_logo_location)
            print("About to click the add logo button...")
            pyautogui.click(add_logo_center)
            break
        else:
            print("I have not seen the add logo button yet, hang on!")
            time.sleep(0.5)

def move_logo(logo_movement_handle):
    """
    Move a logo to a specific location within the Movavi Video Editor interface.

    This function searches for a logo specified by its image handle and moves it to a predefined location within
    the Movavi Video Editor interface.

    Args:
        logo_movement_handle (str): The image handle of the logo to be moved.

    Returns:
        None
    """
    # Define the search region within the Movavi Video Editor interface
    search_region = (1674, 303, 1907, 456)

    while True:
        # First, find the logo specified by its image handle
        logo_location = pyautogui.locateOnScreen(logo_movement_handle, confidence=0.8, region=search_region)
        if logo_location:
            logo_center = pyautogui.center(logo_location)

            # Define the target location where the logo should be moved
            logo_target_location_x = 1769
            logo_target_location_y = 331

            # Press the mouse button down on the logo
            pyautogui.mouseDown(x=logo_center.x, y=logo_center.y, button='left')
            print("Grabbing the logo like it's a sweet, sweet lady, Morty!")

            # Drag the logo to the target location
            pyautogui.moveTo(logo_target_location_x, logo_target_location_y, duration=1)

            # Release the mouse button to drop the logo at the target location
            pyautogui.mouseUp(button='left')
            print("Dropped the logo into the bottom right corner of the video, Morty! Let's get schwifty!")
            break  # Exit the loop once the logo is found and moved
        else:
            print("I can't find the logo yet, Morty! Let's keep looking!")
            time.sleep(0.5)  # Introduce a short delay before the next search iteration

def resize_logo():
    """
    Resize a logo within the Movavi Video Editor interface.

    This function resizes a logo by clicking and dragging its corner to a new location within
    the Movavi Video Editor interface.

    Args:
        None

    Returns:
        None
    """
    # Define the coordinates of the top-left corner of the logo
    top_left_corner_x = 1672
    top_left_corner_y = 308

    # Press the mouse button down on the top-left corner of the logo
    pyautogui.mouseDown(x=top_left_corner_x, y=top_left_corner_y, button='left')

    # Define the target location for resizing the logo
    corner_dot_target_location_x = 1746
    corner_dot_target_location_y = 362

    print("Grabbing the logo corner like it's a sweet, sweet lady, Morty!")

    # Drag the corner of the logo to the target location for resizing
    pyautogui.moveTo(corner_dot_target_location_x, corner_dot_target_location_y, duration=1)

    # Release the mouse button to complete the resizing
    pyautogui.mouseUp(button='left')

    print("Resized the logo to fit the bottom corner better, Morty! Let's get schwifty!")


def click_blank_area_to_set_logo():
    pyautogui.click(892, 578)


def add_channel_logo():
    """
    Add a channel logo to a video project in Movavi Video Editor.

    This function performs a series of actions to add a channel logo to a video project
    within the Movavi Video Editor interface.

    Args:
        None

    Returns:
        None
    """
    # Click the "More Tools" button
    click_more_tools_button()

    # Click the "Video Editing" dropdown
    click_video_editing_dropdown()

    # Click the "Logo & Text" button
    click_logo_text()

    # Click the "Add Logo or Text" button
    click_add_logo_button()

    #Sleep briefly to let the folder load
    time.sleep(1)

    # Navigate to the channel logo file path
    goto_channel_logo_path(logo_path)

    # Move the selected logo to a specific location
    move_logo(logo_movement_handle)

    # Resize the logo to fit the desired position
    resize_logo()

def click_more_tools_button():
    """
    Click the "More Tools" button within Movavi Video Editor.

    This function locates and double-clicks the "More Tools" icon in Movavi Video Editor's interface.

    Args:
        None

    Returns:
        None
    """
    while True:
        # Locate the "More Tools" icon on the screen
        more_tools_icon_image_location = pyautogui.locateOnScreen(more_tools_icon, confidence=0.8)
        if more_tools_icon_image_location:
            more_tools_center = pyautogui.center(more_tools_icon_image_location)

            # Double-click the "More Tools" icon to open it
            pyautogui.doubleClick(more_tools_center)
            print("Clicked the More Tools icon.")
            break
        else:
            print("The More Tools icon is not visible yet. Waiting...")
            time.sleep(0.5)

def click_video_editing_dropdown():
    """
    Click the "Video Editing" dropdown in Movavi Video Editor.

    This function locates and clicks the "Video Editing" dropdown button in Movavi Video Editor's interface.

    Args:
        None

    Returns:
        None
    """
    while True:
        # Locate the "Video Editing" dropdown button on the screen
        video_editing_dropdown_location = pyautogui.locateOnScreen(video_editing_button, confidence=0.8)
        if video_editing_dropdown_location:
            video_editing_dropdown_center = pyautogui.center(video_editing_dropdown_location)

            # Click the "Video Editing" dropdown button
            pyautogui.click(video_editing_dropdown_center)
            print("Clicked the Video Editing dropdown.")
            break
        else:
            print("The Video Editing dropdown is not visible yet. Waiting...")
            time.sleep(0.5)

def goto_channel_logo_path(logo_path):
    """
    Navigate to the specified folder path in the file explorer.

    This function types the provided path in a file explorer dialog and presses Enter to navigate to it.

    Args:
        logo_path (str): The path to the folder to navigate to.

    Returns:
        None
    """
    # Type the provided path
    pyautogui.write(logo_path)
    time.sleep(1)  # Wait for 1 second
    pyautogui.press('enter')  # Press Enter to navigate to the folder



def type_project_path(movavi_project_path):
    """
    Type the project path and press Enter.

    This function types the specified project path into the active window and then presses the Enter key.

    Args:
        movavi_project_path (str): The project path to type.

    Returns:
        None
    """
    pyautogui.write(movavi_project_path)
    time.sleep(1)
    pyautogui.press('enter')

def click_file_name_text_box(file_name_text_box):
    """
    Click the file name text box.

    This function clicks the specified file name text box on the screen.

    Args:
        file_name_text_box (str): The image of the file name text box to click.

    Returns:
        None
    """
    while True:
        file_name_location = pyautogui.locateOnScreen(file_name_text_box, confidence=0.8)
        if file_name_location:
            file_name_center_x, file_name_center_y = pyautogui.center(file_name_location)
            print("About to click the file name text box...")
            pyautogui.click(file_name_center_x + 41, file_name_center_y)
            break
        else:
            print("I have not seen the file name text box yet, hang on!")
            time.sleep(0.5)

def run_video_editor_utility():
    # Time to kick things off, Morty!
    
    # Start the video editor by locating its shortcut
    start_video_editor(video_editor_icon)
    
    # Exit any annoying pop-ups that show up
    exit_popup(exit_icon)
    
    # Create a new project
    create_new_project()
    
    # Click the initial "Add Files" button
    initial_add_files(add_files_image)
    
    # Enter the file path to the media
    enter_file_path(nakshatra_file_path)
    
    # Press Enter to continue
    press_enter()
    
    # Click the "Animated Images" folder
    click_animated_images_folder()
    
    # Click to select all media
    select_all()
    
    # Click the "Open" button
    click_open(open_image)
    
    # Wait for the loading screen to disappear
    wait(wait_image)
    
    # Move the mouse to the video icon
    move_mouse_to_icon(video_icon)
    
    # Drag videos onto the video track
    drag_videos(video_icon, video_track_icon)
    
    # Click the Movavi change button
    click_movavi_change_button(movavi_change_button)
    
    # Use the hotkey to add media
    add_media_hotkey()
    
    # Click the "Nakshatra" folder
    click_nakshatra_folder()
    
    # Double click the audio folder
    double_click_audio_folder(audio_folder)
    
    # Select all audio media
    select_all()
    
    # Click the "Open" button for audio
    click_open(open_image)
    
    # Move the mouse to the music icon
    move_mouse_to_audio_file(music_icon)
    
    # Drag audio files onto the audio track
    drag_audio_files(music_icon, audio_track_icon)
    
    add_channel_logo()
    click_blank_area_to_set_logo()

    # Click the "File" menu
    click_file_image(file_image)
    
    # Click the Ctrl+S (Save) option
    click_ctrl_s_image(ctrl_s_image)
    
    # Click the folder icon
    click_folder_icon()
    
    # Type the project path
    type_project_path(movavi_project_path)
    
    # Click the file name text box
    click_file_name_text_box(file_name_text_box)
    
    # Type the project name
    type_project_name()
    
    # Click the "Save" button
    click_save(save_image)
    
    # Print a message to indicate completion
    print("That's it, this entire project was just automated because I AM PICKLE RICK!!!")
    
    # Press the spacebar to play the project
    press_spacebar_to_play()