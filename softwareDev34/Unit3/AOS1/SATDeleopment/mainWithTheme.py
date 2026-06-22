import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import time



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
app.geometry("1100x800")
app.configure(bg=colours["bg"])

#style.use('clam')
tplFontButton = ("Helvetica", 100, "bold")
tplFontTitle = ("Helvetica", 60, "bold")
tplFontPara = ("Helvetica", 30, "normal")
tplSmallFont = ("Helvetica", 20, "normal")
tplSmallerTitle = ("Helvetica", 30, "bold")
tplVerticalFont = ("Helvetica", 150, "normal")

objStyle = ttk.Style()
objStyle.theme_use('classic')



objStyle.configure('TButton',font=tplFontPara, background=colours["actualBorder"], foreground=colours["lightText"], borderwidth=0.5, bordercolor=colours["actualBorder"], relief="flat", focusthickness=0, highlightthickness=0)
objStyle.map('TButton', background=[('active', colours["primary"])])

objStyle.configure('Secondary.TButton',font=tplSmallFont, background=colours["actualBorder"], foreground=colours["lightText"], borderwidth=0.5, bordercolor=colours["actualBorder"], relief="flat", focusthickness=0, highlightthickness=0)
objStyle.map('Secondary.TButton', background=[('active', colours["primary"])])

objStyle.configure('Next.TButton', padding= 20, font=tplFontButton, background=colours["actualBorder"], foreground=colours["actualBorder"], borderwidth=0.5, bordercolor=colours["actualBorder"], relief="flat", focusthickness=0, highlightthickness=0)
objStyle.map('Next.TButton', background=[('active', colours["actualBorder"])], foreground=[('active', colours["actualBorder"])])

objStyle.configure('Correct.TButton', padding= 20, font=tplFontButton, background=colours["success"], foreground=colours["lightText"], borderwidth=0.5, bordercolor=colours["actualBorder"], relief="flat", focusthickness=0, highlightthickness=0)
objStyle.map('Correct.TButton', background=[('active', colours["success"])], foreground=[('active', colours["lightText"])])


objStyle.configure('TLabel', background=colours["bg"], foreground=colours["text"])
objStyle.configure('Secondary.TLabel', background=colours["border"], foreground=colours["lightText"])
objStyle.configure('Tertiary.TLabel', background=colours["actualBorder"], foreground=colours["lightText"])

objStyle.configure('Success.TLabel', background=colours["success"], foreground=colours["lightText"])

objStyle.configure('Correct.TLabel', background=colours["border"], foreground=colours["success"])
objStyle.configure('Incorrect.TLabel', background=colours["border"], foreground=colours["warning"])



