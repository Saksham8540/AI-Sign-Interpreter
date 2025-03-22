from PIL import Image
import os

# Path to the image in the data folder
image_path = os.path.join(os.getcwd(), "data", "bg.png")
print(f"Testing image path: {image_path}")

try:
    # Open and display the image
    image = Image.open(image_path)
    image.show()
    print("✅ Image loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load image: {e}")
