"""AthleteApp login GUI

This module provides a simple Tkinter-based login GUI for an athlete
application. The file contains the `AthleteApp` class which creates the
widgets and handles user actions.

Module behavior (high-level):
- Input: None at module import; running the file creates a Tk root and
    launches the GUI (side-effect). The GUI accepts user-typed values via
    `Entry` widgets.
- Process: The `AthleteApp` methods read widget values (strings), perform
    validation/comparison and update the GUI (labels, messageboxes) as side
    effects.
- Output: No return values; outputs are GUI side-effects (message boxes,
    widget updates). See method docstrings for details.

Data types summary (most-used):
- `root`: tkinter root window (e.g. `tk.Tk`).
- Member number: string from `Entry` expected to be numeric and is cast to
    `int` inside `login()`.
- Password: `str` from `Entry`.
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class AthleteApp:
        """GUI class for athlete login.

        Purpose:
        - Build and manage a simple login window with member number and
            password fields and three action buttons (`Reset`, `Login`,
            `Exit`).

        Inputs (constructor):
        - `root` (tkinter root window): type `tk.Tk` or compatible tkinter
            container. The window is configured within the constructor.

        Processing:
        - Creates and places `ttk.Label`, `ttk.Entry` and `ttk.Button`
            widgets as instance attributes.

        """
        def __init__(self, root):
            self.root = root
            self.root.title("Athlete Application")
            self.root.geometry("600x250")

            self.titleLabel = ttk.Label(self.root, text="User Login")
            self.titleLabel.place(x=250, y=30, anchor='center')


            self.memberLabel = ttk.Label(self.root, text="Member Number")
            self.memberLabel.place(x=150, y=85, anchor='center')

            self.memberEntry = ttk.Entry(self.root)
            self.memberEntry.place(x=280, y=85, anchor='center')

            self.password = ttk.Label(self.root, text="Password")
            self.password.place(x=150, y=125, anchor='center')

            self.passwordEntry = ttk.Entry(self.root,  show="*")
            self.passwordEntry.place(x=280, y=125, anchor='center')

        
        

            self.resetButton = ttk.Button(self.root, text="Reset", command=self.reset)
            self.resetButton.place(x=150, y=185, anchor='center')

            self.loginButton = ttk.Button(self.root, text="Login", command=self.login)
            self.loginButton.place(x=300, y=185, anchor='center')

            self.exitButton = ttk.Button(self.root, text="Exit", command=self.exit)
            self.exitButton.place(x=450, y=185, anchor='center')
    
        def reset(self):
            """Clear entry fields and focus member entry.

        Input: None (uses internal widget state).
        Process: Calls `delete(0, END)` on both `Entry` widgets.
        Output: None. Side-effects: both `Entry` widgets become empty and
        `memberEntry` receives keyboard focus.
            """
            self.memberEntry.delete(0, tk.END)
            self.passwordEntry.delete(0, tk.END)



            self.memberEntry.focus()
    
        def exit(self):
            """Close the application window.

        Input: None (uses `self.root`).
        Process: Calls `destroy()` on the provided tkinter root.
        Output: None. Side-effect: the GUI terminates.
            """

            self.root.destroy()


    
        def login(self):
                """Validate login credentials from the GUI.

                Expected inputs (read from widgets):
                - Member number: obtained from `self.memberEntry.get()` -> `str`.
                    The string is expected to represent an integer and is cast to
                    `int` (thus a non-numeric value will raise `ValueError`).
                - Password: obtained from `self.passwordEntry.get()` -> `str`.

                Processing:
                - Compares the parsed member number to a hard-coded integer
                    `intCorrectMemNo` and the password to `strCorrectPassword`.
                - On success: shows an informational message box.
                - On failure: places a small `ttk.Label` indicating the error,
                    clears and focuses the appropriate `Entry` widget.

                Outputs: messagebox on success; error label, cleared fields,
                and focus changes on failure.

                Note: This method does not return values and will raise an
                exception if the member number field does not contain a valid
                integer string.
                """

                intCorrectMemNo = 123456

                strCorrectPassword = 'TestPass123'

                intMemberNumber = int(self.memberEntry.get())
                strPassword= str(self.passwordEntry.get())
                self.errorlabel = ttk.Label(self.root, text="")  # Placeholder for error messages
                if intMemberNumber == intCorrectMemNo:
                        if strPassword == strCorrectPassword:
                                messagebox.showinfo("", "Login successful")
                        else:
                                self.errorlabel.destroy()  # Remove previous error label if it exists
                                self.errorlabel = ttk.Label(self.root, text="Password Incorrect")
                                self.errorlabel.place(x=300, y=150, anchor='center')

                                self.passwordEntry.delete(0, tk.END)

                                self.passwordEntry.focus()
                else:
                        self.errorlabel.destroy()  # Remove previous error label if it exists
                        self.errorlabel = ttk.Label(self.root, text="Member Number or Password Incorrect")
                        self.errorlabel.place(x=300, y=150, anchor='center')

                        self.memberEntry.delete(0, tk.END)
                        self.passwordEntry.delete(0, tk.END)

                        self.memberEntry.focus()


        

# Create an object of the AthleteApp class and start the main event loop to run the application.
app = tk.Tk()
app_instance = AthleteApp(app)
app.mainloop()