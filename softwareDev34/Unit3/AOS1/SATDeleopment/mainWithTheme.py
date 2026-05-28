import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox


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
style.configure('Secondary.TLabel', background=colours["border"], foreground=colours["lightText"])

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
    def on_entry_click(self, event, entryType, strPlaceholder):
            """Function to clear placeholder and enable masking."""
            if strPlaceholder == "Password":
                if entryType.get() == strPlaceholder:
                    entryType.delete(0, tk.END)
                    entryType.config(show='*')
            else:
                if entryType.get() == strPlaceholder:
                    entryType.delete(0, tk.END)
                    

    def on_focusout(self, event, entryType, strPlaceholder):
            """Function to restore placeholder if field is left empty."""
            if strPlaceholder == "Password":
                if not entryType.get():
                    entryType.insert(0, strPlaceholder)
                    entryType.config(show='') # Show text and change color to grey
            else:
                if not entryType.get():
                    entryType.insert(0, strPlaceholder)
                    entryType.config(show='') # Show text and change color to grey

    def __init__(self):
        super().__init__()
        self.current_username = ""

        self.lblTitle = ttk.Label(master=app, text="Squiz", font=font_title, style='TLabel')

        

        self.frLogin = ttk.Frame(master=app, style='TFrame', width=600, height=400)

        self.entryUsername = ttk.Entry(master=self.frLogin, width=25, font=font_para, style='TEntry')
        self.entryUsername.insert(0, "Username")

        self.entryUsername.bind('<FocusIn>', lambda event: self.on_entry_click(event, self.entryUsername, "Username"))
        self.entryUsername.bind('<FocusOut>', lambda event: self.on_focusout(event, self.entryUsername, "Username"))

        self.entryPassword = ttk.Entry(master=self.frLogin, width=25, font=font_para, style='TEntry')
        self.entryPassword.insert(0, "Password")
        
        self.entryPassword.bind('<FocusIn>', lambda event: self.on_entry_click(event, self.entryPassword, "Password"))
        self.entryPassword.bind('<FocusOut>', lambda event: self.on_focusout(event, self.entryPassword, "Password"))

        self.btnLogin = ttk.Button(master=self.frLogin, text="Login", command=self.submit)

        self.btnSignUp = ttk.Button(master=app, text="Sign Up", command=self.goToNewAcc)

    def show(self):
        hide_all()
        self.lblTitle.place(relx=0.5, rely=0.1, anchor="center")
        self.entryUsername.place(relx=0.5, rely=0.3, anchor="center")
        self.entryPassword.place(relx=0.5, rely=0.5, anchor="center")
        self.btnLogin.place(relx=0.5, rely=0.7, anchor="center")
        self.btnSignUp.place(relx=0.9, rely=0.95, anchor="center")
        self.frLogin.place(relx=0.5, rely=0.5, anchor="center")
        
        

    def hide(self):
        self.lblTitle.place_forget()
        self.entryUsername.place_forget()
        self.entryPassword.place_forget()
        self.btnLogin.place_forget()
        self.btnSignUp.place_forget()
        self.frLogin.place_forget()

    def goToNewAcc(self):
        show_page3()
        

    def submit(self):
        self.arrUsernames = []
        self.arrPasswords = []

        with open('softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.arrPasswords.append(row[1])  # Assuming passwords are in the second column
                self.arrUsernames.append(row[0])  # Assuming usernames are in the first column
        
        
        self.strUsernameToFind = self.entryUsername.get().strip()
        self.strPasswordToFind = self.entryPassword.get()

        

        intLow = 0
        intHigh = len(self.arrUsernames) - 1
        bFound = False

        while bFound == False and intLow <= intHigh:
            intMid = (intLow + intHigh) // 2

            if self.arrUsernames[intMid] == self.strUsernameToFind:
                if self.arrPasswords[intMid] == self.strPasswordToFind:
                    bFound = True
                    self.current_username = self.strUsernameToFind
                    print("Login successful")
                    break
                else:
                    intLow = intMid + 1
            elif self.arrUsernames[intMid] > self.strUsernameToFind:
                intHigh = intMid - 1
            else:
                intLow = intMid + 1
        
        if bFound == True:
            print("Login successful")
            messagebox.showinfo(title="Login Successful", message="You have successfully logged in.")
            page2.show()
        else:
            print("Login failed")
            messagebox.showwarning(title="Login Failed", message="Invalid username or password.")
            

        
 
class mainPage:
    def __init__(self):
        super().__init__()
        #username = page1.user
        self.hello = ttk.Label(master=app, text="Quizzes", font=font_title, style='TLabel')

        self.btnSort = ttk.Button(master=app, text="Sort", command=self.sort, style='TButton')
        self.btnAdd = ttk.Button(master=app, text="Add", command=self.add, style='TButton')

        self.back = ttk.Button(master=app, text="Log Out", command=show_page1, style='TButton')
        self.manageAccBut = ttk.Button(master=app, text="Account", command=self.managePage, style='TButton')

    def getQuizzes(self):
        username = getattr(page1, 'strUsernameToFind', '').strip()
        if not username:
            return

        data = []

        with open('softwareDev34/Unit3/AOS1/SAT/quiz.csv') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                data.append(row)

        for i in range(len(data)):
            if data[i][1].startswith(page1.strUsernameToFind):
                strQuizTitle = data[i][0]

                frameQuiz = ttk.Frame(master=app, style='TFrame', width=800, height=100)
                lblQuizTitle = ttk.Label(master=frameQuiz, text=strQuizTitle, font=font_para, style='TLabel')
                btnTakeQuiz = ttk.Button(master=frameQuiz, text="Take Quiz", style='TButton', command=self.playQuiz())

        
        
    def playQuiz(self):
        pass

    def sort(self):
        pass

    def add(self):
        pass

    def managePage(self):
        page4.show()
        
    def show(self):
        hide_all()
        self.getQuizzes()
        
        self.hello.place(relx=0.5, rely=0.1, anchor="center")
        self.btnSort.place(relx=0.05, rely=0.05, anchor="nw")
        self.btnAdd.place(relx=0.95, rely=0.05, anchor="ne")
        self.back.place(relx=0.05, rely=0.95, anchor="sw")
        self.manageAccBut.place(relx=0.95, rely=0.95, anchor="se")

        

    def hide(self):
        self.hello.place_forget()
        self.btnSort.place_forget()
        self.btnAdd.place_forget()
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

        self.lblNewAccount = ttk.Label(master=app, text="Sign Up", font=font_title, style='TLabel')

        self.frmSignUp = ttk.Frame(master=app, style='TFrame', width=600, height=400)

        
        self.entryNewUsername = ttk.Entry(master=self.frmSignUp, width=25, font=font_para, style='TEntry')
        self.entryNewUsername.insert(0, "Username")

        

        self.entryNewUsername.bind('<FocusIn>', lambda event: page1.on_entry_click(event, self.entryNewUsername, "Username"))
        self.entryNewUsername.bind('<FocusOut>', lambda event: page1.on_focusout(event, self.entryNewUsername, "Username"))

        self.entryNewPassword = ttk.Entry(master=self.frmSignUp, width=25, font=font_para, style='TEntry')
        self.entryNewPassword.insert(0, "Password")

        self.entryNewPassword.bind('<FocusIn>', lambda event: page1.on_entry_click(event, self.entryNewPassword, "Password"))
        self.entryNewPassword.bind('<FocusOut>', lambda event: page1.on_focusout(event, self.entryNewPassword, "Password"))

        self.btnSubmit = ttk.Button(master=self.frmSignUp, text="Submit", command=self.createNewAcc, style='TButton')

        self.btnBackToLogin = ttk.Button(master=app, text="Login", command=self.goToLogin, style='TButton')

    def goToLogin(self):
        show_page1()

    def createNewAcc(self):

        self.arrUsernames = []
        self.arrPasswords = []

        with open('softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.arrPasswords.append(row[1])  # Assuming passwords are in the second column
                self.arrUsernames.append(row[0])  # Assuming usernames are in the first column
        

        strNewUsername = self.entryNewUsername.get()
        strNewPassword = self.entryNewPassword.get()
        if self.arrUsernames is not None:
            if strNewUsername == '' or strNewUsername == "Username":
                print('Please enter a username')
                messagebox.showwarning(title="Invalid Username", message="Please enter a valid username.")
                return
            for i in range(len(self.arrUsernames)):
                if strNewUsername == self.arrUsernames[i]:
                    print('Username not available')
                    messagebox.showwarning(title="Username Unavailable", message="The username you have entered is already taken. Please choose a different username.")
                    return
            if strNewPassword == '' or strNewPassword == "Password":
                print('Please enter a password')
                messagebox.showwarning(title="Invalid Password", message="Please enter a valid password.")
                return
                
            if len(strNewPassword) < 8:
                print('Password must contain at least 8 characters')
                messagebox.showwarning(title="Weak Password", message="Your password must contain at least 8 characters. Please choose a stronger password.")
                return
            
            writer = csv.writer(open("softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv", 'a', newline=''))
            writer.writerow([strNewUsername, strNewPassword])
            
            print('New account created')
            messagebox.showinfo(title="Account Created", message="Your new account has been created successfully.")
            show_page1()
        else:
            print('Please enter a username')
            messagebox.showwarning(title="Invalid Username", message="Please enter a valid username.")

        

                     
    def show(self):
        hide_all()
        self.lblNewAccount.place(relx=0.5, rely=0.1, anchor="center")
        self.entryNewUsername.place(relx=0.5, rely=0.3, anchor="center")
        self.entryNewPassword.place(relx=0.5, rely=0.5, anchor="center")
        self.btnSubmit.place(relx=0.5, rely=0.7, anchor="center")
        self.frmSignUp.place(relx=0.5, rely=0.5, anchor="center")
        self.btnBackToLogin.place(relx=0.9, rely=0.95, anchor="center")
        

    def hide(self):
        self.lblNewAccount.place_forget()
        self.entryNewUsername.place_forget()
        self.entryNewPassword.place_forget()
        self.btnSubmit.place_forget()
        self.frmSignUp.place_forget()
        self.btnBackToLogin.place_forget()



page1 = logInPage()

page2 = mainPage()

page3 = newAccPage()

page4 = manageAccPage()


show_page1()


app.mainloop()
