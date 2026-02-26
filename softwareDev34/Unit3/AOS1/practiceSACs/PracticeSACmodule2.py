# Imprts
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox
from datetime import date


# Class for SherrinGlenApp which contains methods to initialize the GUI and calculate the eligibility of a member based on their age.
#
# This class encapsulates the user interface and logic for checking whether a
# Sherrin Glen club member is eligible for "P" based on their date of birth.
#
# Attributes created during initialization:
#   root (tk.Tk)       : Tkinter root window passed in by caller.
#   title (ttk.Label)  : Label widget displaying the app title.
#   memberLable (ttk.Label): Label prompting for Member ID input.
#   memberIdLabel (ttk.Entry): Entry widget where the user types the ID.
#   eligibilityButton (ttk.Button): Button that triggers eligibility check.
#   memberIDs (list[str]): list of member ID strings read from CSV.
#   firstNames (list[str]): corresponding first names from CSV.
#   lastNames (list[str]): corresponding last names from CSV.
#   dateOfBirths (list[str]): dates of birth read as YYYY-M-D strings.
class SherrinGlenApp:
    def __init__(self, root):
        """Initialize the GUI and load member data.

        Parameters
        ----------
        root : tk.Tk
            The Tkinter root window object where the application will be mounted.

        Process
        -------
        - Store the root window and configure its title and geometry.
        - Create and position all widgets (labels, entry, button) on the root.
        - Open 'members.csv' and read four rows, assigning them to instance
          variables. Each row is expected to correspond to a specific field and
          the CSV is assumed to have been written with one member per column.

        Input Data
        ----------
        root : tk.Tk
            Tk window passed by the caller.

        Output Data
        -----------
        None (side effects: GUI widgets created and member lists populated).
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


    # Takes the memberID (string) from the entry field and checks if it exists in the list of member IDs.
    # If the member exists, it checks if their age (integer) is greater than 18 and displays an appropriate message.
    # If the member does not exist, it displays an error message.
    def calculateElig(self):
        """Determine and display eligibility based on member ID and age.

        This method reads the value currently entered in the
        ``memberIdLabel`` entry widget, searches for that ID in the
        ``self.memberIDs`` list loaded from the CSV, and compares the
        associated date of birth to the cutoff date to determine if the
        member is at least 18 years old (eligibility for "P").

        Input Data
        ----------
        None directly. The method uses internal state:
        - ``self.memberIdLabel.get()`` -> ``str``: ID text entered by the user.
        - ``self.memberIDs`` -> ``list[str]``: list of registered IDs.
        - ``self.dateOfBirths`` -> ``list[str]``: list of birthdates as
          "YYYY-M-D" strings.
        - ``self.firstNames`` , ``self.lastNames`` -> ``list[str]``: name data.

        Process
        -------
        1. Initialize ``found`` flag to ``False``.
        2. Iterate over index ``i`` through ``self.memberIDs``.
        3. If the ID matches the user entry, convert the corresponding
           ``dateOfBirths[i]`` to string and compare lexically against the
           hard-coded cutoff ("2008-2-26").
        4. Show a messagebox indicating eligible or not eligible using the
           stored names.
        5. Set ``found`` to ``True`` and break the loop.
        6. After the loop, if ``found`` is still ``False``, display an
           error message informing the user the ID is not registered.

        Output Data
        -----------
        None returned. The result is conveyed through ``tkinter`` message
        boxes:
        - ``messagebox.showinfo`` with either eligibility or error text.
        The internal ``found`` flag is manipulated but not exposed.
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