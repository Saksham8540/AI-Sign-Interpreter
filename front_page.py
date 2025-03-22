import tkinter as tk
from PIL import Image, ImageTk
import os
from main import start_gesture_recognition
from collect_data import start_data_collection

# Function to start gesture recognition
def start_recognition():
    root.destroy()
    start_gesture_recognition()

# Function to start data collection
def start_data():
    root.destroy()
    start_data_collection()

# Hover effects for buttons
def on_enter(e, color):
    e.widget.config(bg=color)

def on_leave(e, color):
    e.widget.config(bg=color)

# Create GUI using Tkinter
root = tk.Tk()
root.title("Sign Language Interpretation System")
root.geometry("600x450")

# Load background image from data folder
try:
    # Correct path to the image inside the data folder
    image_path = os.path.join(os.getcwd(), "data", "bg.png")
    print(f"Loading image from: {image_path}")

    # Open and resize using PIL
    image = Image.open(image_path)
    image = image.resize((600, 450), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(image)

    # Keep reference to avoid garbage collection
    root.bg_image = bg_image

    background_label = tk.Label(root, image=root.bg_image)
    background_label.place(relwidth=1, relheight=1)

except Exception as e:
    print(f"❌ Error loading background image: {e}")

# Title Label
label = tk.Label(root, text="Welcome to Sign Language Interpretation", 
                 font=("Arial", 20, "bold"), bg="#ffffff", fg="#333333")
label.place(relx=0.5, rely=0.2, anchor="center")

# Start Recognition Button
start_button = tk.Button(root, text="Start Gesture Recognition", font=("Arial", 14), 
                         bg="#4caf50", fg="white", command=start_recognition, 
                         width=25, height=2, relief="raised", borderwidth=3)
start_button.place(relx=0.5, rely=0.4, anchor="center")
start_button.bind("<Enter>", lambda e: on_enter(e, "#388e3c"))
start_button.bind("<Leave>", lambda e: on_leave(e, "#4caf50"))

# Start Data Collection Button
collect_button = tk.Button(root, text="Start Data Collection", font=("Arial", 14), 
                           bg="#2196f3", fg="white", command=start_data, 
                           width=25, height=2, relief="raised", borderwidth=3)
collect_button.place(relx=0.5, rely=0.5, anchor="center")
collect_button.bind("<Enter>", lambda e: on_enter(e, "#1976d2"))
collect_button.bind("<Leave>", lambda e: on_leave(e, "#2196f3"))

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), bg="#f44336", fg="white", 
                        command=root.quit, width=25, height=2, relief="raised", borderwidth=3)
exit_button.place(relx=0.5, rely=0.6, anchor="center")
exit_button.bind("<Enter>", lambda e: on_enter(e, "#d32f2f"))
exit_button.bind("<Leave>", lambda e: on_leave(e, "#f44336"))

# Start the main loop
root.mainloop()
