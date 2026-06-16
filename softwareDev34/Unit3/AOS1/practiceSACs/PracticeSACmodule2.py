# Imprts
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox
from datetime import date


# SherrinGlenApp: simple GUI to check a member's eligibility for 'P'.
# Attributes: root (tk.Tk), memberIDs/list[str], firstNames/list[str],
# lastNames/list[str], dateOfBirths/list[str]
class SherrinGlenApp:
    def __init__(self, root):
        """Initialize GUI and load member CSV.

        Input: root (tk.Tk)
        Output: None (widgets created; member lists populated)
        """
        self.root = root
        self.root.title("Sherrin Glen")
        self.root.geometry("600x250")

        self.title = ttk.Label(self.root, text="Sherrin Glen")
        self.title.place(x=300, y=25, anchor='center')

        self.memberLable = ttk.Label(self.root, text="Member ID")
        self.memberLable.place(x=150, y=65, anchor='center')

        self.memberIdLabel = ttk.Entry(self.root)
        self.memberIdLabel.place(x=250, y=65, anchor='center')


        self.eligibilityButton = ttk.Button(self.root, text="Eligibility for P", command=self.calculateElig)
        self.eligibilityButton.place(x=300, y=100, anchor='center')

        with open('softwareDev34/Unit3/AOS1/practiceSACs/members.csv', newline='') as f:
            reader = csv.reader(f, skipinitialspace=True)
            self.memberIDs = next(reader)          
            self.firstNames = next(reader)
            self.lastNames = next(reader)
            self.dateOfBirths = next(reader)


     # Check entered member ID and show eligibility message.
    def calculateElig(self):
        """Find ID, compare DOB to cutoff, and show result via messagebox.

          Inputs (used): memberId (str from entry), member lists (list[str]).
          Output: None (messagebox shown).
        """
        found = False
        for i in range(len(self.memberIDs)):
            if self.memberIDs[i] == self.memberIdLabel.get():
                if str(self.dateOfBirths[i]) <= "2008-2-26":
                    messagebox.showinfo("",f"{self.lastNames[i]} {self.firstNames[i]} is eligible.")
                    found = True
                    break
                else:
                    messagebox.showinfo("",f"{self.lastNames[i]} {self.firstNames[i]} is not eligible.")
                    found = True
                    break
        if found == False:
            messagebox.showinfo("Error", "This member is not registered with us.")


        

# Create an object of the SherrinGlenApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = SherrinGlenApp(app)
app.mainloop()