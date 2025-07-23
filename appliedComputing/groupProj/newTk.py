import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Black Background Label")

# Create a Label with a black background and white text
label = ttk.Label(root, text="This is a label on a black background", background="black", foreground="white")
label.pack(pady=20, padx=20) # Add some padding

# Run the Tkinter event loop
root.mainloop()