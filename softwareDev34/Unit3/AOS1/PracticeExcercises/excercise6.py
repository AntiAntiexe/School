
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

        self.v = tk.IntVar()
        

        options = [("Weekly", 0), ("Monthly", 1), ("Annually", 2)]

        for option, val in options:
            ttk.Radiobutton(self.root, text=option, variable=self.v, value=val).place(x=150 + options.index((option, val))*100, y=95, anchor='center')
        
        self.calculateButton = ttk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculateButton.place(x=150, y=135, anchor='center')

        self.v.set(0)


        
    def calculate(self):
        if self.feeEntry.get().isnumeric() and int(self.feeEntry.get()) > 0:
            fee = float(self.feeEntry.get())
            value = self.v.get()

            if value == 0:
                total_cost = fee/52
                self.answer = f"The total cost of the school fee is: ${total_cost:.2f} per week."
            elif value == 1:
                total_cost = fee/12
                self.answer = f"The total cost of the school fee is: ${total_cost:.2f} per month."
            elif value == 2:
                total_cost = fee
                self.answer = f"The total cost of the school fee is: ${total_cost:.2f} per year."
            
            answer = ttk.Label(self.root, text=self.answer)
            answer.place(x=350, y=135, anchor='center')
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for the school fee.")

        

# Create an object of the CoffeeApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = SchoolFeeApp(app)
app.mainloop()