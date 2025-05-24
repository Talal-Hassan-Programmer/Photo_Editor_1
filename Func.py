#This file is for all funcs in this project

from tkinter import filedialog, Scale
from PIL import Image, ImageTk, ImageEnhance


# This function opens an image file and displays it on the provided canvas.
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
        canvas.pil_image = image  # ✅ Store the original image for saving




# This function saves the current image displayed on the canvas to a file.

def save_image(image):
    """Opens a dialog to save the edited image."""
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All files", "*.*")])
    if file_path:
        image.save(file_path)  # Save the image
        print(f"Image saved to {file_path}")


# This function updates the sharpness of the image displayed on the canvas based on the slider value.
def adjust_sharpness(canvas, factor):
    """Enhances sharpness using the Pillow image."""
    if hasattr(canvas, "pil_image"):
        enhancer = ImageEnhance.Sharpness(canvas.pil_image)  # ✅ Apply to correct image
        new_image = enhancer.enhance(float(factor))  # Convert scale value

        tk_image = ImageTk.PhotoImage(new_image)
        canvas.create_image(0, 0, anchor="nw", image=tk_image)

        # ✅ Update image references correctly
        canvas.image = tk_image
        canvas.pil_image = new_image  # Store the edited image



# This function creates a slider for adjusting the sharpness of the image.
def create_sharpness_slider(App, canvas):
    """Creates a slider to control sharpness."""
    sharpness_scale = Scale(App , from_=0.5, to=10, resolution=0.1,
                               orient="horizontal", label="Sharpness",
                               command=lambda v: adjust_sharpness(canvas, v))
    sharpness_scale.set(1.0)  # Default sharpness
    sharpness_scale.pack()
