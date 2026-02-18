# Imprts
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox


# Class for Coffee Application which contains methods to initialize the GUI and calculate the total cost of the coffee order based on user input and selected options.
class CoffeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Export")
        self.root.geometry("600x250")

        self.firstNameLabel = ttk.Label(self.root, text="First Name")
        self.firstNameLabel.place(x=20, y=20, anchor='nw')
        self.firstNameEntry = ttk.Entry(self.root)
        self.firstNameEntry.place(x=110, y=17.5, anchor='nw')

        self.lastNameLabel = ttk.Label(self.root, text="Last Name")
        self.lastNameLabel.place(x=20, y=40, anchor='nw')
        self.lastNameEntry = ttk.Entry(self.root)
        self.lastNameEntry.place(x=110, y=40, anchor='nw')

        self.hoursLabel = ttk.Label(self.root, text="Hours Worked")
        self.hoursLabel.place(x=20, y=60, anchor='nw')
        self.hoursEntry = ttk.Entry(self.root)
        self.hoursEntry.place(x=110, y=62.5, anchor='nw')

        self.registerButton = ttk.Button(self.root, text="Register", command=self.register)
        self.registerButton.place(x=110, y=90, anchor='nw')

        self.fieldNames = ["First Name", "Last Name", "Hours Worked", "Weekly Pay"]


    
    def register(self):

        if not self.firstNameEntry.get() or not self.lastNameEntry.get() or not self.hoursEntry.get():
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        elif not self.hoursEntry.get().isdigit():
            messagebox.showerror("Error", "Please enter a valid number for hours worked.")
            return     
        elif float(self.hoursEntry.get()) < 0:
            messagebox.showerror("Error", "Please enter a positive number for hours worked.")
            return
        
        

        field_names = self.fieldNames
        weeklypay = (float(self.hoursEntry.get()) * 0.3) + 1500

        data = {
            "First Name": self.firstNameEntry.get(),
            "Last Name": self.lastNameEntry.get(),
            "Hours Worked": self.hoursEntry.get(),
            "Weekly Pay": weeklypay
        }

        with open('/Users/anton/Programming/pythonProjects/School/softwareDev34/Unit3/AOS1/register.csv', 'a', newline='') as f_objects:
            dictWriter_object = csv.DictWriter(f_objects, fieldnames=field_names)

            dictWriter_object.writerow(data)
            f_objects.close()
        
        answerLabel = ttk.Label(self.root, text=f"The weekly salary of {self.firstNameEntry.get()} {self.lastNameEntry.get()} is ${weeklypay:.2f}.")
        answerLabel.place(x=20, y=120, anchor='nw')

    

# Create an object of the CoffeeApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = CoffeeApp(app)
app.mainloop()