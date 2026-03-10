# Imports
import tkinter as tk
from tkinter import ttk, messagebox
import csv


class Student:
    """Represents a single student's record."""

    def __init__(
        self,
        student_id: str,
        surname: str,
        given_name: str,
        maths: str,
        science: str,
        english: str,
    ):
        # store IDs in a consistent uppercase form for searching/sorting
        self.student_id = student_id.strip().upper()
        self.surname = surname
        self.given_name = given_name
        self.maths = int(maths)
        self.science = int(science)
        self.english = int(english)

    def weighted_average(self):
        """Return the weighted average rounded to the nearest integer.

        formula: (2*Maths + 2*Science + 3*English) / 7
        """
        return round((2 * self.maths + 2 * self.science + 3 * self.english) / 7)


def load_students(filepath):
    """Load student records from a CSV file and return a sorted list by ID.

    The file is expected to be comma-separated with the following columns in
    this order:

        StudentID, Surname, GivenName, MathsScore, ScienceScore, EnglishScore

    """

    students = []
    with open(filepath, newline="") as file:
        reader = csv.reader(file)
        first = next(reader, None)
        if first and first[0].lower().startswith("studentid"):
            pass
        elif first:
            students.append(Student(*first))

        for row in reader:
            if not row:
                continue
            students.append(Student(*row))

    students.sort(key=lambda s: s.student_id)
    return students


def binary_search(students, target: str):
    """Perform a binary search on the sorted list of students.
    Input: is the target in the form of a student ID string, e.g. "CAL1202".
    Process: Uses binary search to find the student with the matching ID.
    Output: Returns the matching Student object if found, otherwise None.

    Comparison is case‑insensitive; the `Student` objects keep their IDs
    uppercased already, so the target is normalized too.
    """

    target = target.strip().upper()
    intMin = 0
    intMax = len(students) - 1
    while intMin <= intMax:
        intMid = (intMin + intMax) // 2
        mid_id = students[intMid].student_id
        if mid_id == target:
            return students[intMid]
        if mid_id > target:
            intMax = intMid - 1
        else:
            intMin = intMid + 1
    return None


class App:
    """Simple GUI for looking up students by ID."""

    def __init__(self, root, datafile = "students.csv"):
        self.root = root
        self.root.title("Waverley College Student Lookup")
        self.root.geometry("500x200")

        ttk.Label(root, text="Student Search").pack(pady=10)
        label = ttk.Label(root, text="Student ID")
        label.place(x=150, y=50, anchor="center")

        self.entry = ttk.Entry(root)
        self.entry.place(x=250, y=50, anchor="w")

        button = ttk.Button(root, text="Search", command=self.on_find)
        button.place(x=250, y=90, anchor="center")

        
        # load the student records once; the list will be sorted inside the loader
        self.students = load_students(datafile)

    def on_find(self):
        sid = self.entry.get().strip().upper()
        
        student = binary_search(self.students, sid)
        if student:
            name = f"{student.given_name} {student.surname}"
            intWeightedScore = student.weighted_average()
            messagebox.showinfo("Student Found", f"The weighted score of {name} is {intWeightedScore}")
        else:
            messagebox.showwarning("Not found", "Student not found.")



root = tk.Tk()
app = App(root)
root.mainloop()


'''
QUESTION 3: Explain on limitation of binary search with referenc to the design.
One limitation of binary search is that it requires the data to be sorted, before the search algorithm can be applied.
This means that the list of students is sorted by their StudentID before binary search. 
If the data is not sorted, the binary search algorithm will not function correctly the search algorithm will give an incorrect result.
This adds an additional step in our design where we need to sort the data after loading it from the CSV file, which can increase the complexity and runtime of our application, especially if the dataset is large.

'''