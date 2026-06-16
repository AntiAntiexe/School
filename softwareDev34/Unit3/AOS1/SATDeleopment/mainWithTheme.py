import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv



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
small_font = ("Helvetica", 20, "normal")
verticalFont = ("Helvetica", 150, "normal")

style = ttk.Style()
style.theme_use('classic')



style.configure('TButton',font=font_para, background=colours["actualBorder"], foreground=colours["lightText"], borderwidth=0.5, bordercolor=colours["actualBorder"], relief="flat", focusthickness=0, highlightthickness=0)
style.map('TButton', background=[('active', colours["primary"])])

style.configure('Secondary.TButton',font=small_font, background=colours["actualBorder"], foreground=colours["lightText"], borderwidth=0.5, bordercolor=colours["actualBorder"], relief="flat", focusthickness=0, highlightthickness=0)
style.map('Secondary.TButton', background=[('active', colours["primary"])])

style.configure('Next.TButton',font=font_para, background=colours["success"], foreground=colours["lightText"], borderwidth=0.5, bordercolor=colours["actualBorder"], relief="flat", focusthickness=0, highlightthickness=0)
style.map('Next.TButton', background=[('active', colours["primary"])], foreground=[('active', colours["lightText"])])


style.configure('TLabel', background=colours["bg"], foreground=colours["text"])
style.configure('Secondary.TLabel', background=colours["border"], foreground=colours["lightText"])

