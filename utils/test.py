import time
import pyautogui
time.sleep(5)


video_icon = 'images/video_icon_image.png'  # Path to the video icon image



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
        location = pyautogui.locateOnScreen(video_icon, confidence=0.9)
        if location:
            print("Let's move the mouse to the video icon and prepare to drag it like Jerry through a Nickelback concert!")
            pyautogui.moveTo(pyautogui.center(location))
            pyautogui.click(pyautogui.center(location))
            time.sleep(.5)
            break
        else:
            print("Stop distracting me, Morty! I'm trying to find the damn video icon!")
            time.sleep(0.5)


move_mouse_to_icon(video_icon)