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

        self.var = IntVar()

        self.radio1= ttk.Radiobutton(self.root, text="Yes",variable=self.var, value=1)
        self.radio1.place(x=450, y=75, anchor='center')
        self.radio2 = ttk.Radiobutton(self.root, text="No", variable=self.var, value=0)
        self.radio2.place(x=450, y=105, anchor='center')

        self.var.set(0) #default value for the radio button is set to "No"

        self.ch1 = IntVar()
        self.ch2 = IntVar()
        self.ch3 = IntVar()

        self.chButton1 = ttk.Checkbutton(self.root, text="ch1", variable=self.ch1)
        self.chButton1.place(x=175, y=100, anchor='w')
        self.chButton2 = ttk.Checkbutton(self.root, text="ch2", variable=self.ch2)
        self.chButton2.place(x=250, y=100, anchor='w')
        self.chButton3 = ttk.Checkbutton(self.root, text="ch3", variable=self.ch3)
        self.chButton3.place(x=325, y=100, anchor='w')

        options = ["Option1", "Option2", "Option3", "Option4", "Option5"]

        opt = StringVar(value = options[0]) #default value for the option menu is set to the first option in the list

        self.optionMenu = ttk.OptionMenu(self.root, opt, *options)
        self.optionMenu.place(x=250, y=150, anchor='center')
        

        self.button = ttk.Button(self.root, text="Button", command=self.buttonCommand)
        self.button.place(x=300, y=185, anchor='center')


    # Takes the numerical integer values from the entry fields for small, medium and large coffee.
    # Checks boolean variable for the radio button to determine if the user has a senior card and applies a 10% discount if they do.
    # Calculates the total cost of the coffee order and applies a discount of $2 for every 5 coffees ordered.
    def buttonCommand(self):
        messagebox.showerror("Error", "Error message")

        print('Entry field value:', self.entry.get())
        if self.var.get() == 1:
            print('Radio button value: Yes')
        elif self.var.get() == 0:
            print('Radio button value: No')
        
        if self.ch1.get() == 1:
            print('Checkbutton 1 is selected')
        if self.ch2.get() == 1:
            print('Checkbutton 2 is selected')
        if self.ch3.get() == 1:
            print('Checkbutton 3 is selected')

        print('Selected option:', self.optionMenu['text'])

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