# Import necessary libraries and modules
import pyautogui  # Library for automating mouse and keyboard actions
import time  # Library for handling time-related operations
import queue  # Library for implementing queues
import threading  # Library for creating and managing threads
import tkinter as tk  # Library for creating GUI applications
from config import DOWNLOAD_DURATION  # Import the DOWNLOAD_DURATION from the config module
from .browser_utils import close_browser  # Import item_count and close_browser functions from auto_ideogram module
from .auto_ideogram import item_count

# Set the pause duration for pyautogui actions
pyautogui.PAUSE = 1  # Pause for each action to simulate human interaction

username = "from: abitdiphrent" #Replace with "from: yourusername" this is the username used in Discord.

# Define the DownloadManager class, responsible for managing downloads
class DownloadManager:
    def __init__(self, item_count):
        """
        Constructor for the DownloadManager class.

        Parameters:
        - item_count (int): The total number of items to download.
        """
        # Initialize instance variables
        self.item_count = item_count  # The total number of items to download
        self.download_counter = 0  # Counter for tracking the number of downloads completed
        self.should_destroy_download_window = False  # Flag to indicate if the download window should be destroyed


    def check_destroy_window(self):
        """
        Check whether the download window should be destroyed or not.

        If `should_destroy_download_window` is True, the window will be destroyed.
        Otherwise, the method will continue to check after a delay of 100 milliseconds.
        """
        if self.should_destroy_download_window:
            self.window.destroy()  # Destroy the download window
        else:
            self.window.after(100, self.check_destroy_window)  # Continue checking after a delay


    def destroy_download_window(self):
        """
        Set the flag to indicate that the download window should be destroyed.

        This method sets the `should_destroy_download_window` flag to True, which
        will trigger the destruction of the download window in the `check_destroy_window` method.
        """
        self.should_destroy_download_window = True  # Set the flag to destroy the download window


    def create_download_window(self, download_queue):
        """
        Create a tkinter window to display the download progress.

        This method creates a graphical window using tkinter to show the download progress.
        It includes a label that displays a message and positions the window at the center of the screen.

        Args:
            download_queue (queue.Queue): A queue to monitor download progress.

        Note:
            The `check_destroy_window` method is scheduled to run periodically to check if the
            window should be destroyed.

        Returns:
            None
        """
        self.window = tk.Tk()  # Create a tkinter window
        self.window.title("Patience please... ♄")  # Set the window title
        self.window.attributes('-topmost', True)  # Ensure the window is on top
        self.counter_label = tk.Label(self.window, text="Give me a minute, I'm looking for the download button!")  # Create a label
        self.counter_label.pack()  # Pack the label into the window

        # Position the window at the center of the screen
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = 400
        window_height = 100
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

        # Schedule the `check_destroy_window` method to run periodically
        self.window.after(100, self.check_destroy_window)

        # Start the tkinter main loop to display the window
        self.window.mainloop()


    def update_download_label(self, download_queue):
        """
        Update the download progress label in the tkinter window.

        This method retrieves the current download progress from the queue and calculates
        the remaining items and estimated time left for the downloads. It then updates
        the text displayed in the label accordingly.

        Args:
            download_queue (queue.Queue): A queue containing download progress information.

        Returns:
            None
        """
        try:
            number = download_queue.get_nowait()  # Get the current download progress
            remaining_videos = self.item_count - number  # Calculate remaining items
            estimated_time_left = remaining_videos * DOWNLOAD_DURATION  # Calculate estimated time left
            # Update the label text with download progress information
            self.counter_label.config(
                text=f"Downloaded: {number}, Remaining: {remaining_videos}, Estimated Time Left: {estimated_time_left} seconds")
        except queue.Empty:
            pass
        finally:
            # Schedule this method to run again after 1000 milliseconds (1 second)
            self.counter_label.after(1000, self.update_download_label, download_queue)
    

    def find_username(self, username):
        #Takes in username variable set earlier because it will type that username into the finder box.
        """
        Perform a search for a specific username in a text editor.

        This method uses keyboard shortcuts and text input to initiate a search for
        a specific username ('from: abitdiphrent') in a text editor. It simulates the
        keypresses and waits between actions for proper execution.

        Args:
            None

        Returns:
            None
        """
        pyautogui.hotkey('ctrl', 'f')  # Press Ctrl + F to initiate the find/search dialog
        time.sleep(1)
        pyautogui.write(f"{username}")  # Type the username to search for [THIS WILL NEED TO BE YOUR USERNAME]
        time.sleep(1)
        pyautogui.press('enter')  # Press Enter to perform the search
        time.sleep(1)  # Wait for stability before proceeding


    def find_download_button(self):
        """
        Locate and return the position of the video download button on the screen.

        This method uses PyAutoGUI's `locateOnScreen` function to search for an image
        ('video_download.png') that represents the download button. The confidence
        threshold is set to 0.8 for reliable identification.

        Args:
            None

        Returns:
            tuple or None: A tuple containing the coordinates (x, y) of the found
            download button, or None if it's not found.
        """
        return pyautogui.locateOnScreen('images/video_download.png', confidence=0.8)


    def find_next_button(self):
        """
        Find and locate the 'Next' button on the screen.

        Returns:
            tuple or None: A tuple representing the location of the 'Next' button (x, y coordinates)
                if found, or None if not found.
        """
        return pyautogui.locateOnScreen('images/next_button.png', confidence=0.8)


    def click_download_button(self, download_queue, download_button_location):
        """
        Click the download button and update the download counter.

        Args:
            download_queue (queue.Queue): A queue for tracking the number of downloads.
            download_button_location (tuple): A tuple representing the location of the download button (x, y coordinates).
        """
        # Click the download button
        pyautogui.click(download_button_location)
        
        # Increment the download counter
        self.download_counter += 1
        
        # Update the download queue with the current counter value
        download_queue.put(self.download_counter)
        
        # Sleep for 2 seconds to allow time for the download to start
        time.sleep(2)


    def click_next_button(self, next_button_location):
        """
        Click the next button to navigate to the next page.

        Args:
            next_button_location (tuple): A tuple representing the location of the next button (x, y coordinates).
        """
        # Click the next button
        pyautogui.click(next_button_location)
        
        # Sleep for 3 seconds to allow time for the next page to load
        time.sleep(3)


    def clear_downloads(self):
        """
        Click the clear downloads button to remove completed downloads.

        This method continuously checks for the presence of the clear downloads button and clicks it when found.
        """
        clear_download_location = None
        while not clear_download_location:
            clear_download_location = pyautogui.locateOnScreen('images/clear_download.png', confidence=0.8)
            
            # If the clear downloads button is not found, wait for 1 second and try again
            if not clear_download_location:
                time.sleep(1)

        # Get the center of the clear downloads button and click it
        clear_download_center = pyautogui.center(clear_download_location)
        pyautogui.click(clear_download_center)


    def move_mouse_to_video(self):
        """
        Move the mouse to a specific location on the screen where the video is located.

        This method moves the mouse cursor to the coordinates (1756, 856) on the screen, which is where the video is.
        It uses a duration of 0.3 seconds for the mouse movement to make it smoother.
        """
        pyautogui.moveTo(1756, 856, duration=0.3)


    def scroll_down_slowly(self, download_queue):
        """
        Scroll down slowly to find the download button and click it if found.

        This method performs a slow scroll operation to look for the download button on the screen. It repeatedly
        scrolls up and checks for the button's presence. If the download button is found, it clicks the button
        and updates the download queue. If not found, it continues scrolling.

        Parameters:
        - download_queue (queue.Queue): A queue to keep track of the number of downloads completed.
        """
        download_button_location = None
        while download_button_location is None:
            pyautogui.scroll(-27)  # Scroll up
            time.sleep(0.3)  # Wait for a short duration
            download_button_location = self.find_download_button()
            if download_button_location:
                self.click_download_button(download_queue, download_button_location)
            else:
                print("Download button not found during slow scroll. Scrolling again...")


    def scroll_down(self):
        """
        Scroll down rapidly.

        This method performs a rapid scroll operation by scrolling the screen downwards.

        Parameters:
        - None
        """
        pyautogui.scroll(-180)  # Scroll down by a large amount


    def download_video(self, download_queue):
        """
        Download videos.

        This method initiates the video download process, including finding and clicking the download button,
        clearing the download window, scrolling down to discover more videos, and navigating to the next page of videos.

        Parameters:
        - download_queue (queue.Queue): A queue used to track the number of downloaded videos.

        Returns:
        - None
        """
        self.move_mouse_to_video()  # Move the mouse to the video area
        download_button_location = self.find_download_button()  # Find the download button on the current page
        if download_button_location:
            print("Download button located!")
            self.click_download_button(download_queue, download_button_location)  # Click the download button
            print("Download button clicked!")
            time.sleep(2)
            self.clear_downloads()  # Clear the download window
            print("Download window cleared.")
            self.move_mouse_to_video()  # Move the mouse back to the video area
            self.scroll_down()  # Scroll down the page to discover more videos
        else:
            self.scroll_down_slowly(download_queue)  # Scroll down slowly and search for the download button
            print("Download button not found.")
        
        # Continue downloading videos until the download counter matches the total item count
        while self.download_counter < self.item_count:
            self.move_mouse_to_video()  # Move the mouse to the video area
            self.scroll_down()  # Scroll down the page to discover more videos
            download_button_location = self.find_download_button()  # Find the download button on the current page
            if download_button_location:
                print("Download button located!")
                self.click_download_button(download_queue, download_button_location)  # Click the download button
                print("Download button clicked!")
                self.clear_downloads()  # Clear the download window
                print("Download window cleared.")
                self.move_mouse_to_video()  # Move the mouse back to the video area
                self.scroll_down()  # Scroll down the page to discover more videos
                next_button_location = self.find_next_button()  # Find the next page button
                if next_button_location:
                    self.click_next_button(next_button_location)  # Click the next page button
            else:
                self.scroll_down_slowly(download_queue)  # Scroll down slowly and search for the download button
                print("Download button not found.")
                next_button_location = self.find_next_button()  # Find the next page button
                if next_button_location:
                    self.click_next_button(next_button_location)  # Click the next page button




    def download_phase(self):
        """
        Execute the download phase.

        This method orchestrates the entire download phase, including finding the username, creating a download window,
        starting a separate thread for the download window, initiating video downloads, and closing the browser.

        Returns:
        - None
        """
        self.find_username(username)  # Find and set the username in the search field
        download_queue = queue.Queue()  # Create a queue for tracking downloaded videos
        download_window_thread = threading.Thread(target=self.create_download_window, args=(download_queue,))
        download_window_thread.start()  # Start a separate thread for the download window
        self.download_video(download_queue)  # Start downloading videos
        print(f"Finished downloading {item_count} videos!")
        self.destroy_download_window()  # Close the download window
        print("Preparing to close the browser and launch the video editor.")
        close_browser()  # Close the browser window and proceed to the video editing phase