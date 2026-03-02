# Imprts
import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox


# Class for Coffee Application which contains methods to initialize the GUI and calculate the total cost of the coffee order based on user input and selected options.
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App")
        self.root.geometry("600x250")

        self.label = ttk.Label(self.root, text="Label")
        self.label.place(x=150, y=65, anchor='center')
    
    def buttonCommand(self):
        pass

# Create an object of the App class and start the main event loop to run the application.
app = tk.Tk()
app_instance = App(app)
app.mainloop()