style.configure('TEntry', background=colours["actualBorder"], foreground=colours["lightText"], fieldbackground=colours["border"], relief="flat",borderwidth=0, highlightthickness=2, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"] )
style.map('TEntry', background=[('focus', colours["actualBorder"]), ('focus', colours["actualBorder"])], foreground=[('focus', colours["lightText"])], highlightcolor=[('focus', colours["actualBorder"])])

style.configure('TFrame', background=colours["border"], highlightthickness=3, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"])

#style.configure('TScrollbar', background=colours["border"],width = 20, foreground=colours["border"], troughcolor=colours["border"], bordercolor=colours["actualBorder"], arrowcolor=colours["actualBorder"], relief="flat", borderwidth=0, highlightthickness=0, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"])

style.configure('TScrollbar', arrowcolor=colours["primary"], relief="flat", arrowsize=0, background=colours["actualBorder"], width=20, foreground=colours["border"], troughcolor=colours["border"], bordercolor=colours["actualBorder"], borderwidth=0, highlightthickness=0, highlightcolor=colours["actualBorder"], highlightbackground=colours["actualBorder"])
style.map('TScrollbar', background=[('active', colours["primary"])])

def hide_all():
    """ Hides all the pages """
    page1.hide()
    page2.hide()
    page3.hide()
    page4.hide()
    page5.hide()
    page6.hide()
    page7.hide()
    page8.hide()

def show_page1():
    page1.show()

def show_page2():
    page2.show()

def show_page3():
    page3.show()

def show_page4():
    page4.show()

def show_page5():
    page5.show()

def show_page6():
    page6.show()

def show_page7():
    page7.show()
    
def show_page8():
    page8.show()


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
        # ensure login widgets are above other stacked widgets (like the canvas)
        try:
            self.frLogin.lift()
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
        
        self.sideBar = ttk.Frame(app, style='TFrame', width=200, height=800)

        self.clicks = 0
        self.btnSort = ttk.Button(master=self.sideBar, text="Sort", command=self.sort, style='TButton')
        self.btnAdd = ttk.Button(master=self.sideBar, text="Add", command=self.add, style='TButton')

        self.manageAccBut = ttk.Button(master=self.sideBar, text="Account", command=self.managePage, style='TButton')

        self.canvas = Canvas(app, bg=colours["bg"], highlightthickness=0, borderwidth=0, highlightcolor=colours["bg"], highlightbackground=colours["border"], relief="flat")
        
        
        

        self.scrollbar = ttk.Scrollbar(master=self.canvas, orient="vertical", command=self.canvas.yview, style='TScrollbar')
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_frame = Frame(self.canvas, bg=colours["bg"])

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas_window = self.canvas.create_window((100, 2), window=self.scrollable_frame, anchor="nw")
        


        
        self.lblQuiz = ttk.Label(master=app, text="", font=small_font, style='Secondary.TLabel')
        self.btnPlay = ttk.Button(master=app, text="Play", command=self.playQuiz, style='Secondary.TButton')
        self.quiz_labels = []
        self.quiz_buttons = []
        self.quiz_frames = []
        
        self.quizzes = []

    def getQuizzes(self):
        username = getattr(page1, 'strUsernameToFind', '').strip()
        if not username:
            return

        data = []

        with open('softwareDev34/Unit3/AOS1/SATDeleopment/quizzesArray.csv') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                data.append(row)

        rquizzes_for_user = [row for row in data if row[1].strip() == username]

        return rquizzes_for_user
  
    def playQuiz(self):
        #methodOfPlay = self.quizzes[self.quiz_buttons.index(self.btnPlay)][2]
        page6.getQuizToPlay()
        show_page6()
        
        '''
        win = Toplevel()
        win.title('warning')
        win.configure(bg=colours["bg"])
        
        lblPlay = ttk.Label(master=win, text="How would you like to play the quiz?", font=font_para, style='TLabel').pack(pady=20, padx=20)
        
        show_page6()
        
        def flashCard():
            win.destroy()
            show_page7()
        
        def kahoot():
            win.destroy()
            show_page8()
        
        btnFlashCard = ttk.Button(master=win, text="Flashcards", command=flashCard, style='TButton').pack(pady=10, padx=20)
        btnKahoot = ttk.Button(master=win, text="Kahoot", command=kahoot, style='TButton').pack(pady=10, padx=20)'''
        
        
        
        #methodOFPlay = messagebox.askquestion(title="Play Quiz", message="How would you like to play the quiz?", icon='question', type='yesnocancel', default='yes', detail="Yes: Play as Quiz\nNo: Play as Flashcards\nCancel: Play as Kahoot")
        

    def sort(self):
        
        self.clicks += 1
        
        n = len(self.quizzes)

        if self.clicks % 2 == 0:
            for i in range(n - 1):
                min_index = i
                for j in range(i + 1, n):
                    if self.quizzes[j][0].lower() > self.quizzes[min_index][0].lower():
                        min_index = j
                if min_index != i:
                    self.quizzes[i], self.quizzes[min_index] = self.quizzes[min_index], self.quizzes[i]
            self.show(reload_quizzes=False)
            return
            
        
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if self.quizzes[j][0].lower() < self.quizzes[min_index][0].lower():
                    min_index = j
            if min_index != i:
                self.quizzes[i], self.quizzes[min_index] = self.quizzes[min_index], self.quizzes[i]

        self.show(reload_quizzes=False)

    def add(self):
        show_page5()

    def managePage(self):
        page4.show()
        
    def show(self, reload_quizzes=True):
        hide_all()
        self.hide()
        if reload_quizzes:
            self.quizzes = self.getQuizzes()
        if self.quizzes is None:
            self.quizzes = []
        
        print("Quizzes for user:")
        print(self.quizzes)
        
        self.sideBar.place(relx=0, rely=0, anchor="nw", width=200, height=800)

        self.canvas.place(relx=0.6, rely=0.5, anchor="center", width=800, height=500)
        self.scrollbar.pack(side=RIGHT, fill=Y, padx=(0,50))

        



        for i in range(len(self.quizzes)):
            strQuizTitle = self.quizzes[i][0]

            frmQuiz = ttk.Frame(self.scrollable_frame, style='TFrame', width=600, height=50)
            if i == 0:
                frmQuiz.pack(pady=(0,10), padx=10)
            else:
                frmQuiz.pack(pady=10, padx=10)


            lblQuiz = ttk.Label(master=frmQuiz, text=strQuizTitle, font=small_font, style='Secondary.TLabel')
            self.btnPlay = ttk.Button(master=frmQuiz, text="Play", command=self.playQuiz, style='Secondary.TButton')

            lblQuiz.place(relx=0.05, rely=0.5, anchor="w")
            self.btnPlay.place(relx=0.95, rely=0.5, anchor="e")

            self.quiz_labels.append(lblQuiz)
            print(self.btnPlay)
            self.quiz_buttons.append(self.btnPlay)
            self.quiz_frames.append(frmQuiz)
        print("Quiz buttons:")
        print(self.quiz_buttons)
        
        self.hello.place(relx=0.6, rely=0.1, anchor="center")
        self.btnSort.place(relx=0.5, rely=0.3, anchor="center")
        self.btnAdd.place(relx=0.5, rely=0.5, anchor="center")
        self.manageAccBut.place(relx=0.5, rely=0.7, anchor="center")

        

    def hide(self):

        for frame in self.quiz_frames:
                frame.destroy()

        self.quiz_labels.clear()
        self.quiz_buttons.clear()
        self.quiz_frames.clear()
        
        self.sideBar.place_forget()

        # lower canvas below the login frame (call with a widget argument)
        # calling lower() with no args raised a TclError on some Tk versions
        try:
            self.canvas.lower(page1.frLogin)
        except Exception:
            # fallback: lower below the root window's first child
            try:
                self.canvas.lower()
            except Exception:
                pass
        self.scrollbar.pack_forget()

        self.hello.place_forget()
        self.btnSort.place_forget()
        self.btnAdd.place_forget()
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
        
class newQuizPage:
    def __init__(self):
        self.lblNewQuiz = ttk.Label(master=app, text="Create Quiz", font=font_title, style='TLabel')
        
        self.frmCard = ttk.Frame(master=app, style='TFrame', width=600, height=400)
        
        self.entryQuizTitle = ttk.Entry(master=app, width=35, font=font_para, style='TEntry')
        self.entryQuizTitle.insert(0, "Quiz Title")
        
        self.entryQuizTitle.bind('<FocusIn>', lambda event: page1.on_entry_click(event, self.entryQuizTitle, "Quiz Title"))
        self.entryQuizTitle.bind('<FocusOut>', lambda event: page1.on_focusout(event, self.entryQuizTitle, "Quiz Title"))
        
        self.entryQuestion = ttk.Entry(master=self.frmCard, width=25, font=font_para, style='TEntry')
        self.entryQuestion.insert(0, "Question")
        
        self.entryQuestion.bind('<FocusIn>', lambda event: page1.on_entry_click(event, self.entryQuestion, "Question"))
        self.entryQuestion.bind('<FocusOut>', lambda event: page1.on_focusout(event, self.entryQuestion, "Question"))
        
        self.entryAnswer = ttk.Entry(master=self.frmCard, width=25, font=font_para, style='TEntry')
        self.entryAnswer.insert(0, "Answer")
        
        self.entryAnswer.bind('<FocusIn>', lambda event: page1.on_entry_click(event, self.entryAnswer, "Answer"))
        self.entryAnswer.bind('<FocusOut>', lambda event: page1.on_focusout(event, self.entryAnswer, "Answer"))
        
        self.photo = PhotoImage(file="softwareDev34/Unit3/AOS1/SATDeleopment/whiteArrowIcon.png")
        
        self.photoimage = self.photo.subsample(20, 20)  # Adjust the subsample values as needed to resize the image
        
        
        self.btnNext = ttk.Button(master=app, text="Next Question", command=self.nextQuestion, style='TButton')
        
        self.btnFinish = ttk.Button(master=app, text="Finish", command=self.finishQuiz, style='TButton')
        
        self.btnExit = ttk.Button(master=app, text="Exit", command=self.exit, style='TButton')
        
        self.arrQuizQuestions = []
        self.arrQuizAnswers = []
        
    
    def exit(self):
        response = messagebox.askyesno(title="Exit", message="Are you sure you want to exit? Your progress will not be saved.")

        if response:
            self.arrQuizQuestions.clear()
            self.arrQuizAnswers.clear()
            show_page2()
        else:
            print("Click 'Yes' to exit!")
            
    def nextQuestion(self):
        if self.entryQuestion.get() == '' or self.entryQuestion.get() == "Question":
            print('Please enter a question')
            messagebox.showwarning(title="Invalid Question", message="Please enter a valid question.")
            return
        
        if self.entryAnswer.get() == '' or self.entryAnswer.get() == "Answer":
            print('Please enter an answer')
            messagebox.showwarning(title="Invalid Answer", message="Please enter a valid answer.")
            return
        
        question = self.entryQuestion.get()
        answer = self.entryAnswer.get()
        
        print('Get result')
        print(self.entryQuestion.get())
        print(self.entryAnswer.get())
        
        print('Variable result')
        print(question)
        print(answer)
        
        self.arrQuizQuestions.append(question)
        self.arrQuizAnswers.append(answer)
        
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
        
        quizTitle = self.entryQuizTitle.get()
        
        if quizTitle == '' or quizTitle == "Quiz Title":
            print('Please enter a quiz title')
            messagebox.showwarning(title="Invalid Quiz Title", message="Please enter a valid quiz title.")
            return
        
        if len(self.arrQuizQuestions) < 5:
            print('Please enter at least 5 questions')
            messagebox.showwarning(title="Not Enough Questions", message="Please enter at least 5 questions for your quiz.")
            return
        
        
        
        quizData = [quizTitle, page1.current_username, [[question, answer] for question, answer in zip(self.arrQuizQuestions, self.arrQuizAnswers)]]
        
        
        with open("softwareDev34/Unit3/AOS1/SATDeleopment/quizzesArray.csv", 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([quizData[0], quizData[1], quizData[2]])
            
        print('Quiz saved')
        
        self.arrQuizQuestions.clear()
        self.arrQuizAnswers.clear()
        
        messagebox.showinfo(title="Quiz Saved", message="Your quiz has been saved successfully.")
        show_page2()
        
    
    def show(self):
        hide_all()
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
        
        #self.quizToPlay = page2.quizzes[page2.quiz_buttons.index(page2.btnPlay)][2]
        
        print("quiz button to play:")
        print(page2.btnPlay)
        
        #print(self.quizToPlay)
        
        self.frmPlay = ttk.Frame(master=app, style='TFrame', width=600, height=400)
        self.lblPlay = ttk.Label(master=self.frmPlay, text="How would you like to play the quiz?", font=font_para, style='Secondary.TLabel')
        
        
        self.btnFlashCard = ttk.Button(master=self.frmPlay, text="Flashcards", command=self.flashCard, style='TButton')
        self.btnKahoot = ttk.Button(master=self.frmPlay, text="Kahoot", command=self.kahoot, style='TButton')
        
        self.btnCancel = ttk.Button(master=self.frmPlay, text="Cancel", command=self.cancel, style='TButton')
        
    def show(self):
        hide_all()
        # add widgets here
        
        self.frmPlay.place(relx=0.5, rely=0.5, anchor="center")
        self.lblPlay.place(relx=0.5, rely=0.1, anchor="center")
        
        self.btnFlashCard.place(relx=0.5, rely=0.3, anchor="center")
        self.btnKahoot.place(relx=0.5, rely=0.5, anchor="center")
        
        self.btnCancel.place(relx=0.5, rely=0.7, anchor="center")
        
    def getQuizToPlay(self):
        print("Get quiz to play")
        print(page2.btnPlay)
        #quizToPlay = page2.quizzes[page2.quiz_buttons.index(page2.btnPlay)][2]
        #print(quizToPlay)
        
    def cancel(self):
        
        show_page2()
        
    def flashCard(self):
        show_page7()
    
    def kahoot(self):
        show_page8()
    
    def hide(self):
        # hide widgets here
        self.lblPlay.place_forget()
        self.frmPlay.place_forget()
        self.btnFlashCard.place_forget()
        self.btnKahoot.place_forget()
        
        self.btnCancel.place_forget()

class flashCardPage:
    def __init__(self):
        pass
    def show(self):
        hide_all()
        # add widgets here
        
    
    def hide(self):
        # hide widgets here
        pass

class kahootPage:
    def __init__(self):
        pass
    def show(self):
        hide_all()
        # add widgets here
        
    
    def hide(self):
        # hide widgets here
        pass



page1 = logInPage()

page2 = mainPage()

page3 = newAccPage()

page4 = manageAccPage()

page5 = newQuizPage()

page6 = playQuizPage()

page7 = flashCardPage()

page8 = kahootPage()





show_page1()


app.mainloop()
