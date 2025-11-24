import tkinter as tk
from tkinter import messagebox, ttk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marks Entry")
        
        self.root.geometry("600x250")
        
        
        self.StudentNameLabel = ttk.Label(self.root, text="Student Name:")
        self.StudentNameLabel.place(x=300, y=25, anchor='center')
        self.StudentNameEntry = ttk.Entry(self.root, width=30)
        self.StudentNameEntry.place(x=300, y=50, anchor='center')
        
        self.ageLabel = ttk.Label(self.root, text="Age:")
        self.ageLabel.place(x=300, y=75, anchor='center')
        self.ageEntry = ttk.Entry(self.root, width=30)
        self.ageEntry.place(x=300, y=100, anchor='center')
        
        self.marksLabel = ttk.Label(self.root, text="Marks:")
        self.marksLabel.place(x=300, y=125, anchor='center')
        self.marksEntry = ttk.Entry(self.root, width=30)
        self.marksEntry.place(x=300, y=150, anchor='center')
        
        self.submitButton = ttk.Button(self.root, text="Submit", command=self.submit_info)
        self.submitButton.place(x=300, y=175, anchor='center')
        
    def submit_info(self):
        name = self.StudentNameEntry.get()
        age = self.ageEntry.get()
        marks = self.marksEntry.get()
        
        if name == "" or age == "" or marks == "":
            messagebox.showwarning("Error", "All fields must be filled in.")
        elif not age.isdigit():
            messagebox.showwarning("Error", "Age must be a numeric.")
        elif not marks.isdigit():
            messagebox.showwarning("Error", "Marks must be a numeric.")
        elif int(marks) < 0 or int(marks) > 100:
            messagebox.showwarning("Error", "Marks must be between 0 and 100.")
        elif int(age) < 5 or int(age) > 20:
            messagebox.showwarning("Error", "Age must be between 5 and 20.")
        else:
            messagebox.showinfo("Success", f"Record saved: \nName: {name}\nAge: {age}\nMarks: {marks}")

app = tk.Tk()
app_instance = App(app)
app.mainloop()