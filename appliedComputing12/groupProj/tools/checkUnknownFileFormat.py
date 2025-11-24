"""
Error:
InvalidArgumentError:  Unknown image file format. One of JPEG, PNG, GIF, BMP required.
Find the images using the following code and delete those images from the dataset. 
"""

from pathlib import Path
import imghdr

data_dir = "/Users/home/Downloads/fruity"
image_extensions = [".png", ".jpg"]  # add there all your images file extensions

img_type_accepted_by_tf = ["bmp", "gif", "jpeg", "png", "jpg"]
                           
for filepath in Path(data_dir).rglob("*"):
    if filepath.suffix.lower() in image_extensions:
        img_type = imghdr.what(filepath)
        if img_type is None:
            print(f"{filepath} is not an image")
        elif img_type not in img_type_accepted_by_tf:
            print(f"{filepath} is a {img_type}, not accepted by TensorFlow")