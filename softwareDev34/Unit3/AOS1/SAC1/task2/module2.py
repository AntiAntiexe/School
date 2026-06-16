"""Book Search GUI.

Purpose:
- Provide a simple GUI to search for book titles in a CSV and display results.

Inputs (external):
- GUI entry `bookTitleEntry`: str (the exact book title to search for)
- CSV file at 'softwareDev34/Unit3/AOS1/SAC1/task2/books.csv' with five rows:
    - titles: list[str]
    - authors: list[str]
    - copiesAvailable: list[str]
    - availability: list[str]
    - location: list[str]

Process:
- Read the five CSV rows into lists of strings.
- Perform a linear search over `titles` for exact string matches.
- For each match, display a messagebox with location and availability.
- If no match, display a "not found" messagebox.

Outputs (side-effects):
- One or more `tkinter.messagebox.showinfo` dialogs are shown. The function
    returns None.
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox


class App:
    """Book Search application window.

    Notes on types:
    - `root`: tkinter.Tk
    - `bookTitleEntry.get()`: str
    - CSV rows are treated as `list[str]`.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("App")
        self.root.geometry("600x250")

        self.bookSearchTitle = ttk.Label(self.root, text="Book Search")
        self.bookSearchTitle.place(x=300, y=65, anchor='center')

        self.bookTitle = ttk.Label(self.root, text="Book Title")
        self.bookTitle.place(x=150, y=90, anchor='center')

        self.bookTitleEntry = ttk.Entry(self.root)
        self.bookTitleEntry.place(x=300, y=90, anchor='center')

        self.searchButton = ttk.Button(self.root, text="Search", command=self.buttonCommand)
        self.searchButton.place(x=300, y=120, anchor='center')
    
    def buttonCommand(self):
                """

                Function:
                - Reads five rows from the CSV file at the hard-coded path and treats each
                    row as a list of strings representing parallel columns.
                - Performs a linear search over the `titles` row for exact `==` matches.

                Input:
                - title (str): obtained from `self.bookTitleEntry.get()`.
                - CSV file rows (list[str]):
                    - titles: list[str]
                    - authors: list[str]
                    - copiesAvailable: list[str]
                    - availability: list[str]
                    - location: list[str]

                Process:
                - Open and read the CSV using `csv.reader` with `skipinitialspace=True`.
                - Use `next(reader)` five times to load rows into lists of strings.
                - Iterate indices and for each index `i` where `titles[i] == title`, show
                    a `messagebox.showinfo` with the location and availability for that
                    index.

                Output:
                - Displays one `messagebox.showinfo` per match with:
                    Title: "Book Found"
                    Message: "Correct title, the book should be in {location[i]}. According to the records the book is {availability[i]} to borrow."
                - If no matches are found, displays an empty-title messagebox with
                    message: "Please enter the correct title".
                """
                strBookTitleToFind = self.bookTitleEntry.get()

                with open('softwareDev34/Unit3/AOS1/SAC1/task2/module2.csv', newline='') as f:
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
                        messagebox.showinfo("Book Not Found", f"Please enter the correct title")

        



# Create an object of the App class and start the main event loop to run the application.
app = tk.Tk()
app_instance = App(app)
app.mainloop()