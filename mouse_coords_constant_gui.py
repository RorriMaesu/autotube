import tkinter as tk
import pyautogui

def update_coordinates():
    x, y = pyautogui.position()  # Get the current mouse position
    coordinates_label.config(text=f"X: {x}, Y: {y}")  # Update the label with the new coordinates
    root.after(100, update_coordinates)  # Schedule the function to run again after 100ms

root = tk.Tk()  # Create the main window
root.title("Mouse Coordinates")  # Set the title of the window
root.geometry("200x50")  # Set the size of the window
root.attributes('-topmost', True)  # Make the window stay on top of others

coordinates_label = tk.Label(root, text="")  # Create a label to display the coordinates
coordinates_label.pack()  # Add the label to the window

update_coordinates()  # Start updating the coordinates

root.mainloop()  # Start the Tkinter event loop
