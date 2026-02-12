
# Imprts
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox


# Class for Coffee Application which contains methods to initialize the GUI and calculate the total cost of the coffee order based on user input and selected options.
class CoffeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Shop")
        self.root.geometry("600x250")

        self.title = ttk.Label(self.root, text="Coffee Application")
        self.title.place(x=300, y=25, anchor='center')

        self.smallLabel = ttk.Label(self.root, text="Small Coffee")
        self.smallLabel.place(x=150, y=65, anchor='center')

        self.smallEntry = ttk.Entry(self.root)
        self.smallEntry.place(x=250, y=65, anchor='center')

        self.mediumLabel = ttk.Label(self.root, text="Medium Coffee")
        self.mediumLabel.place(x=150, y=95, anchor='center')
        self.mediumEntry = ttk.Entry(self.root)
        self.mediumEntry.place(x=250, y=95, anchor='center')

        self.largeLabel = ttk.Label(self.root, text="Large Coffee")
        self.largeLabel.place(x=150, y=125, anchor='center')
        self.largeEntry = ttk.Entry(self.root)
        self.largeEntry.place(x=250, y=125, anchor='center')


        self.seniorLabel = ttk.Label(self.root, text="Senior Card")
        self.seniorLabel.place(x=450, y=45, anchor='center')
        self.seniorRadioButton= ttk.Radiobutton(self.root, text="Yes", value=1)
        self.seniorRadioButton.place(x=450, y=75, anchor='center')
        self.seniorRadioButton2 = ttk.Radiobutton(self.root, text="No", value=0)
        self.seniorRadioButton2.place(x=450, y=105, anchor='center')
        

        self.calculateButton = ttk.Button(self.root, text="Calculate Total Cost", command=self.calculateTotal)
        self.calculateButton.place(x=300, y=185, anchor='center')


    # Takes the numerical integer values from the entry fields for small, medium and large coffee.
    # Checks boolean variable for the radio button to determine if the user has a senior card and applies a 10% discount if they do.
    # Calculates the total cost of the coffee order and applies a discount of $2 for every 5 coffees ordered.
    def calculateTotal(self):
        if not self.smallEntry.get().isdigit() or not self.mediumEntry.get().isdigit() or not self.largeEntry.get().isdigit():
            messagebox.showerror("Invalid Input", "Please enter valid numbers for coffee quantities.")
        elif int(self.smallEntry.get()) < 0 or int(self.mediumEntry.get()) < 0 or int(self.largeEntry.get()) < 0:
            messagebox.showerror("Invalid Input", "Please enter non-negative numbers for coffee quantities.")
        elif int(self.smallEntry.get()) > 8:
            messagebox.showerror("Invalid Input", "You cannot order more than 8 small coffees.")
        else:

        
            smalls = int(self.smallEntry.get())
            mediums = int(self.mediumEntry.get())
            larges = int(self.largeEntry.get())

            totalCost = (smalls * 2.5) + (mediums * 3.5) + (larges * 4.8)
            if not self.seniorRadioButton.instate(['selected']) and not self.seniorRadioButton2.instate(['selected']):
                discount = totalCost * 0.1
                totalCost -= discount
            if self.seniorRadioButton.instate(['selected']):
                discount = totalCost * 0.1
                totalCost -= discount
            
        
            totalCoffees = smalls + mediums + larges

            fiveCoffeeDiscount = (totalCoffees//5) *2

            print(fiveCoffeeDiscount)

            totalCost -= fiveCoffeeDiscount

            self.answerLabel = ttk.Label(self.root, text=f"Total Cost: ${totalCost:.2f}")
            self.answerLabel.place(x=300, y=150, anchor='center')

# Create an object of the CoffeeApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = CoffeeApp(app)
app.mainloop()