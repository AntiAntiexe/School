# Imprts
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox
from datetime import date
from tkinter import StringVar, IntVar


# Class for HospitalApp which contains methods to initialize the GUI and calculate the eligibility of a member based on their age.
class SubjectSelection:
    def __init__(self, root):
        self.root = root
        self.root.title("Subject Selection")
        self.root.geometry("600x250")

        self.title = ttk.Label(self.root, text="Select Your Subjects")
        self.title.place(x=300, y=25, anchor='center')

        self.nameLabel = ttk.Label(self.root, text="Name")
        self.nameLabel.place(x=150, y=65, anchor='center')

        self.nameEntry = ttk.Entry(self.root)
        self.nameEntry.place(x=250, y=65, anchor='center')

        self.var = IntVar()


        self.yr10Radio = ttk.Radiobutton(self.root, text="Year 10", variable=self.var, value=1)
        self.yr10Radio.place(x=150, y=100, anchor='center')

        self.yr11Radio = ttk.Radiobutton(self.root, text="Year 11", variable=self.var, value=2)
        self.yr11Radio.place(x=250, y=100, anchor='center')

        self.yr12Radio = ttk.Radiobutton(self.root, text="Year 12", variable=self.var, value=3)
        self.yr12Radio.place(x=350, y=100, anchor='center')

        self.methodsCh = IntVar()
        self.specCh = IntVar()
        self.physicsCh = IntVar()
        self.chemCh = IntVar()
        self.softCh = IntVar()


        self.subjectsLabel = ttk.Label(self.root, text="Subjects")
        self.subjectsLabel.place(x=150, y=135, anchor='center')

        self.methodsCheck = ttk.Checkbutton(self.root, text="Methods", variable=self.methodsCh)
        self.methodsCheck.place(x=175, y=135, anchor='w')
        self.specCheck = ttk.Checkbutton(self.root, text="Specialist", variable=self.specCh)
        self.specCheck.place(x=250, y=135, anchor='w')
        self.physicsCheck = ttk.Checkbutton(self.root, text="Physics", variable=self.physicsCh)
        self.physicsCheck.place(x=325, y=135, anchor='w')
        self.chemCheck = ttk.Checkbutton(self.root, text="Chemistry", variable=self.chemCh)
        self.chemCheck.place(x=175, y=160, anchor='w')
        self.softwareCheck = ttk.Checkbutton(self.root, text="Software Development", variable=self.softCh)
        self.softwareCheck.place(x=275, y=160, anchor='w')

        careers = ["Engineering", "Medicine", "IT", "Business", "Arts"]

        opt = StringVar(value = careers[0])

        self.careerLabel = ttk.Label(self.root, text="Career Interest")
        self.careerLabel.place(x=150, y=200, anchor='center')
        self.optionMenu = ttk.OptionMenu(self.root, opt, *careers)
        self.optionMenu.place(x=250, y=200, anchor='center')

        
        self.confirmButton = ttk.Button(self.root, text="Check Eligibility", command=self.checkElig)
        self.confirmButton.place(x=300, y=220, anchor='center')



    # Takes the memberID (string) from the entry field and checks if it exists in the list of member IDs.
    # If the member exists, it checks if their age (integer) is greater than 18 and displays an appropriate message.
    # If the member does not exist, it displays an error message.
    def checkElig(self):
        if self.methodsCh.get() == 1 and self.specCh.get() != 1 or self.specCh.get() == 1 and self.methodsCh.get() != 1:
            messagebox.showerror("Ineligible", "To take Specialist Maths, you must also take Methods.")
        elif self.optionMenu['text'] == 'Medicine' and self.chemCh.get() != 1:
            messagebox.showwarning("Warning", "To pursue Medicine, it is recommended that you take Chemistry.")
       
        

# Create an object of the HospitalApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = SubjectSelection(app)
app.mainloop()