objStyle.configure('TEntry', background=colours["actualBorder"], foreground=colours["lightText"], fieldbackground=colours["border"], relief="flat",borderwidth=0, highlightthickness=2, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"] )
objStyle.map('TEntry', background=[('focus', colours["actualBorder"]), ('focus', colours["actualBorder"])], foreground=[('focus', colours["lightText"])], highlightcolor=[('focus', colours["actualBorder"])])

objStyle.configure('TFrame', background=colours["border"], highlightthickness=3, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"])

#style.configure('TScrollbar', background=colours["border"],width = 20, foreground=colours["border"], troughcolor=colours["border"], bordercolor=colours["actualBorder"], arrowcolor=colours["actualBorder"], relief="flat", borderwidth=0, highlightthickness=0, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"])

objStyle.configure('TScrollbar', arrowcolor=colours["primary"], relief="flat", arrowsize=0, background=colours["actualBorder"], width=20, foreground=colours["border"], troughcolor=colours["border"], bordercolor=colours["actualBorder"], borderwidth=0, highlightthickness=0, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"])
objStyle.map('TScrollbar', background=[('active', colours["primary"])])

def hideAll():
    """ Hides all the pages """
    page1.hide()
    page2.hide()
    page3.hide()
    page4.hide()
    page5.hide()
    page6.hide()
    page7.hide()
    page8.hide()

def showPage1():
    page1.show()

def showPage2():
    page2.show()

def showPage3():
    page3.show()

def showPage4():
    page4.show()

def showPage5():
    page5.show()

def showPage6():
    page6.show()

def showPage7():
    page7.show()
    
def showPage8():
    page8.show()


class logInPage:
    def onEntryClick(self, event, entryEntryType, strPlaceholder):
            """Function to clear placeholder and enable masking."""
            if strPlaceholder == "Password":
                if entryEntryType.get() == strPlaceholder:
                    entryEntryType.delete(0, tk.END)
                    entryEntryType.config(show='*')
            else:
                if entryEntryType.get() == strPlaceholder:
                    entryEntryType.delete(0, tk.END)
                    

    def onFocusOut(self, event, entryEntryType, strPlaceholder):
            """Function to restore placeholder if field is left empty."""
            if strPlaceholder == "Password":
                if not entryEntryType.get():
                    entryEntryType.insert(0, strPlaceholder)
                    entryEntryType.config(show='') # Show text and change color to grey
            else:
                if not entryEntryType.get():
                    entryEntryType.insert(0, strPlaceholder)
                    entryEntryType.config(show='') # Show text and change color to grey

    def __init__(self):
        super().__init__()
        self.strCurrentUsername = ""
        

        self.lblTitle = ttk.Label(master=app, text="Squiz", font=tplFontTitle, style='TLabel')

        

        self.frmLogin = ttk.Frame(master=app, style='TFrame', width=600, height=400)

        self.entryUsername = ttk.Entry(master=self.frmLogin, width=25, font=tplFontPara, style='TEntry')
        self.entryUsername.insert(0, "Username")

        self.entryUsername.bind('<FocusIn>', lambda event: self.onEntryClick(event, self.entryUsername, "Username"))
        self.entryUsername.bind('<FocusOut>', lambda event: self.onFocusOut(event, self.entryUsername, "Username"))

        self.entryPassword = ttk.Entry(master=self.frmLogin, width=25, font=tplFontPara, style='TEntry')
        self.entryPassword.insert(0, "Password")
        
        self.entryPassword.bind('<FocusIn>', lambda event: self.onEntryClick(event, self.entryPassword, "Password"))
        self.entryPassword.bind('<FocusOut>', lambda event: self.onFocusOut(event, self.entryPassword, "Password"))

        self.btnLogin = ttk.Button(master=self.frmLogin, text="Login", command=self.submit)

        self.btnSignUp = ttk.Button(master=app, text="Sign Up", command=self.goToNewAcc)

    def show(self):
        hideAll()
        self.lblTitle.place(relx=0.5, rely=0.1, anchor="center")
        self.entryUsername.place(relx=0.5, rely=0.3, anchor="center")
        self.entryPassword.place(relx=0.5, rely=0.5, anchor="center")
        self.btnLogin.place(relx=0.5, rely=0.7, anchor="center")
        self.btnSignUp.place(relx=0.9, rely=0.95, anchor="center")
        self.frmLogin.place(relx=0.5, rely=0.5, anchor="center")
        # ensure login widgets are above other stacked widgets (like the canvas)
        try:
            self.frmLogin.lift()
            self.lblTitle.lift()
            self.btnSignUp.lift()
        except Exception:
            pass
        
        

    def hide(self):
        self.lblTitle.place_forget()
        self.entryUsername.place_forget()
        self.entryPassword.place_forget()
        self.btnLogin.place_forget()
        self.btnSignUp.place_forget()
        self.frmLogin.place_forget()

    def goToNewAcc(self):
        showPage3()
        

    def submit(self):
        self.arrUsernames = []
        self.arrPasswords = []

        with open('softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv', mode='r') as file:
            reader = csv.reader(file)
            for arrRow in reader:
                self.arrPasswords.append(arrRow[1])  # Assuming passwords are in the second column
                self.arrUsernames.append(arrRow[0])  # Assuming usernames are in the first column
        
        
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
                    self.strCurrentUsername = self.strUsernameToFind
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
        self.lblQuizzes = ttk.Label(master=app, text="Quizzes", font=tplFontTitle, style='TLabel')
        
        self.frmSideBar = ttk.Frame(app, style='TFrame', width=200, height=800)

        self.intClicks = 0
        self.btnSort = ttk.Button(master=self.frmSideBar, text="Sort", command=self.sort, style='TButton')
        self.btnAdd = ttk.Button(master=self.frmSideBar, text="Add", command=self.add, style='TButton')

        self.btnManageAcc = ttk.Button(master=self.frmSideBar, text="Account", command=self.managePage, style='TButton')

        self.cnvMainPageCanvas = Canvas(app, bg=colours["bg"], highlightthickness=0, borderwidth=0, highlightcolor=colours["bg"], highlightbackground=colours["border"], relief="flat")
        
        
        

        self.scrlbrQuizScrollBar = ttk.Scrollbar(master=self.cnvMainPageCanvas, orient="vertical", command=self.cnvMainPageCanvas.yview, style='TScrollbar')
        
        self.cnvMainPageCanvas.configure(yscrollcommand=self.scrlbrQuizScrollBar.set)
        self.frmScrollableFrame = Frame(self.cnvMainPageCanvas, bg=colours["bg"])

        self.frmScrollableFrame.bind("<Configure>", lambda e: self.cnvMainPageCanvas.configure(scrollregion=self.cnvMainPageCanvas.bbox("all")))

        self.canvasWindow = self.cnvMainPageCanvas.create_window((100, 2), window=self.frmScrollableFrame, anchor="nw")
        


        
        self.lblQuiz = ttk.Label(master=app, text="", font=tplSmallFont, style='Secondary.TLabel')
        self.btnPlay = ttk.Button(master=app, text="Play", command=self.playQuiz, style='Secondary.TButton')
        self.arrQuizLabels = []
        self.arrQuizButtons = []
        self.arrQuizFrames = []
        
        self.arrQuizzes = []

    def getQuizzes(self):
        strUsername = getattr(page1, 'strUsernameToFind', '').strip()
        if not strUsername:
            return

        arrData = []

        with open('softwareDev34/Unit3/AOS1/SATDeleopment/quizzesArray.csv') as file:
            reader = csv.reader(file, delimiter=';')
            for arrRow in reader:
                arrData.append(arrRow)

        arrQuizzesForUser = [row for row in arrData if row[1].strip() == strUsername]

        return arrQuizzesForUser
  
    def playQuiz(self, quiz_index):
        #methodOfPlay = self.quizzes[self.quiz_buttons.index(self.btnPlay)][2]
        page6.getQuizToPlay(quiz_index)
        showPage6()
        
        

    def sort(self):
        
        self.intClicks += 1
        
        intN = len(self.arrQuizzes)

        if self.intClicks % 2 == 0:
            for i in range(intN - 1):
                min_index = i
                for j in range(i + 1, intN):
                    if self.arrQuizzes[j][0].lower() > self.arrQuizzes[min_index][0].lower():
                        min_index = j
                if min_index != i:
                    self.arrQuizzes[i], self.arrQuizzes[min_index] = self.arrQuizzes[min_index], self.arrQuizzes[i]
            self.show(bReloadQuizzes=False)
            return
            
        
        for i in range(intN - 1):
            min_index = i
            for j in range(i + 1, intN):
                if self.arrQuizzes[j][0].lower() < self.arrQuizzes[min_index][0].lower():
                    min_index = j
            if min_index != i:
                self.arrQuizzes[i], self.arrQuizzes[min_index] = self.arrQuizzes[min_index], self.arrQuizzes[i]

        self.show(bReloadQuizzes=False)

    def add(self):
        showPage5()

    def managePage(self):
        page4.show()
        
    def show(self, bReloadQuizzes=True):
        hideAll()
        self.hide()
        if bReloadQuizzes:
            self.arrQuizzes = self.getQuizzes()
        if self.arrQuizzes is None:
            self.arrQuizzes = []
        
        print("Quizzes for user:")
        print(self.arrQuizzes)
        
        self.frmSideBar.place(relx=0, rely=0, anchor="nw", width=200, height=800)

        self.cnvMainPageCanvas.place(relx=0.6, rely=0.5, anchor="center", width=800, height=500)
        self.scrlbrQuizScrollBar.pack(side=RIGHT, fill=Y, padx=(0,50))

        



        for i in range(len(self.arrQuizzes)):
            strQuizTitle = self.arrQuizzes[i][0]

            frmQuiz = ttk.Frame(self.frmScrollableFrame, style='TFrame', width=600, height=50)
            if i == 0:
                frmQuiz.pack(pady=(0,10), padx=10)
            else:
                frmQuiz.pack(pady=10, padx=10)


            lblQuiz = ttk.Label(master=frmQuiz, text=strQuizTitle, font=tplSmallFont, style='Secondary.TLabel')
            btnPlay = ttk.Button(master=frmQuiz, text="Play", command=lambda i=i: self.playQuiz(i), style='Secondary.TButton')

            lblQuiz.place(relx=0.05, rely=0.5, anchor="w")
            btnPlay.place(relx=0.95, rely=0.5, anchor="e")

            self.arrQuizLabels.append(lblQuiz)
            print(btnPlay)
            self.arrQuizButtons.append(btnPlay)
            self.arrQuizFrames.append(frmQuiz)
        print("Quiz buttons:")
        print(self.arrQuizButtons)
        
        self.lblQuizzes.place(relx=0.6, rely=0.1, anchor="center")
        self.btnSort.place(relx=0.5, rely=0.3, anchor="center")
        self.btnAdd.place(relx=0.5, rely=0.5, anchor="center")
        self.btnManageAcc.place(relx=0.5, rely=0.7, anchor="center")

        

    def hide(self):

        for frame in self.arrQuizFrames:
                frame.destroy()

        self.arrQuizLabels.clear()
        self.arrQuizButtons.clear()
        self.arrQuizFrames.clear()
        
        self.frmSideBar.place_forget()

        # lower canvas below the login frame (call with a widget argument)
        # calling lower() with no args raised a TclError on some Tk versions
        try:
            self.cnvMainPageCanvas.lower(page1.frmLogin)
        except Exception:
            # fallback: lower below the root window's first child
            try:
                self.cnvMainPageCanvas.lower()
            except Exception:
                pass
        self.scrlbrQuizScrollBar.pack_forget()

        self.lblQuizzes.place_forget()
        self.btnSort.place_forget()
        self.btnAdd.place_forget()
        self.btnManageAcc.place_forget()
        

class manageAccPage:
    def __init__(self):
        self.lblManageTitle = ttk.Label(master=app, text="Manage", font=tplFontTitle, style='TLabel')
        self.frmManage = ttk.Frame(master=app, style='TFrame', width=600, height=400)
        
        self.btnDone = ttk.Button(master=self.frmManage, text="Done", command=self.done, style='TButton')
        
        self.btnDeleteAcc = ttk.Button(master=self.frmManage, text="Delete Account", command=self.deleteAcc, style='TButton')
        
    def done(self):
        page2.show()
    
    def deleteAcc(self):
        bResponse = messagebox.askyesno(title="Delete Account", message="Are you sure you want to delete your account? This action is not reversible.")

        if bResponse:
            username = getattr(page1, 'strUsernameToFind', '').strip()
            if not username:
                messagebox.showerror(title="Error", message="Could not determine user account to delete.")
                return
            
            
            # Delete from accounts.csv
            strAccountsPath = 'softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv'
            with open(strAccountsPath, mode='r') as file:
                lines = file.readlines()
                
            # Filter out the user's account
            arrUpdatedLines = [line for line in lines if not line.startswith(username + ',')]
                
            with open(strAccountsPath, mode='w') as file:
                file.writelines(arrUpdatedLines)
                
            # Delete from quizzesArray.csv
            strQuizzesPath = 'softwareDev34/Unit3/AOS1/SATDeleopment/quizzesArray.csv'
            with open(strQuizzesPath, mode='r') as file:
                lines = file.readlines()
                
            # Filter out quizzes for this user
            arrUpdatedLines = [line for line in lines if not (';' + username + ';' in line)]
                
            with open(strQuizzesPath, mode='w') as file:
                file.writelines(arrUpdatedLines)
                
            messagebox.showinfo(title="Success", message="Account deleted successfully.")
            showPage1()
            
            
        else:
            pass
        
        
    def show(self):
        hideAll()
        self.lblManageTitle.place(relx=0.5, rely=0.1, anchor="center")
        self.frmManage.place(relx=0.5, rely=0.5, anchor="center")
        self.btnDeleteAcc.place(relx=0.5, rely=0.4, anchor="center")
        self.btnDone.place(relx=0.5, rely=0.6, anchor="center")
        

    def hide(self):
        self.lblManageTitle.place_forget()
        self.frmManage.place_forget()
        self.btnDeleteAcc.place_forget()
        self.btnDone.place_forget()

class newAccPage:
    def __init__(self):
        super().__init__()

        self.lblNewAccount = ttk.Label(master=app, text="Sign Up", font=tplFontTitle, style='TLabel')

        self.frmSignUp = ttk.Frame(master=app, style='TFrame', width=600, height=400)

        
        self.entryNewUsername = ttk.Entry(master=self.frmSignUp, width=25, font=tplFontPara, style='TEntry')
        self.entryNewUsername.insert(0, "Username")

        

        self.entryNewUsername.bind('<FocusIn>', lambda event: page1.onEntryClick(event, self.entryNewUsername, "Username"))
        self.entryNewUsername.bind('<FocusOut>', lambda event: page1.onFocusOut(event, self.entryNewUsername, "Username"))

        self.entryNewPassword = ttk.Entry(master=self.frmSignUp, width=25, font=tplFontPara, style='TEntry')
        self.entryNewPassword.insert(0, "Password")

        self.entryNewPassword.bind('<FocusIn>', lambda event: page1.onEntryClick(event, self.entryNewPassword, "Password"))
        self.entryNewPassword.bind('<FocusOut>', lambda event: page1.onFocusOut(event, self.entryNewPassword, "Password"))

        self.btnSubmit = ttk.Button(master=self.frmSignUp, text="Submit", command=self.createNewAcc, style='TButton')

        self.btnBackToLogin = ttk.Button(master=app, text="Login", command=self.goToLogin, style='TButton')

    def goToLogin(self):
        showPage1()

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
            showPage1()
        else:
            print('Please enter a username')
            messagebox.showwarning(title="Invalid Username", message="Please enter a valid username.")

        

                     
    def show(self):
        hideAll()
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
        
class newQuizPage:
    def __init__(self):
        self.lblNewQuiz = ttk.Label(master=app, text="Create Quiz", font=tplFontTitle, style='TLabel')
        
        self.frmCard = ttk.Frame(master=app, style='TFrame', width=600, height=400)
        
        self.entryQuizTitle = ttk.Entry(master=app, width=35, font=tplFontPara, style='TEntry')
        self.entryQuizTitle.insert(0, "Quiz Title")
        
        self.entryQuizTitle.bind('<FocusIn>', lambda event: page1.onEntryClick(event, self.entryQuizTitle, "Quiz Title"))
        self.entryQuizTitle.bind('<FocusOut>', lambda event: page1.onFocusOut(event, self.entryQuizTitle, "Quiz Title"))
        
        self.entryQuestion = ttk.Entry(master=self.frmCard, width=25, font=tplFontPara, style='TEntry')
        self.entryQuestion.insert(0, "Question")
        
        self.entryQuestion.bind('<FocusIn>', lambda event: page1.onEntryClick(event, self.entryQuestion, "Question"))
        self.entryQuestion.bind('<FocusOut>', lambda event: page1.onFocusOut(event, self.entryQuestion, "Question"))
        
        self.entryAnswer = ttk.Entry(master=self.frmCard, width=25, font=tplFontPara, style='TEntry')
        self.entryAnswer.insert(0, "Answer")
        
        self.entryAnswer.bind('<FocusIn>', lambda event: page1.onEntryClick(event, self.entryAnswer, "Answer"))
        self.entryAnswer.bind('<FocusOut>', lambda event: page1.onFocusOut(event, self.entryAnswer, "Answer"))
        
        
        self.btnNext = ttk.Button(master=app, text="Next Question", command=self.nextQuestion, style='TButton')
        
        self.btnFinish = ttk.Button(master=app, text="Finish", command=self.finishQuiz, style='TButton')
        
        self.btnExit = ttk.Button(master=app, text="Exit", command=self.exit, style='TButton')
        
        self.arrQuizQuestions = []
        self.arrQuizAnswers = []
    
    def exit(self):
        bResponse = messagebox.askyesno(title="Exit", message="Are you sure you want to exit? Your progress will not be saved.")

        if bResponse:
            self.arrQuizQuestions.clear()
            self.arrQuizAnswers.clear()
            showPage2()
        else:
            print("Click 'Yes' to exit!")
            
    def nextQuestion(self):
        if self.entryQuestion.get() == '' or self.entryQuestion.get() == "Question":
            print('Please enter a question')
            messagebox.showwarning(title="Invalid Question", message="Please enter a valid question.")
            return
        
        if len(self.entryQuestion.get()) > 37:
            messagebox.showwarning(title="Invalid Question", message="Please enter a question that is less than 38 characters")
            return

        
        if self.entryAnswer.get() == '' or self.entryAnswer.get() == "Answer":
            print('Please enter an answer')
            messagebox.showwarning(title="Invalid Answer", message="Please enter a valid answer.")
            return
        
        if len(self.entryAnswer.get()) > 13:
            messagebox.showwarning(title="Invalid Answer", message="Please enter an answer that is less than 13 characters")

        
        strQuestion = self.entryQuestion.get()
        strAnswer = self.entryAnswer.get()
        
        print('Get result')
        print(self.entryQuestion.get())
        print(self.entryAnswer.get())
        
        print('Variable result')
        print(strQuestion)
        print(strAnswer)
        
        self.arrQuizQuestions.append(strQuestion)
        self.arrQuizAnswers.append(strAnswer)
        
        print('Append to array')
        print(self.arrQuizQuestions)
        print(self.arrQuizAnswers)
        
        self.entryQuestion.delete(0, tk.END)
        self.entryQuestion.insert(0, "Question")
        self.entryQuestion.config(show='') # Show text and change color to grey
        self.entryAnswer.delete(0, tk.END)
        self.entryAnswer.insert(0, "Answer")
        self.entryAnswer.config(show='') # Show text and change color to grey
    
    def finishQuiz(self):
        
        strQuizTitle = self.entryQuizTitle.get()
        
        if strQuizTitle == '' or strQuizTitle == "Quiz Title":
            print('Please enter a quiz title')
            messagebox.showwarning(title="Invalid Quiz Title", message="Please enter a valid quiz title.")
            return
        
        if len(self.arrQuizQuestions) < 5:
            print('Please enter at least 5 questions')
            messagebox.showwarning(title="Not Enough Questions", message="Please enter at least 5 questions for your quiz.")
            return
        
        
        
        arrQuizData = [strQuizTitle, page1.strCurrentUsername, [[question, answer] for question, answer in zip(self.arrQuizQuestions, self.arrQuizAnswers)]]
        
        
        with open("softwareDev34/Unit3/AOS1/SATDeleopment/quizzesArray.csv", 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([arrQuizData[0], arrQuizData[1], arrQuizData[2]])
            
        print('Quiz saved')
        
        self.arrQuizQuestions.clear()
        self.arrQuizAnswers.clear()
        
        messagebox.showinfo(title="Quiz Saved", message="Your quiz has been saved successfully.")
        showPage2()
        
    
    def show(self):
        hideAll()
        # add widgets here
        
        self.lblNewQuiz.place(relx=0.5, rely=0.1, anchor="center")
        self.frmCard.place(relx=0.5, rely=0.5, anchor="center")
        
        self.entryQuizTitle.place(relx=0.5, rely=0.2, anchor="center")
        self.entryQuestion.place(relx=0.5, rely=0.3, anchor="center")
        self.entryAnswer.place(relx=0.5, rely=0.5, anchor="center")
        self.btnNext.place(relx=0.5, rely=0.7, anchor="center")
        self.btnFinish.place(relx=0.5, rely=0.85, anchor="center")
        self.btnExit.place(relx=0.9, rely=0.95, anchor="center")
        
    
    def hide(self):
        # hide widgets here
        self.lblNewQuiz.place_forget()
        self.frmCard.place_forget()
        self.entryQuestion.place_forget()
        self.entryAnswer.place_forget()
        self.btnNext.place_forget()
        self.btnFinish.place_forget()
        self.btnExit.place_forget()
        self.entryQuizTitle.place_forget()
      
class playQuizPage:
    def __init__(self):
        self.arrQuizToPlay = []
        self.strQuizTitle = ""
        self.frmPlay = ttk.Frame(master=app, style='TFrame', width=600, height=400)
        self.lblPlay = ttk.Label(master=self.frmPlay, text="How would you like to play the quiz?", font=tplFontPara, style='Secondary.TLabel')
        
        
        self.btnFlashCard = ttk.Button(master=self.frmPlay, text="Flashcards", command=self.flashCard, style='TButton')
        self.btnKahoot = ttk.Button(master=self.frmPlay, text="Kahoot", command=self.kahoot, style='TButton')
        
        self.btnCancel = ttk.Button(master=self.frmPlay, text="Cancel", command=self.cancel, style='TButton')
        
    def show(self):
        hideAll()
        # add widgets here
        
        self.frmPlay.place(relx=0.5, rely=0.5, anchor="center")
        self.lblPlay.place(relx=0.5, rely=0.1, anchor="center")
        
        self.btnFlashCard.place(relx=0.5, rely=0.3, anchor="center")
        self.btnKahoot.place(relx=0.5, rely=0.5, anchor="center")
        
        self.btnCancel.place(relx=0.5, rely=0.7, anchor="center")
        
    def getQuizToPlay(self, quiz_index):
        print("Get quiz to play")
        print(quiz_index)
        self.arrQuizToPlay = page2.arrQuizzes[quiz_index][2]
        self.strQuizTitle = page2.arrQuizzes[quiz_index][0]

        self.arrQuizToPlay = eval(self.arrQuizToPlay)  # Convert string representation of list back to a list
        print(self.arrQuizToPlay)
        
    def cancel(self):
        
        showPage2()
        
    def flashCard(self):
        showPage7()
    
    def kahoot(self):
        showPage8()
    
    def hide(self):
        # hide widgets here
        self.lblPlay.place_forget()
        self.frmPlay.place_forget()
        self.btnFlashCard.place_forget()
        self.btnKahoot.place_forget()
        
        self.btnCancel.place_forget()

class flashCardPage:
    def __init__(self):
        self.arrQuiz = page6.arrQuizToPlay
        self.strTitle = page6.strQuizTitle

        self.intClicks = 0

        self.n = 0

        self.lblQuizTitle = ttk.Label(master=app, text=self.strTitle, font=tplFontTitle, style='TLabel')

        self.crdFlashCard = ttk.Frame(master=app, style='TFrame', width=600, height=400)
        self.lblQuestion = ttk.Label(master=self.crdFlashCard, text="", font=tplFontPara, style='Secondary.TLabel')
        self.lblAnswer = ttk.Label(master=self.crdFlashCard, text="", font=tplFontPara, style='Secondary.TLabel')

        self.btnAnswer = ttk.Button(master=app, text="Flip", command=self.flipCard, style='TButton')
        self.btnNextCard = ttk.Button(master=app, text="Next", command=self.nextCard, style='TButton')
        self.btnFinish = ttk.Button(master=app, text="Finish", command=self.finishQuiz, style='TButton')

    def show(self):
        hideAll()
        # add widgets here
        self.lblQuizTitle.config(text=page6.strQuizTitle)
        print("Quiz to play in flashcard page:")
        print(page6.arrQuizToPlay)
        self.lblQuestion.config(text=page6.arrQuizToPlay[self.n][0])
        #self.lblAnswer.config(text=page6.arrQuizToPlay[0][1])
        
        self.btnAnswer.place(relx=0.3, rely=0.8, anchor="center")
        self.btnNextCard.place(relx=0.7, rely=0.8, anchor="center")
        self.btnFinish.place(relx=0.5, rely=0.8, anchor="center")
        
        self.lblQuizTitle.place(relx=0.5, rely=0.1, anchor="center")
        self.crdFlashCard.place(relx=0.5, rely=0.5, anchor="center")
        self.lblQuestion.place(relx=0.5, rely=0.5, anchor="center")
        self.lblAnswer.place(relx=0.5, rely=0.7, anchor="center")

    def flipCard(self):
        self.intClicks += 1

        if self.intClicks % 2 == 0:
            self.lblQuestion.config(text=page6.arrQuizToPlay[self.n][0])
        else:
            self.lblQuestion.config(text=page6.arrQuizToPlay[self.n][1])

    def finishQuiz(self):
        showPage2()

    def nextCard(self):
        # logic to go to the next card
        self.n += 1

        if self.n >= len(page6.arrQuizToPlay):
            self.n = 0
            self.intClicks = 0
            self.lblQuestion.config(text=page6.arrQuizToPlay[self.n][0])
        else:
            self.intClicks = 0
            self.lblQuestion.config(text=page6.arrQuizToPlay[self.n][0])
        
    
    def hide(self):
        # hide widgets here
        self.lblQuizTitle.place_forget()
        self.crdFlashCard.place_forget()
        self.lblQuestion.place_forget()
        self.lblAnswer.place_forget()
        self.btnAnswer.place_forget()
        self.btnNextCard.place_forget()
        self.btnFinish.place_forget()

class kahootPage:
    def __init__(self):

        self.frmSettings = ttk.Frame(master=app, style='TFrame', width=700, height=500)

        #self.lblSettings = ttk.Label(master=self.frmSettings, text="Options", font=smaller_title, style='Tertiary.TLabel')

        self.n = 0

        self.frmResults = ttk.Frame(master=app, style='TFrame', width=600, height=400)

        self.lblResults = ttk.Label(master=app, text="Results", font=tplFontTitle, style='TLabel')

        self.lblCorrect = ttk.Label(master=self.frmResults, text="", font=tplFontTitle, style='Correct.TLabel')

        self.lblIncorrect = ttk.Label(master=self.frmResults, text="", font=tplFontTitle, style='Incorrect.TLabel')

        self.lblPercentage = ttk.Label(master=self.frmResults, text="", font=tplFontTitle, style='Secondary.TLabel')

        self.lblQuizName = ttk.Label(master=self.frmResults, text="", font=tplFontTitle, style='TLabel')

        self.lblCorrectlbl = ttk.Label(master=self.frmResults, text="Correct", font=tplSmallerTitle, style='Secondary.TLabel')

        self.lblIncorrectlbl = ttk.Label(master=self.frmResults, text="Incorrect", font=tplSmallerTitle, style='Secondary.TLabel')

        self.lblKahoot = ttk.Label(master=app, text="Kahoot Mode", font=tplFontTitle, style='TLabel')
        self.btnStart = ttk.Button(master=self.frmSettings, text="Start", command=self.getAnswers, style='TButton')
        self.btnDone = ttk.Button(master=self.frmResults, text="Done", command=self.finishKahoot, style='TButton')
        
        self.lblTimePerQ = ttk.Label(master=app, text="Time per question (seconds):", font=tplFontPara, style='Secondary.TLabel')
        self.entryTimePerQ = ttk.Entry(master=app, width=10, font=tplFontPara, style='TEntry')

        self.lblQuestion = ttk.Label(master=app, text="", font=tplFontTitle, style='TLabel')
        self.entryTimePerQ.insert(0, "30")

        self.entryTimePerQ.bind('<FocusIn>', lambda event: page1.onEntryClick(event, self.entryTimePerQ, "30"))
        self.entryTimePerQ.bind('<FocusOut>', lambda event: page1.onFocusOut(event, self.entryTimePerQ, "30"))

        self.btnAns1 = ttk.Button(master=app, text="GGGGG\nGGGGG", command=self.ans1Selected, style='Next.TButton')
        self.lblAns1 = ttk.Label(master=app, text="", font=tplFontTitle, style='Tertiary.TLabel')

        self.btnAns2 = ttk.Button(master=app, text="GGGGG\nGGGGG", command=self.ans2Selected, style='Next.TButton')
        self.lblAns2 = ttk.Label(master=app, text="", font=tplFontTitle, style='Tertiary.TLabel')

        self.btnAns3 = ttk.Button(master=app, text="GGGGG\nGGGGG", command=self.ans3Selected, style='Next.TButton')
        self.lblAns3 = ttk.Label(master=app, text="", font=tplFontTitle, style='Tertiary.TLabel')
    
        self.btnAns4 = ttk.Button(master=app, text="GGGGG\nGGGGG", command=self.ans4Selected, style='Next.TButton')
        self.lblAns4 = ttk.Label(master=app, text="", font=tplFontTitle, style='Tertiary.TLabel')

        

    def ans1Selected(self):
        print(self.lblAns1.cget('text'))
        if self.lblAns1.cget('text') == self.allAnswers[self.n][self.ansPositions[self.n]]:
            print('corect answer')
            #self.btnAns1.config(style='Correct.TButton')
            #self.lblAns1.configure(style='Success.TLabel')
            #time.sleep(1)
            self.correct +=1

        else:
            print('incorrect')
            self.incorrect +=1
        
        self.n += 1

        

        self.startKahoot()

        

    def ans2Selected(self):
        print(self.lblAns2.cget('text'))
        if self.lblAns2.cget('text') == self.allAnswers[self.n][self.ansPositions[self.n]]:
            print('corect answer')
            #self.btnAns2.config(style='Correct.TButton')
            #self.lblAns2.configure(style='Success.TLabel')
            #time.sleep(1)
            self.correct += 1
        else:
            print('incorrect')
            self.incorrect += 1

        self.n += 1
        

        self.startKahoot()

        

    def ans3Selected(self):
        print(self.lblAns3.cget('text'))
        if self.lblAns3.cget('text') == self.allAnswers[self.n][self.ansPositions[self.n]]:
            print('corect answer')
            #self.btnAns3.config(style='Correct.TButton')
            #self.lblAns3.configure(style='Success.TLabel')
            #time.sleep(1)

            self.correct += 1
        else:
            print('incorrect')
            self.incorrect += 1

        self.n += 1
        

        self.startKahoot()

    def ans4Selected(self):
        print(self.lblAns4.cget('text'))
        if self.lblAns4.cget('text') == self.allAnswers[self.n][self.ansPositions[self.n]]:
            print('corect answer')
            #self.btnAns4.config(style='Correct.TButton')
            #self.lblAns4.configure(style='Success.TLabel')
            #time.sleep(1)
            self.correct += 1
        else:
            print('incorrect')
            self.incorrect += 1

        self.n += 1
        
        self.startKahoot()
    
    def getAnswers(self):
        # logic to start kahoot mode
        
        self.correct = 0
        self.incorrect = 0
        possibleAnswers = []
        self.allAnswers = []
        self.allQuestions = []
        self.ansPositions = []

        for question, answer in page6.arrQuizToPlay:
            for i in range(len(page6.arrQuizToPlay)):
                if page6.arrQuizToPlay[i][1] != answer:
                    possibleAnswers.append(page6.arrQuizToPlay[i][1])

            incorrectAnswers = random.sample(possibleAnswers, 3)

            answerPos = random.randint(0, 3)



            incorrectAnswers.insert(answerPos, answer)
            self.allAnswers.append(incorrectAnswers)
            self.allQuestions.append(question)
            self.ansPositions.append(answerPos)

            print(question)
            print(incorrectAnswers)
            self.lblQuestion.config(text=question)

            possibleAnswers = []

        print(self.allAnswers) 
        print(self.allQuestions)
        hideAll()
        self.startKahoot()
                              
    def finished(self):
        hideAll()

        self.frmResults.place(relx=0.5, rely=0.5, anchor="center")

        self.btnDone.place(relx=0.5, rely=0.9, anchor="center")

        self.lblResults.place(relx=0.5, rely=0.1, anchor="center")

        self.lblIncorrectlbl.place(relx=0.2, rely=0.38, anchor="center")
        self.lblIncorrect.config(text=self.incorrect)
        self.lblIncorrect.place(relx=0.2, rely=0.5, anchor="center")

        self.lblCorrectlbl.place(relx=0.8, rely=0.38, anchor="center")
        self.lblCorrect.config(text=self.correct)
        self.lblCorrect.place(relx=0.8, rely=0.5, anchor="center")

        percentage = (len(self.allQuestions)-self.incorrect)/len(self.allQuestions)*100

        self.lblPercentage.config(text=f'{round(percentage, 2)}%')

        self.lblPercentage.place(relx=0.5, rely=0.5, anchor="center")

        



            
    def startKahoot(self):
        time.sleep(0.1)
        #hide_all()
        '''
        self.btnAns1.config(style='Next.TButton')
        self.lblAns1.configure(style='Tertiary.TLabel')

        self.btnAns2.config(style='Next.TButton')
        self.lblAns2.configure(style='Tertiary.TLabel')

        self.btnAns3.config(style='Next.TButton')
        self.lblAns3.configure(style='Tertiary.TLabel')

        self.btnAns4.config(style='Next.TButton')
        self.lblAns4.configure(style='Tertiary.TLabel')'''

        if self.n >= len(self.allQuestions):
            self.finished()
            return


        self.lblQuestion.config(text=self.allQuestions[self.n])

        #self.btnAns1.config(text=incorrectAnswers[0])
        self.lblAns1.config(text=self.allAnswers[self.n][0])

        #self.btnAns2.config(text=incorrectAnswers[1])
        self.lblAns2.config(text=self.allAnswers[self.n][1])

        #self.btnAns3.config(text=incorrectAnswers[2])
        self.lblAns3.config(text=self.allAnswers[self.n][2])

        #self.btnAns4.config(text=incorrectAnswers[3])
        self.lblAns4.config(text=self.allAnswers[self.n][3])

        self.lblQuestion.place(relx=0.5, rely=0.1, anchor="center")

        self.btnAns1.place(relx=0.25, rely=0.4, anchor="center")
        self.lblAns1.place(relx=0.25, rely=0.4, anchor="center")

        self.btnAns2.place(relx=0.75, rely=0.4, anchor="center")
        self.lblAns2.place(relx=0.75, rely=0.4, anchor="center")

        self.btnAns3.place(relx=0.25, rely=0.8, anchor="center")
        self.lblAns3.place(relx=0.25, rely=0.8, anchor="center")

        self.btnAns4.place(relx=0.75, rely=0.8, anchor="center") 
        self.lblAns4.place(relx=0.75, rely=0.8, anchor="center") 


            

       

           

    def finishKahoot(self):
        showPage2()

    def show(self):
        hideAll()
        # add widgets here
        #self.lblSettings.place(relx=0.5, rely=0.1, anchor="center")
        self.lblKahoot.place(relx=0.5, rely=0.1, anchor="center")
        self.btnStart.place(relx=0.5, rely=0.9, anchor="center")
        self.frmSettings.place(relx=0.5, rely=0.5, anchor="center")
        self.lblTimePerQ.place(relx=0.5, rely=0.4, anchor="center")
        self.entryTimePerQ.place(relx=0.5, rely=0.5, anchor="center")
        #self.btnFinish.place(relx=0.5, rely=0.7, anchor="center")
        
    
    def hide(self):
        # hide widgets here
        self.lblKahoot.place_forget()
        self.btnStart.place_forget()
        self.frmSettings.place_forget()
        self.lblTimePerQ.place_forget()
        self.entryTimePerQ.place_forget()
        self.btnDone.place_forget()
        self.btnAns1.place_forget()
        self.btnAns3.place_forget()
        self.btnAns4.place_forget()
        self.btnAns2.place_forget()

        self.lblAns1.place_forget()
        self.lblAns2.place_forget()
        self.lblAns3.place_forget()
        self.lblAns4.place_forget()

        self.lblQuestion.place_forget()

        self.lblIncorrect.place_forget()
        self.lblIncorrectlbl.place_forget()

        self.lblCorrect.place_forget()
        self.lblCorrectlbl.place_forget()

        self.lblPercentage.place_forget()

        self.frmResults.place_forget()

        self.btnDone.place_forget()
        
        self.lblResults.place_forget()


page1 = logInPage()

page2 = mainPage()

page3 = newAccPage()

page4 = manageAccPage()

page5 = newQuizPage()

page6 = playQuizPage()

page7 = flashCardPage()

page8 = kahootPage()





showPage1()


app.mainloop()
