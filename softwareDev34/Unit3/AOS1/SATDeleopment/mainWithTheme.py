#import pandas as pd
import re
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox

#from matplotlib import style

colours = {
    "bg":  "#e0e6f0",
    "text": "#060b19",
    "lightText": "#f0f5ff",
    "highligh": "#ffffff",
    "border": "#778092",
    "primary": "#2b457d",
    "secondary": "#473400",
    "danger": "#7f5953",
    "warning": "#6b6543",
    "success": "#4a6d5a",
    "info": "#4a6d5a",
    "actualBorder": "#404859"
}


app = tk.Tk()
app.title("Squiz")
app.geometry("1000x800")
app.configure(bg=colours["bg"])

#style.use('clam')

font_title = ("Helvetica", 60, "bold")
font_para = ("Helvetica", 30, "normal")

style = ttk.Style()
style.theme_use('classic')

style.configure('TButton',font=font_para, background=colours["actualBorder"], foreground=colours["lightText"], borderwidth=0.5, bordercolor=colours["actualBorder"], relief="flat", focusthickness=0, highlightthickness=0)
style.map('TButton', background=[('active', colours["primary"])])

style.configure('TLabel', background=colours["bg"], foreground=colours["text"])

style.configure('TEntry', background=colours["actualBorder"], foreground=colours["lightText"], fieldbackground=colours["border"], relief="flat",borderwidth=0, highlightthickness=2, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"] )
style.map('TEntry', background=[('focus', colours["actualBorder"]), ('focus', colours["actualBorder"])], foreground=[('focus', colours["lightText"])], highlightcolor=[('focus', colours["actualBorder"])])

style.configure('TFrame', background=colours["border"], highlightthickness=3, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"])





def hide_all():
    """ Hides all the pages """
    page1.hide()
    page2.hide()
    page3.hide()
    page4.hide()


def show_page1():
    page1.show()


def show_page2():
    page2.show()

def show_page3():
    page3.show()

def show_page4():
    page4.show()

class logInPage:
    def on_entry_click(self, event, entryType, placeholder):
            """Function to clear placeholder and enable masking."""
            if placeholder == "Password":
                if entryType.get() == placeholder:
                    entryType.delete(0, tk.END)
                    entryType.config(show='*')
            else:
                if entryType.get() == placeholder:
                    entryType.delete(0, tk.END)
                    

    def on_focusout(self, event, entryType, placeholder):
            """Function to restore placeholder if field is left empty."""
            if placeholder == "Password":
                if not entryType.get():
                    entryType.insert(0, placeholder)
                    entryType.config(show='') # Show text and change color to grey
            else:
                if not entryType.get():
                    entryType.insert(0, placeholder)
                    entryType.config(show='') # Show text and change color to grey

    def __init__(self):
        super().__init__() 

         

        self.labela = ttk.Label(master=app, text="Squiz", font=font_title, style='TLabel')

        self.check = ttk.Label(master=app, text="Incorrect username or password!", font=font_para, style='TLabel')
        

        self.loginFrame = ttk.Frame(master=app, style='TFrame', width=600, height=400)

        self.username = ttk.Entry(master=self.loginFrame, width=25, font=font_para, style='TEntry')
        self.username.insert(0, "Username")

        self.username.bind('<FocusIn>', lambda event: self.on_entry_click(event, self.username, "Username"))
        self.username.bind('<FocusOut>', lambda event: self.on_focusout(event, self.username, "Username"))

        self.passwordEntry = ttk.Entry(master=self.loginFrame, width=25, font=font_para, style='TEntry')
        self.passwordEntry.insert(0, "Password")
        
        self.passwordEntry.bind('<FocusIn>', lambda event: self.on_entry_click(event, self.passwordEntry, "Password"))
        self.passwordEntry.bind('<FocusOut>', lambda event: self.on_focusout(event, self.passwordEntry, "Password"))

        self.button = ttk.Button(master=self.loginFrame, text="Login", command=self.submit)

        self.newAccBut = ttk.Button(master=app, text="Sign Up", command=self.goToNewAcc)

    def show(self):
        hide_all()
        #self.label.place(relx=0.5, rely=0.1, anchor="center")
        self.labela.place(relx=0.5, rely=0.1, anchor="center")
        self.username.place(relx=0.5, rely=0.3, anchor="center")
        self.passwordEntry.place(relx=0.5, rely=0.5, anchor="center")
        self.button.place(relx=0.5, rely=0.7, anchor="center")
        self.newAccBut.place(relx=0.9, rely=0.95, anchor="center")
        self.loginFrame.place(relx=0.5, rely=0.5, anchor="center")
        
        

    def hide(self):
        #self.label.place_forget()
        self.labela.place_forget()
        self.username.place_forget()
        self.passwordEntry.place_forget()
        self.button.place_forget()
        self.check.place_forget()
        self.newAccBut.place_forget()
        self.loginFrame.place_forget()

    def goToNewAcc(self):
        show_page3()
        

    def submit(self):
        self.arrUsernames = []
        self.arrPasswords = []
        with open('softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv', newline='') as f:
            reader = csv.reader(f, skipinitialspace=True)
            self.arrUsernames = next(reader, None)

            if self.arrUsernames is not None:
                self.arrPasswords = next(reader, None)
        print(self.arrUsernames)

        if self.arrUsernames is None:
            print('accounts.csv is empty or missing header rows')
        else:
            print(self.arrUsernames)
            if self.arrPasswords is not None:
                print(self.arrPasswords)
            else:
                print('accounts.csv has only one row')
        
        
        self.strUsernameToFind = self.username.get()
        self.strPasswordToFind = self.passwordEntry.get()

        

        intLow = 0
        intHigh = len(self.arrUsernames) - 1
        bFound = False

        while bFound == False and intLow <= intHigh:
            intMid = (intLow + intHigh) // 2

            if self.arrUsernames[intMid] == self.strUsernameToFind:
                if self.arrPasswords[intMid] == self.strPasswordToFind:
                    bFound = True
                    print("Login successful")
                    page2.show()
                else:
                    intLow = intMid + 1
            elif self.arrUsernames[intMid] > self.strUsernameToFind:
                intHigh = intMid - 1
            else:
                intLow = intMid + 1
        
        if bFound == True:
            print("Login successful")
            page2.show()
        else:
            print("Login failed")
            self.check.place(relx=0.5, rely=0.5, anchor="center")

        
 
class mainPage:
    def __init__(self):
        #username = page1.user
        self.hello = tk.Label(master=app, text=f"Hello, user", font=font_title)
        self.back = tk.Button(master=app, text="Log Out", command=show_page1)

        self.manageAccBut = tk.Button(master=app, text="Manage Account", command=self.managePage)
    def managePage(self):
        page4.show()
        
    def show(self):
        hide_all()
        self.hello.place(relx=0.5, rely=0.1, anchor="center")
        self.back.place(relx=0.125, rely=0.95, anchor="center")
        self.manageAccBut.place(relx=0.8, rely=0.95, anchor="center")
        

    def hide(self):
        self.hello.place_forget()
        self.back.place_forget()
        self.manageAccBut.place_forget()

class manageAccPage:
    def __init__(self):
        self.delete =   tk.Button(master=app, text="Delete Account")
        
        self.done = tk.Button(master=app, text="Done")
    def deleteAcc(self):
        response = messagebox.askyesno(title="Delete", message="Are you sure you want to delete your account? This action is not reversable.")

        if response:
            page1.df = page1.df[page1.df.username != page1.strUsernameToFind]
            page1.df.to_csv('softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv', index=False)
            print(page1.df)

            show_page1()

        else:
            print("Click 'Yes' to exit!")
        
        
    def show(self):
        hide_all()
        self.delete.place(relx=0.5, rely=0.4, anchor="center")
        self.done.place(relx=0.8, rely=0.95, anchor="center")
        

    def hide(self):
        self.delete.place_forget()
        self.done.place_forget()

class newAccPage:
    def __init__(self):
        super().__init__()

        self.newAccLabel = ttk.Label(master=app, text="Sign Up", font=font_title, style='TLabel')
        self.checkNewAcc = ttk.Label(master=app, text="Incorrect username or password!", font=(font_para, 20), style='TLabel')

        
        self.signUpFrame = ttk.Frame(master=app, style='TFrame', width=600, height=400)
        
        self.newUsername = ttk.Entry(master=self.signUpFrame, width=25, font=font_para, style='TEntry')
        self.newUsername.insert(0, "Username")

        

        self.newUsername.bind('<FocusIn>', lambda event: page1.on_entry_click(event, self.newUsername, "Username"))
        self.newUsername.bind('<FocusOut>', lambda event: page1.on_focusout(event, self.newUsername, "Username"))

        self.newPasswordEntry = ttk.Entry(master=self.signUpFrame, width=25, font=font_para, style='TEntry')
        self.newPasswordEntry.insert(0, "Password")

        self.newPasswordEntry.bind('<FocusIn>', lambda event: page1.on_entry_click(event, self.newPasswordEntry, "Password"))
        self.newPasswordEntry.bind('<FocusOut>', lambda event: page1.on_focusout(event, self.newPasswordEntry, "Password"))

        self.submit = ttk.Button(master=self.signUpFrame, text="Submit", command=self.createNewAcc, style='TButton')

        self.loginButton = ttk.Button(master=app, text="Login", command=self.goToLogin, style='TButton')

    def goToLogin(self):
        show_page1()

    def createNewAcc(self):

        self.arrUsernames = []
        self.arrPasswords = []
        with open('softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv', newline='') as f:
            reader = csv.reader(f, skipinitialspace=True)
            self.arrUsernames = next(reader, None)

            if self.arrUsernames is not None:
                self.arrPasswords = next(reader, None)
        print(self.arrUsernames)

        if self.arrUsernames is None:
            print('accounts.csv is empty or missing header rows')
        else:
            print(self.arrUsernames)
            if self.arrPasswords is not None:
                print(self.arrPasswords)
            else:
                print('accounts.csv has only one row')

        strNewUsername = self.newUsername.get()
        strNewPassword = self.newPasswordEntry.get()
        if self.arrUsernames is not None:
            for i in range(len(self.arrUsernames)):
                if strNewUsername == self.arrUsernames[i]:
                    print('Username not available')
                    self.checkNewAcc.configure(text='Username not available')
                    self.checkNewAcc.place(relx=0.5, rely=0.5, anchor="center")
                    return
                
        if len(strNewPassword) < 8:
            print('Password must contain at least 8 characters')
            self.checkNewAcc.configure(text='Password must contain at least 8 characters')
            self.checkNewAcc.place(relx=0.5, rely=0.5, anchor="center")
            return
            
        writer = csv.writer(open("softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv", 'a', newline=''))
        writer.writerow([strNewUsername])
        writer.writerow([strNewPassword])
        print('New account created')
        

        

                     
    def show(self):
        hide_all()
        self.newAccLabel.place(relx=0.5, rely=0.1, anchor="center")
        self.newUsername.place(relx=0.5, rely=0.3, anchor="center")
        self.newPasswordEntry.place(relx=0.5, rely=0.5, anchor="center")
        self.submit.place(relx=0.5, rely=0.7, anchor="center")
        self.signUpFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.loginButton.place(relx=0.9, rely=0.95, anchor="center")
        

    def hide(self):
        self.newAccLabel.place_forget()
        self.newUsername.place_forget()
        self.newPasswordEntry.place_forget()
        self.checkNewAcc.place_forget()
        self.submit.place_forget()
        self.signUpFrame.place_forget()
        self.loginButton.place_forget()



page1 = logInPage()

page2 = mainPage()

page3 = newAccPage()

page4 = manageAccPage()


show_page1()


app.mainloop()
