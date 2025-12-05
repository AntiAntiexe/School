import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marks Entry")

        self.targetLabel = ttk.Label(self.root, text="Enter a number to search:")
        self.targetLabel.place(x=300, y=25, anchor='center')
        self.targetEntry = ttk.Entry(self.root, width=30)
        self.targetEntry.place(x=300, y=50, anchor='center')

        self.searchButton = ttk.Button(self.root, text="Search", command=self.search_number)
        self.searchButton.place(x=300, y=75, anchor='center')
        
        self.root.geometry("600x250")
        
        data = []
        with open('softwareDev34/Unit3/AOS1/numbers.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        
        self.arr= [c[0] for c in data]

        self.arr.sort(key=int)

    def search_number(self):
        
 
        numExists = False
        Low = 0
        High = len(self.arr) - 1

        while numExists == False and Low <= High:
            
            Mid = (Low + High) // 2
            print(f"Low: {Low}, High: {High}, Mid: {Mid}, Checking: {self.arr[Mid]}")
            
            if int(self.arr[Mid]) == int(self.targetEntry.get()):
                numExists = True
            elif int(self.arr[Mid]) > int(self.targetEntry.get()):
                High = Mid - 1
            else:
                Low = Mid + 1
        
        
        if numExists:
            messagebox.showinfo("Result", f"Number {self.targetEntry.get()} found in the list at index {Mid}.")
        else:
            messagebox.showinfo("Result", f"Number {self.targetEntry.get()} not found in the list.")


app = tk.Tk()
app_instance = App(app)
app.mainloop() 