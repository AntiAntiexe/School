
# Imprts
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox


# Class for School Fee Application which contains methods to initialize the GUI and calculate the total cost of the school fee based on user input and selected options.
class SchoolFeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("School Fee Calculator")
        self.root.geometry("600x250")

        self.feeLabel = ttk.Label(self.root, text="Enter school fee")
        self.feeLabel.place(x=150, y=45, anchor='center')

        self.feeEntry = ttk.Entry(self.root)
        self.feeEntry.place(x=350, y=45, anchor='center')

        v = tk.IntVar()
        

        options = [("Weekly", 0), ("Monthly", 1), ("Annually", 2)]

        for option, val in options:
            ttk.Radiobutton(self.root, text=option, variable=v, value=val).place(x=150 + options.index((option, val))*100, y=95, anchor='center')
        
        self.calculateButton = ttk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculateButton.place(x=150, y=135, anchor='center')

        v.set(0)


        """
        self.radioButton = ttk.Radiobutton(self.root, text="Weekly", value=0, variable=myVar)
        self.radioButton.place(x=150, y=95, anchor='center')
        self.radioButton2 = ttk.Radiobutton(self.root, text="Monthly", value=1, variable=myVar)
        self.radioButton2.place(x=250, y=95, anchor='center')
        self.radioButton3 = ttk.Radiobutton(self.root, text="Annually", value=2, variable=myVar)
        self.radioButton3.place(x=350, y=95, anchor='center')"""
        

        

        

        


    def calculate(self):
        pass

# Create an object of the CoffeeApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = SchoolFeeApp(app)
app.mainloop()