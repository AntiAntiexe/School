# Imprts
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox
from datetime import date
from tkinter import StringVar, IntVar


# Class for HospitalApp which contains methods to initialize the GUI and calculate the eligibility of a member based on their age.
class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital App")
        self.root.geometry("600x250")

        self.title = ttk.Label(self.root, text="Book an Appointment")
        self.title.place(x=300, y=25, anchor='center')

        self.nameLabel = ttk.Label(self.root, text="Name")
        self.nameLabel.place(x=150, y=65, anchor='center')

        self.nameEntry = ttk.Entry(self.root)
        self.nameEntry.place(x=250, y=65, anchor='center')

        self.ageLabel = ttk.Label(self.root, text="Age")
        self.ageLabel.place(x=150, y=100, anchor='center')
        self.ageEntry = ttk.Entry(self.root)
        self.ageEntry.place(x=250, y=100, anchor='center')

        doctors = ["Dr Smith", "Dr Patel", "Dr Nguyen"]

        opt = StringVar(value = doctors[0])

        self.doctorLabel = ttk.Label(self.root, text="Doctor")
        self.doctorLabel.place(x=150, y=135, anchor='center')
        self.optionMenu = ttk.OptionMenu(self.root, opt, *doctors)
        self.optionMenu.place(x=250, y=135, anchor='center')

        self.ch1 = IntVar()
        self.ch2 = IntVar()
        self.ch3 = IntVar()
        self.ch4 = IntVar()


        self.sicknessLabel = ttk.Label(self.root, text="Symptoms")
        self.sicknessLabel.place(x=400, y=65, anchor='center')

        self.feverCheck = ttk.Checkbutton(self.root, text="Fever", variable=self.ch1)
        self.feverCheck.place(x=400, y=90, anchor='center')
        self.headacheCheck = ttk.Checkbutton(self.root, text="Headache", variable=self.ch2)
        self.headacheCheck.place(x=400, y=115, anchor='center')
        self.coughCheck = ttk.Checkbutton(self.root, text="Cough", variable=self.ch3)
        self.coughCheck.place(x=400, y=140, anchor='center')
        self.stomachPainCheck = ttk.Checkbutton(self.root, text="Stomach Pain", variable=self.ch4)
        self.stomachPainCheck.place(x=400, y=165, anchor='center')

        

        self.confirmButton = ttk.Button(self.root, text="Confirm Appointment", command=self.showSummary)
        self.confirmButton.place(x=300, y=185, anchor='center')



    # Takes the memberID (string) from the entry field and checks if it exists in the list of member IDs.
    # If the member exists, it checks if their age (integer) is greater than 18 and displays an appropriate message.
    # If the member does not exist, it displays an error message.
    def showSummary(self):
        if not self.ageEntry.get().isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number for age.")
            return
        elif int(self.ageEntry.get()) < 0:
            messagebox.showerror("Invalid Input", "Please enter a non-negative number for age.")
            return
        
        if self.ch1.get() == 0 and self.ch2.get() == 0 and self.ch3.get() == 0 and self.ch4.get() == 0:
            messagebox.showerror("Invalid Input", "Please select at least one symptom.")
            return
        
        print(self.ch1.get(), self.ch2.get(), self.ch3.get(), self.ch4.get())
        
        symptoms = []
        if self.ch1.get() == 1:
            symptoms.append("Fever")
        if self.ch2.get() == 1:
            symptoms.append("Headache")
        if self.ch3.get() == 1:
            symptoms.append("Cough")
        if self.ch4.get() == 1:
            symptoms.append("Stomach Pain")

        messagebox.showinfo("Appointment Confirmed", f"Name: {self.nameEntry.get()}\nDoctor: {self.optionMenu['text']}\nType: Specialist\nSymptoms: {', '.join(symptoms)}")
        
        

# Create an object of the HospitalApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = HospitalApp(app)
app.mainloop()