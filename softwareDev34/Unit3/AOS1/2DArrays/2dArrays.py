import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marks Average")

        self.targetLabel = ttk.Label(self.root, text="Enter a student to find average:")
        self.targetLabel.place(x=300, y=25, anchor='center')
        self.targetEntry = ttk.Entry(self.root, width=30)
        self.targetEntry.place(x=300, y=50, anchor='center')

        self.searchButton = ttk.Button(self.root, text="Search", command=self.search_name)
        self.searchButton.place(x=300, y=75, anchor='center')
        
        self.root.geometry("600x250")
        
        self.data = []
        with open('softwareDev34/Unit3/AOS1/marks.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                self.data.append(row)
        
        print(self.data)

    def search_name(self):
        targetName = self.targetEntry.get()
        names = []
        with open('softwareDev34/Unit3/AOS1/names.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                names.append(row[0])
                
        index = names.index(targetName) if targetName in names else -1

        if index != -1:
            marks = self.data[index]
            marks = [int(mark.strip()) for mark in marks]
            average = sum(marks) / len(marks)
            messagebox.showinfo("Result", f"{targetName}'s average mark is {average:.2f}.")
        else:
            messagebox.showinfo("Result", f"Student {targetName} not found.")

        
        
 


app = tk.Tk()
app_instance = App(app)
app.mainloop() 