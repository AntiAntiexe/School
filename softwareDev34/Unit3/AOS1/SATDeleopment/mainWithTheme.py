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
style.theme_use('alt')
style.configure('TButton',font=font_para, background=colours["border"], foreground=colours["lightText"], borderwidth=3, bordercolor=colours["actualBorder"], relief="flat", focusthickness=0, highlightthickness=0)
style.map('TButton', background=[('active', colours["actualBorder"]), ('disabled', colours["actualBorder"])], foreground=[('disabled', colours["actualBorder"])])
style.configure('TLabel', background=colours["bg"], foreground=colours["text"])
style.configure('TEntry', background=colours["border"], foreground=colours["lightText"], fieldbackground=colours["border"], borderwidth=0, highlightthickness=3, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"] )
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
    def __init__(self):
        super().__init__()
        
        
        

        self.labela = ttk.Label(master=app, text="Squiz", font=font_title, style='TLabel')

        self.check = ttk.Label(master=app, text="Incorrect username or password!", font=font_para, style='TLabel')


        def on_entry_click(event, entryType, placeholder):
            """Function to clear placeholder and enable masking."""
            if placeholder == "Password":
                if entryType.get() == placeholder:
                    entryType.delete(0, tk.END)
                    entryType.config(show='*')
            else:
                if entryType.get() == placeholder:
                    entryType.delete(0, tk.END)
                    

        def on_focusout(event, entryType, placeholder):
            """Function to restore placeholder if field is left empty."""
            if placeholder == "Password":
                if not entryType.get():
                    entryType.insert(0, placeholder)
                    entryType.config(show='') # Show text and change color to grey
            else:
                if not entryType.get():
                    entryType.insert(0, placeholder)
                    entryType.config(show='') # Show text and change color to grey

        self.loginFrame = ttk.Frame(master=app, style='TFrame', width=600, height=400)

        self.username = ttk.Entry(master=self.loginFrame, width=25, font=font_para, style='TEntry')
        self.username.insert(0, "Username")

        self.username.bind('<FocusIn>', lambda event: on_entry_click(event, self.username, "Username"))
        self.username.bind('<FocusOut>', lambda event: on_focusout(event, self.username, "Username"))

        self.passwordEntry = ttk.Entry(master=self.loginFrame, width=25, font=font_para, style='TEntry')
        self.passwordEntry.insert(0, "Password")
        
        self.passwordEntry.bind('<FocusIn>', lambda event: on_entry_click(event, self.passwordEntry, "Password"))
        self.passwordEntry.bind('<FocusOut>', lambda event: on_focusout(event, self.passwordEntry, "Password"))

        self.button = ttk.Button(master=self.loginFrame, text="Login", command=self.submit)

        self.newAccBut = ttk.Button(master=self.loginFrame, text="Create new account", command=self.goToNewAcc)

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
        self.newAccLabel = tk.Label(master=app, text="Create a New Account", font=font_title)

        self.checkNewAcc = tk.Label(master=app, text="Incorrect username or password!", font=(font_para, 20))


        self.newUsername = tk.Entry(master=app, width=20, font=font_para)

        self.newPassword = tk.Entry(master=app, width=20, font=font_para, show="*")

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
