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

        self.entry = ttk.Entry(self.root)
        self.entry.place(x=250, y=65, anchor='center')

        

        self.button = ttk.Button(self.root, text="Button", command=self.buttonCommand)
        self.button.place(x=300, y=185, anchor='center')


    
    def buttonCommand(self):
        messagebox.showerror("Error", "Error message")

        print('Entry field value:', self.entry.get())

        #Access csv per row
        with open('softwareDev34/Unit3/AOS1/practiceSACs/members.csv', newline='') as f:
            reader = csv.reader(f, skipinitialspace=True)
            self.memberIDs = next(reader)          
            self.firstNames = next(reader)
            self.lastNames = next(reader)
            self.dateOfBirths = next(reader)

         


        

# Create an object of the CoffeeApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = App(app)
app.mainloop()