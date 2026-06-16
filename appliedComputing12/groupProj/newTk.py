from tkinter import *
from PIL import ImageTk, Image

# Create the main window
root = Tk()
root.title("Black Background Label")
root.geometry("800x600")

filename = '/Users/home/Downloads/MANGOES-R2E2.jpg'

img = Image.open(filename)
img = ImageTk.PhotoImage(img)
            
my_label = Label(root, image=img)
my_label.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()