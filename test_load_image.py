import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Test Background")
root.geometry("600x450")

# Load and display the image
try:
    image_path = os.path.join(os.getcwd(), "data", "bg.png")
    print(f"Testing image path: {image_path}")
    
    image = Image.open(image_path)
    image = image.resize((600, 450), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(image)
    
    # Keep reference to avoid garbage collection
    root.bg_image = bg_image
    
    label = tk.Label(root, image=root.bg_image)
    label.place(relwidth=1, relheight=1)
    
except Exception as e:
    print(f"Error loading background image: {e}")

root.mainloop()
