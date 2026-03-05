# Imprts
import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox


# Class for Student Ranking Application
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Ranking System")
        self.root.geometry("600x300")
        
        self.strStudentList = []
        self.load_student_data()
        self.sort_students_by_weighted_score()
        self.titleLabel = ttk.Label(self.root, text="Finding the Student's Rank")
        self.titleLabel.place(x=300, y=30, anchor='center')
        # UI Elements
        self.label = ttk.Label(self.root, text="Enter Student ID:")
        self.label.place(x=200, y=100, anchor='center')

        self.entry = ttk.Entry(self.root)
        self.entry.place(x=400, y=100, anchor='center')

        self.rank_button = ttk.Button(self.root, text="Find Rank", command=self.show_rank)
        self.rank_button.place(x=390, y=200, anchor='center')

        self.score_button = ttk.Button(self.root, text="Find Weighted Score", command=self.show_weighted_score)
        self.score_button.place(x=235, y=200, anchor='center')
        
        self.result_label = ttk.Label(self.root, text="", wraplength=550)
        self.result_label.place(x=300, y=180, anchor='center')

    def load_student_data(self):
        """Load student data from headerless CSV file"""
        self.strStudentList = []
        with open('softwareDev34/Unit3/AOS1/SAC1/task4/module4.csv', 'r', newline='') as file:
            csv_reader = csv.reader(file, skipinitialspace=True)
            for row in csv_reader:
                if len(row) < 6:
                    continue
                student = {
                    'StudentID': row[0].strip(),
                    'GivenName': row[1].strip(),
                    'Surname': row[2].strip(),
                    'MathsScore': int(row[3].strip()),
                    'ScienceScore': int(row[4].strip()),
                    'EnglishScore': int(row[5].strip())
                }
                self.strStudentList.append(student)
    
    def calculate_weighted_score(self, student):
        """
        IPO + Data Types
        Input:
            student (dict[str, str | int])
        Process:
            Computes weighted score:
            (2*Maths + 2*Science + 3*English) / 7, then rounds result.
        Output:
            int (rounded weighted score)
        """
        weighted_score = (2 * student['MathsScore'] + 2 * student['ScienceScore'] + 3 * student['EnglishScore']) / 7
        return round(weighted_score)
    
    def sort_students_by_weighted_score(self):
        """
        Input:
            self.students (list[dict[str, str | int]])
        Process:
            Uses selection sort to order students by weighted score descending.
        Output:
            None (self.students sorted in place)
        """
        n = len(self.strStudentList)
        
        for i in range(n):
            min_idx = i
            
            for j in range(i, n):
                weighted_score_j = self.calculate_weighted_score(self.strStudentList[j])
                weighted_score_min = self.calculate_weighted_score(self.strStudentList[min_idx])
                

                if weighted_score_min < weighted_score_j:
                    min_idx = j

            if min_idx != i:
                self.strStudentList[i], self.strStudentList[min_idx] = self.strStudentList[min_idx], self.strStudentList[i]
    
    def calculate_average_weighted_score(self):
        """
        Input:
            self.students (list[dict[str, str | int]])
        Process:
            Sums all weighted scores and divides by number of students.
        Output:
            int (rounded class average weighted score)
        """
        total_weighted_score = sum(self.calculate_weighted_score(student) for student in self.strStudentList)
        intAverageScore = total_weighted_score / len(self.strStudentList)
        return round(intAverageScore)
    
    def find_student_and_rank(self, student_id):
        """Find student and rank by ID"""
        for rank, student in enumerate(self.strStudentList, start=1):
            if student['StudentID'] == student_id:
                return student, rank
        return None, None

    def show_rank(self):
        """Show only student rank in a message box"""
        student_id = self.entry.get().strip()

        student, rank = self.find_student_and_rank(student_id)
        weighted_score = self.calculate_weighted_score(student)
        average_score = self.calculate_average_weighted_score()
        difference = abs(weighted_score - average_score)

        messagebox.showinfo("Score", f"The rank of {student['Surname']} {student['GivenName']} is {rank}, the student has scored {difference} more than {average_score} which is the Average Score for the class")

    def show_weighted_score(self):
        """Show only student weighted score in a message box"""
        student_id = self.entry.get().strip()

        student, _ = self.find_student_and_rank(student_id)

        intWeightedScore = self.calculate_weighted_score(student)

        messagebox.showinfo("Student Found", f"Weighted Score is {intWeightedScore}")


# Create an object of the App class and start the main event loop to run the application.
app = tk.Tk()
app_instance = App(app)
app.mainloop()