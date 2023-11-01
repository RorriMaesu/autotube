import pyautogui
import time
import queue
import threading
import tkinter as tk
from config import DOWNLOAD_DURATION


pyautogui.PAUSE = .72  # pause for each action

class DownloadManager:
    def __init__(self, user_input):
        self.user_input = user_input
        self.download_counter = 0

    def create_download_window(self, download_queue):
        window = tk.Tk()
        window.title("Patience please... ♄")
        window.attributes('-topmost', True)
        self.counter_label = tk.Label(window, text="Give me a minute, I'm looking for the download button! 😠")
        self.counter_label.pack()

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = 400
        window_height = 100
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

        # Set up an initial call to update_download_label after 1000 milliseconds (1 second)
        window.after(1000, self.update_download_label, download_queue)
        window.mainloop()

    def update_download_label(self, download_queue):
        try:
            # Non-blocking get from queue
            number = download_queue.get_nowait()
            remaining_videos = self.user_input - number
            estimated_time_left = remaining_videos * DOWNLOAD_DURATION
            self.counter_label.config(
                text=f"Downloaded: {number}, Remaining: {remaining_videos}, Estimated Time Left: {estimated_time_left} seconds")
        except queue.Empty:
            # Handle empty queue here if necessary
            pass
        finally:
            # Schedule the next call to update_download_label
            self.counter_label.after(1000, self.update_download_label, download_queue)

    def find_username(self):
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write('from: abitdiphrent')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

    def find_download_button(self):
        return pyautogui.locateOnScreen('images/video_download.png', confidence=0.8)

    def find_next_button(self):
        return pyautogui.locateOnScreen('images/next_button.png', confidence=0.8)

    def click_download_button(self, download_queue, download_button_location):
        pyautogui.click(download_button_location)
        self.download_counter += 1
        download_queue.put(self.download_counter)
        time.sleep(2)

    def click_next_button(self, next_button_location):
        pyautogui.click(next_button_location)
        time.sleep(3)

    def clear_downloads(self):
        clear_download_location = None
        while not clear_download_location:
            clear_download_location = pyautogui.locateOnScreen('images/clear_download.png', confidence=0.8)
            if not clear_download_location:
                time.sleep(1)  # Wait for a short period before trying again to reduce CPU usage

        clear_download_center = pyautogui.center(clear_download_location)
        pyautogui.click(clear_download_center)

    def move_mouse_to_video(self):
        pyautogui.moveTo(1756, 856, duration=0.3)

    def scroll_down_slowly(self, download_queue):
        download_button_location = None  # Initialize to None
        
        while download_button_location is None:  # Loop until the download button is found
            pyautogui.scroll(-27)  # Scroll down slowly
            time.sleep(0.3)  # Wait a little for the page to adjust

            download_button_location = self.find_download_button()  # Look for the download button
            
            if download_button_location:  # If found, click it
                self.click_download_button(download_queue, download_button_location)
            else:
                print("Download button not found during slow scroll. Scrolling again...")

    def scroll_down(self):
        pyautogui.scroll(-180)

    def download_video(self, download_queue):
        self.move_mouse_to_video()
        download_button_location = self.find_download_button()
        if download_button_location:
                print("Download button located!")
                self.click_download_button(download_queue, download_button_location)
                print("Download button clicked!")
                time.sleep(2)
                self.clear_downloads()
                print("Download window cleared.")
                self.move_mouse_to_video()
                self.scroll_down()
                
        else:
            self.scroll_down_slowly(download_queue)
            print("Download button not found.")
            
        while self.download_counter < self.user_input:
            self.move_mouse_to_video()
            self.scroll_down()
            download_button_location = self.find_download_button()
            if download_button_location:
                print("Download button located!")
                self.click_download_button(download_queue, download_button_location)
                print("Download button clicked!")
                self.clear_downloads()
                print("Download window cleared.")
                self.move_mouse_to_video()
                self.scroll_down()
                next_button_location = self.find_next_button()
                if next_button_location:
                    self.click_next_button(next_button_location)
            else:
                self.scroll_down_slowly(download_queue)
                print("Download button not found.")
                next_button_location = self.find_next_button()
                if next_button_location:
                    self.click_next_button(next_button_location)

    def download_phase(self):
        self.find_username()
        download_queue = queue.Queue()
        download_window_thread = threading.Thread(target=self.create_download_window, args=(download_queue,))
        download_window_thread.start()
        self.download_video(download_queue)
