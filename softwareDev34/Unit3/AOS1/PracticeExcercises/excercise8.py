# Imprts
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox


# Class for School Fee Application which contains methods to initialize the GUI and calculate the total cost of the school fee based on user input and selected options.
class SchoolFeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lowest vs Highest")
        self.root.geometry("600x600")

        self.feeLabel = ttk.Label(self.root, text="Finding the lowest and \n highest numbers", justify=tk.CENTER, font=("Helvetica", 20, 'bold'))
        self.feeLabel.place(x=300, y=45, anchor='center')

        self.num1Label = ttk.Label(self.root, text="Number 1", font=("Helvetica", 17, 'bold'))
        self.num1Label.place(x=100, y=100, anchor='center')

        self.num1Entry = ttk.Entry(self.root, font=("Helvetica", 17))
        self.num1Entry.place(x=250, y=100, anchor='center')

        self.num2Label = ttk.Label(self.root, text="Number 2", font=("Helvetica", 17, 'bold'))
        self.num2Label.place(x=100, y=150, anchor='center')

        self.num2Entry = ttk.Entry(self.root, font=("Helvetica", 17))
        self.num2Entry.place(x=250, y=150, anchor='center')

        self.num3Label = ttk.Label(self.root, text="Number 3", font=("Helvetica", 17, 'bold'))
        self.num3Label.place(x=100, y=200, anchor='center')

        self.num3Entry = ttk.Entry(self.root, font=("Helvetica", 17))
        self.num3Entry.place(x=250, y=200, anchor='center')

        self.num4Label = ttk.Label(self.root, text="Number 4", font=("Helvetica", 17, 'bold'))
        self.num4Label.place(x=100, y=250, anchor='center')

        self.num4Entry = ttk.Entry(self.root, font=("Helvetica", 17))
        self.num4Entry.place(x=250, y=250, anchor='center')

        self.num5Label = ttk.Label(self.root, text="Number 5", font=("Helvetica", 17, 'bold'))
        self.num5Label.place(x=100, y=300, anchor='center')

        self.num5Entry = ttk.Entry(self.root, font=("Helvetica", 17))
        self.num5Entry.place(x=250, y=300, anchor='center')

        self.lowestButton = ttk.Button(self.root, text="Lowest", command=self.calculate_lowest)
        self.lowestButton.place(x=100, y=350, anchor='center')

        self.highestButton = ttk.Button(self.root, text="Highest", command=self.calculate_highest)
        self.highestButton.place(x=100, y=400, anchor='center')

        
    def calculate_lowest(self):
        if not self.num1Entry.get() or not self.num2Entry.get() or not self.num3Entry.get() or not self.num4Entry.get() or not self.num5Entry.get():
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        elif not self.num1Entry.get().isdigit() or not self.num2Entry.get().isdigit() or not self.num3Entry.get().isdigit() or not self.num4Entry.get().isdigit() or not self.num5Entry.get().isdigit():
            messagebox.showerror("Error", "Please enter valid numbers.")
            return
        
        numbers = [float(self.num1Entry.get()), float(self.num2Entry.get()), float(self.num3Entry.get()), float(self.num4Entry.get()), float(self.num5Entry.get())]
         
        min = numbers[0]
        for num in numbers:
            if num < min:
                min = num
        lowestLabel = ttk.Label(self.root, text=f"The lowest number is: {min}", font=("Helvetica", 17, 'bold'))
        lowestLabel.place(x=300, y=350, anchor='center')   

        
    def calculate_highest(self):
        if not self.num1Entry.get() or not self.num2Entry.get() or not self.num3Entry.get() or not self.num4Entry.get() or not self.num5Entry.get():
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        elif not self.num1Entry.get().isdigit() or not self.num2Entry.get().isdigit() or not self.num3Entry.get().isdigit() or not self.num4Entry.get().isdigit() or not self.num5Entry.get().isdigit():
            messagebox.showerror("Error", "Please enter valid numbers.")
            return
        
        numbers = [float(self.num1Entry.get()), float(self.num2Entry.get()), float(self.num3Entry.get()), float(self.num4Entry.get()), float(self.num5Entry.get())]
         
        max = numbers[0]
        for num in numbers:
            if num > max:
                max = num

        highestLabel = ttk.Label(self.root, text=f"The highest number is: {max}", font=("Helvetica", 17, 'bold'))
        highestLabel.place(x=300, y=400, anchor='center')  
        
         
# Create an object of the CoffeeApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = SchoolFeeApp(app)
app.mainloop()