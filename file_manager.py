"""Handles file selection using Tkinter."""

import tkinter as tk
from tkinter import filedialog

def select_image():
    """
    Opens file dialog for user to select an image.
    """
    root = tk.Tk()
    root.withdraw()  # Hide main window
    root.attributes('-topmost', True)  # Bring dialog to front
    root.update()

    file_path = filedialog.askopenfilename(
        title="Select a Screenshot",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )

    root.destroy()
    return file_path
