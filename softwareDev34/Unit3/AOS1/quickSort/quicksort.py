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

        self.label = ttk.Label(self.root, text="Quick Sort")
        self.label.place(x=300, y=65, anchor='center')

        

        self.button = ttk.Button(self.root, text="Sort", command=self.run)
        self.button.place(x=300, y=185, anchor='center')

        data = []
        with open('softwareDev34/Unit3/AOS1/quickSort/quickSortData.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)

        self.arr= [int(c[0]) for c in data]

        print(self.arr)
    
    # partition function
    # partition function
    def partition(self, low, high):
        
        # choose the pivot
        pivot = self.arr[high]
        
        # index of smaller element and indicates 
        # the right position of pivot found so far
        i = low - 1
        
        # traverse arr[low..high] and move all smaller
        # elements to the left side. Elements from low to 
        # i are smaller after every iteration
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.swap(i, j)
        
        # move pivot after smaller elements and
        # return its position
        self.swap(i + 1, high)
        return i + 1

    # swap function
    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    # the QuickSort function implementation
    def quickSort(self, low, high):
        if low < high:
            
            # pi is the partition return index of pivot
            pi = self.partition(low, high)
            
            # recursion calls for smaller elements
            # and greater or equals elements
            self.quickSort(low, pi - 1)
            self.quickSort(pi + 1, high)

    def run(self):
        arr = self.arr
        n = len(arr)

        self.quickSort(0, n - 1)
    
        for val in arr:
            print(val, end=" ")
        

         


        

# Create an object of the CoffeeApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = App(app)
app.mainloop()

    