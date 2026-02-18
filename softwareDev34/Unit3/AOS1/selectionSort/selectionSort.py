import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Selection Sort")

        self.searchButton = ttk.Button(self.root, text="Sort", command=self.sortNumbers)
        self.searchButton.place(x=300, y=75, anchor='center')
        
        self.root.geometry("600x250")
        
        data = []
        with open('softwareDev34/Unit3/AOS1/numbersSort.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        
        self.arr= [c[0] for c in data]

        self.arr.sort(key=int)

    def sortNumbers(self):
        n = len(self.arr)
 
        for i in range(n-2):
            minIndx = i

            for j in range(i+1, n-1):
                if self.arr[j] >= self.arr[minIndx]:
                    minIndx = j
        self.arr[i], self.arr[minIndx] = self.arr[minIndx], self.arr[i]


        self.searchButton.place_forget()

        self.label = ttk.Label(self.root, text=f"Sorted Numbers: {', '.join(self.arr)}")
        self.label.place(x=300, y=100, anchor='center')


app = tk.Tk()
app_instance = App(app)
app.mainloop()