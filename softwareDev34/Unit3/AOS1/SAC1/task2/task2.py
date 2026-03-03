"""Book Search GUI.

Input: title (str) from GUI entry; CSV with five rows (lists of str).
Process: read rows, linear-search `titles` for exact matches.
Output: shows tkinter messageboxes for matches; returns None.
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox


class App:
    """Book Search GUI window.

    `root`: tkinter.Tk
    CSV rows used as lists of strings.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("App")
        self.root.geometry("600x250")

        self.bookSearchTitle = ttk.Label(self.root, text="Book Search")
        self.bookSearchTitle.place(x=150, y=65, anchor='center')

        self.bookTitle = ttk.Label(self.root, text="Book Title")
        self.bookTitle.place(x=150, y=90, anchor='center')

        self.bookTitleEntry = ttk.Entry(self.root)
        self.bookTitleEntry.place(x=300, y=90, anchor='center')

        self.searchButton = ttk.Button(self.root, text="Search", command=self.buttonCommand)
        self.searchButton.place(x=300, y=120, anchor='center')
    
    def buttonCommand(self):
                """Search CSV for exact matches to the entered title.

                Input: title (str) from the entry.
                Process: read five CSV rows (lists of str) and linear-search titles.
                Output: shows a messagebox per match; if none, shows a "not found" message.
                Returns: None
                """
                strBookTitleToFind = self.bookTitleEntry.get()

                with open('softwareDev34/Unit3/AOS1/SAC1/task2/books.csv', newline='') as f:
                        reader = csv.reader(f, skipinitialspace=True)
                        self.booksName = next(reader)
                        self.authors = next(reader)
                        self.copiesAvailable = next(reader)
                        self.availability = next(reader)
                        self.location = next(reader)

                found = False
                for i in range(len(self.booksName)):
                        if self.booksName[i] == strBookTitleToFind:
                                messagebox.showinfo("Book Found", f"Correct title, the book should be in {self.location[i]}. According to the records the book is {self.availability[i]} to borrow.")
                                found = True

                if not found:
                        messagebox.showinfo("", f"Please enter the correct title")

        



# Create an object of the App class and start the main event loop to run the application.
app = tk.Tk()
app_instance = App(app)
app.mainloop()