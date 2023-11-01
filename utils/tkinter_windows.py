import tkinter as tk
import queue
from config import ANIMATION_DURATION, DOWNLOAD_DURATION
from .auto_ideogram import item_count

class TkinterManager:
    def __init__(self):
        self.user_input = 0  # Initialize user_input

    def destroy_animation_window(self):
        self.animation_window.destroy()

    def set_window_geometry(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def create_animation_window(self, animation_queue):
        self.animation_window = tk.Tk()
        self.animation_window.title("Animation Counter")
        self.animation_window.attributes('-topmost', True)
        self.set_window_geometry(self.animation_window, 400, 100)

        # Initialize Tkinter variables here
        self.current_image = tk.IntVar(value=0)
        self.remaining_images = tk.IntVar(value=0)
        self.total_time_remaining = 0
        self.estimated_time_left = tk.StringVar(value="00:00:00")

        # Ensure user_input is properly set before using it
        if self.user_input <= 0:
            print("Error: user_input is not properly set")
            return

        self.remaining_images.set(self.user_input)
        self.total_time_remaining = self.user_input * ANIMATION_DURATION + 7  # Initialize total time remaining

        # Create and pack labels
        self.current_image_text_label = tk.Label(self.animation_window, text="Animating number:")
        self.current_image_text_label.pack()
        self.current_image_label = tk.Label(self.animation_window, textvariable=self.current_image)
        self.current_image_label.pack()

        self.remaining_images_text_label = tk.Label(self.animation_window, text="Remaining images:")
        self.remaining_images_text_label.pack()
        self.remaining_images_label = tk.Label(self.animation_window, textvariable=self.remaining_images)
        self.remaining_images_label.pack()

        self.estimated_time_label = tk.Label(self.animation_window, textvariable=self.estimated_time_left)
        self.estimated_time_label.pack()

        self.animation_window.after(1000, self.update_animation_label, animation_queue)
        self.animation_window.mainloop()

    def update_animation_label(self, animation_queue):
        try:
            animated_images = animation_queue.get_nowait()
            self.current_image.set(animated_images)
            remaining_images = self.user_input - animated_images
            self.remaining_images.set(remaining_images)
        except queue.Empty:
            pass

        # Decrement total time remaining every second and update timer
        self.total_time_remaining -= 1
        if self.total_time_remaining <= 0:
            self.animation_window.destroy()  # Close the window when time reaches zero
            return  # Exit the update method

        # Convert total time remaining to HH:MM:SS format and update estimated_time_left variable
        hours, remainder = divmod(self.total_time_remaining, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.estimated_time_left.set(f"{hours:02}:{minutes:02}:{seconds:02}")

        # Schedule the next call to update_animation_label
        self.animation_window.after(1000, self.update_animation_label, animation_queue)

    def create_download_window(self, download_queue):
        self.download_window = tk.Tk()
        self.download_window.title("Patience please... ♄")
        self.download_window.attributes('-topmost', True)
        self.set_window_geometry(self.download_window, 400, 100)

        self.download_counter_label = tk.Label(self.download_window, text="Downloading, please wait...")
        self.download_counter_label.pack()

        self.download_window.after(100, self.update_download_label, download_queue)
        self.download_window.mainloop()

    def update_download_label(self, download_queue):
        try:
            number = download_queue.get_nowait()
            remaining_videos = self.user_input - number
            estimated_time_left = remaining_videos * DOWNLOAD_DURATION
            self.download_counter_label.config(text=f"Downloaded: {number}, Remaining: {remaining_videos}, Estimated Time Left: {estimated_time_left} seconds")
        except queue.Empty:
            self.download_counter_label.config(text="Waiting for next download...")
        finally:
            self.download_window.after(100, self.update_download_label, download_queue)

    def destroy_download_window(self):
        self.download_window.destroy()
