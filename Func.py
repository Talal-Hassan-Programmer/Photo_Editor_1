#This file is for all funcs in this project

from tkinter import filedialog
from PIL import Image, ImageTk

def open_image(canvas):
    """Open an image file and display it on the canvas."""
    file_path = filedialog.askopenfilename(
        title="Open Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    
    if file_path:
        # Open the image using PIL
        image = Image.open(file_path)
        
        # Convert the image to a PhotoImage
        photo = ImageTk.PhotoImage(image)
        
        # Clear the canvas and display the new image
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=photo)
        
        # Keep a reference to the image to prevent garbage collection
        canvas.image = photo