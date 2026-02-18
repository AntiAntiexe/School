import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marks Average")

        self.students_data = [
            ["Amy", 23, 30, 25, 26],
            ["Bob", 20, 22, 19, 24],
            ["Cathy", 30, 29, 31, 28],
            ["David", 25, 27, 26, 24]
        ]

        self.targetLabel = ttk.Label(self.root, text="Enter a student to find average:")
        self.targetLabel.place(x=300, y=25, anchor='center')
        self.targetEntry = ttk.Entry(self.root, width=30)
        self.targetEntry.place(x=300, y=50, anchor='center')

        self.searchButton = ttk.Button(self.root, text="Search", command=self.search_name)
        self.searchButton.place(x=300, y=75, anchor='center')

        self.avgLabel = ttk.Label(self.root, text=f"Average for {self.targetEntry.get()}:")
        #self.avgLabel.place(x=300, y=100, anchor='center')
        
        self.root.geometry("600x250")
        
        

    def search_name(self):

        
        for i in self.students_data:
            if i[0] == self.targetEntry.get():
                total = 0
                for j in range(1, len(i)):
                    total += i[j]

                average = total / (len(i) - 1)

                self.avgLabel.config(text=f"Average for {self.targetEntry.get()}: {average:.2f}")
                self.avgLabel.place(x=300, y=100, anchor='center')

                

                


                
app = tk.Tk()
app_instance = App(app)
app.mainloop() 