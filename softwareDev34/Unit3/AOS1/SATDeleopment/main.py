#import pandas as pd
import re
import tkinter as tk
import csv
from tkinter import messagebox

from matplotlib import style

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
    def __init__(self):
        super().__init__()
        
        
        self.font_title = ("Helvetica", 60, "bold")
        self.font_para = ("Helvetica", 30, "normal")

        self.labela = tk.Label(master=app, text="Squiz", font=self.font_title, bg=colours["bg"], fg=colours["text"])

        self.check = tk.Label(master=app, text="Incorrect username or password!", font=self.font_para, bg=colours["bg"], fg=colours["danger"])


        def on_entry_click(event, entryType, placeholder):
            """Function to clear placeholder and enable masking."""
            if placeholder == "Password":
                if entryType.get() == placeholder:
                    entryType.delete(0, tk.END)
                    entryType.config(show='*', fg=colours["lightText"])
            else:
                if entryType.get() == placeholder:
                    entryType.delete(0, tk.END)
                    entryType.config(fg=colours["lightText"]) # Change color to black when user starts typing

        def on_focusout(event, entryType, placeholder):
            """Function to restore placeholder if field is left empty."""
            if placeholder == "Password":
                if not entryType.get():
                    entryType.insert(0, placeholder)
                    entryType.config(show='', fg=colours["lightText"]) # Show text and change color to grey
            else:
                if not entryType.get():
                    entryType.insert(0, placeholder)
                    entryType.config(show='', fg=colours["lightText"]) # Show text and change color to grey

        self.loginFrame = tk.Frame(master=app, bg=colours["border"],highlightcolor=colours["actualBorder"],highlightbackground=colours["actualBorder"] ,highlightthickness=3,width=600, height=400)

        self.username = tk.Entry(master=self.loginFrame, width=25, font=self.font_para, fg=colours["lightText"], bg=colours["border"], bd=0, highlightcolor=colours["actualBorder"], highlightthickness=3, highlightbackground=colours["actualBorder"])
        self.username.insert(0, "Username")

        self.username.bind('<FocusIn>', lambda event: on_entry_click(event, self.username, "Username"))
        self.username.bind('<FocusOut>', lambda event: on_focusout(event, self.username, "Username"))

        self.passwordEntry = tk.Entry(master=self.loginFrame, width=25, fg=colours["lightText"], bg=colours["border"], bd=0, highlightcolor=colours["actualBorder"], highlightthickness=3, highlightbackground=colours["actualBorder"],font=self.font_para)
        self.passwordEntry.insert(0, "Password")
        
        self.passwordEntry.bind('<FocusIn>', lambda event: on_entry_click(event, self.passwordEntry, "Password"))
        self.passwordEntry.bind('<FocusOut>', lambda event: on_focusout(event, self.passwordEntry, "Password"))

        self.button = tk.Button(master=self.loginFrame, text="Login", command=self.submit, font=self.font_para, bg=colours["border"], fg=colours["lightText"], bd=0, highlightcolor=colours["actualBorder"], activebackground=colours["actualBorder"], disabledforeground=colours["border"],highlightthickness=3, highlightbackground=colours["actualBorder"], width=10)

        self.newAccBut = tk.Button(master=self.loginFrame, text="Create new account", command=self.goToNewAcc)
          
    def show(self):
        hide_all()
        #self.label.place(relx=0.5, rely=0.1, anchor="center")
        self.labela.place(relx=0.5, rely=0.1, anchor="center")
        self.username.place(relx=0.5, rely=0.3, anchor="center")
        self.passwordEntry.place(relx=0.5, rely=0.5, anchor="center")
        self.button.place(relx=0.5, rely=0.6, anchor="center")
        self.newAccBut.place(relx=0.8, rely=0.95, anchor="center")
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
        with open('C:/Users/anton/Programming/PythonProjects/School/softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv', newline='') as f:
            reader = csv.reader(f, skipinitialspace=True)
            first_row = reader.__next__()          # first row
            next(reader)          # first row
            second_row = next(reader)
        print(first_row)
        print(second_row)
        
        self.user = self.username.get()
        self.password = self.passwordEntry.get()

        data = self.df[self.df['username']== self.user].astype(str)
        print(self.password, type(self.password))
        print(data['password'].tolist())

        print('\n ------------\n')
        print(self.df['username'].tolist())

        if self.user in self.df['username'].tolist() and self.password in data['password'].tolist():
            print(f'hello {self.user}.')
            show_page2()
        else:
            self.check.place(relx=0.5, rely=0.5, anchor="center")
            print('Incorrect username or password.')


        print(self.df[self.df['username']== self.user])
 
class mainPage:
    def __init__(self):
        #username = page1.user
        self.hello = tk.Label(master=app, text=f"Hello, user", font=page1.font_title)
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
            page1.df = page1.df[page1.df.username != page1.user]
            page1.df.to_csv('SoftwareDev10/l4_year12LoginPageFolder/accounts.csv', index=False)
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
        self.newAccLabel = tk.Label(master=app, text="Create a New Account", font=page1.font_title)

        self.checkNewAcc = tk.Label(master=app, text="Incorrect username or password!", font=(page1.font_para, 20))


        self.newUsername = tk.Entry(master=app, width=20, font=page1.font_para)

        self.newPassword = tk.Entry(master=app, width=20, font=page1.font_para, show="*")

        self.done = tk.Button(master=app, text="Submit", command=self.createNewAcc)
        
        #self.backbut = ttk.Button(master=app, text="Back", command=self.managePage)
    def createNewAcc(self):
        newUser = self.newUsername.get()
        newPass = self.newPassword.get()

        if newUser in page1.df['username'].tolist():
            print('Username not available')
            self.checkNewAcc.configure(text='Username not available')
            self.checkNewAcc.place(relx=0.5, rely=0.5, anchor="center")
        else:
            if newPass.isascii():
                
                match = re.findall('@gwsc.vic.edu.au', newUser)
                if match:
                    
                    if len(newPass) >= 8:
                        page1.df.loc[len(page1.df)] = [newUser, newPass]  
                        page1.show()
                        page1.df.to_csv('SoftwareDev10/l4_year12LoginPageFolder/accounts.csv', index=True)
                        print('New account created')
                        print(page1.df)
                    else:
                        self.checkNewAcc.configure(text='Password must contain at least 8 characters')
                        self.checkNewAcc.place(relx=0.5, rely=0.5, anchor="center")
                else:
                    self.checkNewAcc.configure(text='Email must be GWSC')
                    self.checkNewAcc.place(relx=0.5, rely=0.5, anchor="center")

            else:
                self.checkNewAcc.configure(text='Please enter a password')
                self.checkNewAcc.place(relx=0.5, rely=0.5, anchor="center")

                     
    def show(self):
        hide_all()
        self.newAccLabel.place(relx=0.5, rely=0.1, anchor="center")
        self.newUsername.place(relx=0.5, rely=0.2, anchor="center")
        self.newPassword.place(relx=0.5, rely=0.3, anchor="center")
        self.done.place(relx=0.5, rely=0.4, anchor="center")
        

    def hide(self):
        self.newAccLabel.place_forget()
        self.newUsername.place_forget()
        self.newPassword.place_forget()
        self.checkNewAcc.place_forget()
        self.done.place_forget()



page1 = logInPage()

page2 = mainPage()

page3 = newAccPage()

page4 = manageAccPage()


show_page1()


app.mainloop()
