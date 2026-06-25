"""
Squiz - A quiz creation and study application.
VCE Software Development - Unit 4 AOS1

OOP Language: Python 3  |  GUI Library: Tkinter
Naming convention: Hungarian Notation
File formats used: CSV (delimited)

Inheritance hierarchy:
    BasePage
    ├ FormPage          (generalises shared form-entry behaviour)
    │   ├ logInPage     (page 1)
    │   ├ newAccPage    (page 3)
    │   ├ newQuizPage   (page 5)
    │   └ kahootPage    (page 8)
    ├ mainPage          (page 2)
    ├ manageAccPage     (page 4)
    ├ playQuizPage      (page 6)
    └ flashCardPage     (page 7)
"""

import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv



#  CONSTANTS  (global)
strAccountsPath  = 'softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv'
strQuizzesPath   = 'softwareDev34/Unit3/AOS1/SATDeleopment/quizzesArray.csv'


#  COLOUR PALETTE  (global)
dictColours = {
    "bg":          "#12162b",   # deep-space navy – main window background
    "card":        "#1c2340",   # slightly lighter card / frame surface
    "sidebar":     "#161b34",   # sidebar panel background
    "text":        "#e2e8ff",   # primary text (near-white with blue tint)
    "lightText":   "#ffffff",   # pure-white text for dark backgrounds
    "muted":       "#6b7db3",   # placeholder / secondary muted text
    "primary":     "#4d84f5",   # Squiz brand blue – primary interactive colour
    "primaryHov":  "#3669d6",   # primary hover / active state
    "success":     "#3ecf8e",   # correct answer / success green
    "danger":      "#e05c6b",   # delete / destructive action red
    "dangerHov":   "#c0394a",   # danger hover
    "warning":     "#f0a03c",   # incorrect answer / warning amber
    "border":      "#252d4a",   # subtle card border
    "inputBg":     "#1e2540",   # entry-field background
    "highlight":   "#5c6bc0",   # accent purple for hover states
    "answerTile":  "#232c50",   # Kahoot answer tile background
}


#  APPLICATION WINDOW
app = tk.Tk()
app.title("Squiz")
app.geometry("1100x800")
app.resizable(False, False)
app.configure(bg=dictColours["bg"])


#  FONTS  (global font types)
tplFontTitle    = ("Helvetica", 48, "bold")     # page headings
tplFontSubTitle = ("Helvetica", 28, "bold")     # section headings
tplFontPara     = ("Helvetica", 22, "normal")   # body / entry text
tplSmallBold    = ("Helvetica", 16, "bold")     # quiz card title
tplSmallFont    = ("Helvetica", 16, "normal")   # muted / secondary text
tplFontAnswer   = ("Helvetica", 18, "bold")     # Kahoot answer label text
tplFontHuge     = ("Helvetica", 72, "bold")     # large score numbers



#  TTK STYLE CONFIGURATION


ttkStyle = ttk.Style()
ttkStyle.theme_use('classic')

#  Buttons ─

# Primary action button (large)
ttkStyle.configure('TButton', font=tplFontPara, background=dictColours["primary"], foreground=dictColours["lightText"], borderwidth=0, relief="flat", focusthickness=0, highlightthickness=0, padding=(24, 10))
ttkStyle.map('TButton', background=[('active', dictColours["primaryHov"])])

# Secondary / smaller button
ttkStyle.configure('Secondary.TButton', font=tplSmallFont, background=dictColours["primary"], foreground=dictColours["lightText"], borderwidth=0, relief="flat", focusthickness=0, highlightthickness=0, padding=(14, 7))
ttkStyle.map('Secondary.TButton', background=[('active', dictColours["primaryHov"])])

# Ghost sidebar button
ttkStyle.configure('Sidebar.TButton', font=tplSmallFont, background=dictColours["sidebar"], foreground=dictColours["muted"], borderwidth=0, relief="flat", focusthickness=0, highlightthickness=0, padding=(14, 10))
ttkStyle.map('Sidebar.TButton', background=[('active', dictColours["border"])], foreground=[('active', dictColours["text"])])

# Destructive / danger button
ttkStyle.configure('Danger.TButton', font=tplFontPara, background=dictColours["danger"], foreground=dictColours["lightText"], borderwidth=0, relief="flat", focusthickness=0, highlightthickness=0, padding=(24, 10))
ttkStyle.map('Danger.TButton', background=[('active', dictColours["dangerHov"])])

# Kahoot answer tile (large square button – text hidden; label is overlaid)
ttkStyle.configure('Tile.TButton', padding=20, font=("Helvetica", 60), background=dictColours["answerTile"], foreground=dictColours["answerTile"], borderwidth=0, relief="flat", focusthickness=0, highlightthickness=0)
ttkStyle.map('Tile.TButton', background=[('active', dictColours["border"])], foreground=[('active', dictColours["border"])])

#  Labels 

ttkStyle.configure('TLabel', background=dictColours["bg"], foreground=dictColours["text"])
ttkStyle.configure('Card.TLabel', background=dictColours["card"], foreground=dictColours["text"])
ttkStyle.configure('Muted.TLabel', background=dictColours["bg"], foreground=dictColours["muted"])
ttkStyle.configure('MutedCard.TLabel', background=dictColours["card"], foreground=dictColours["muted"])
ttkStyle.configure('Sidebar.TLabel', background=dictColours["sidebar"], foreground=dictColours["muted"])
ttkStyle.configure('SidebarTitle.TLabel', background=dictColours["sidebar"], foreground=dictColours["lightText"])
ttkStyle.configure('Success.TLabel', background=dictColours["card"], foreground=dictColours["success"])
ttkStyle.configure('Warning.TLabel', background=dictColours["card"], foreground=dictColours["warning"])
ttkStyle.configure('TileText.TLabel', background=dictColours["answerTile"], foreground=dictColours["lightText"])

#  Entry fields 

ttkStyle.configure('TEntry', background=dictColours["inputBg"], foreground=dictColours["lightText"], fieldbackground=dictColours["inputBg"], relief="flat", borderwidth=0, insertcolor=dictColours["lightText"])

#  Frames 

ttkStyle.configure('TFrame', background=dictColours["card"])
ttkStyle.configure('Sidebar.TFrame', background=dictColours["sidebar"])
ttkStyle.configure('BG.TFrame', background=dictColours["bg"])

#  Scrollbar ─

ttkStyle.configure('TScrollbar', arrowcolor=dictColours["primary"], relief="flat", arrowsize=0, background=dictColours["border"], width=6, troughcolor=dictColours["card"], bordercolor=dictColours["card"], borderwidth=0, highlightthickness=0)
ttkStyle.map('TScrollbar', background=[('active', dictColours["primary"])])



#  PAGE NAVIGATION HELPERS  (global functions)


def hideAll():
    """
    Hide every page so the target page can be shown cleanly.
    Called before any show() method to avoid widget overlap.
    """
    page1.hide()
    page2.hide()
    page3.hide()
    page4.hide()
    page5.hide()
    page6.hide()
    page7.hide()
    page8.hide()

def showPage1():
    """Navigate to the Login page (page 1)."""
    page1.show()

def showPage2():
    """Navigate to the Main dashboard (page 2)."""
    page2.show()

def showPage3():
    """Navigate to the Sign-Up page (page 3)."""
    page3.show()

def showPage4():
    """Navigate to the Manage Account page (page 4)."""
    page4.show()

def showPage5():
    """Navigate to the Create Quiz page (page 5)."""
    page5.show()

def showPage6():
    """Navigate to the Play Mode Selection page (page 6)."""
    page6.show()

def showPage7():
    """Navigate to the Flashcard Mode page (page 7)."""
    page7.show()

def showPage8():
    """Navigate to the Kahoot/Quiz Mode page (page 8)."""
    page8.show()



#  BASE PAGE  –  Abstraction & Generalisation


class BasePage:
    """
    Abstract base class for every page in the application.

    OOP Principles demonstrated:
      • Abstraction - the internal implementation of each page is
                         hidden; only show() and hide() are exposed.
      • Generalisation - common behaviour (_set_placeholder) is defined
                         once here and shared by all sub-classes.

    All eight page classes inherit from BasePage (or its sub-class
    FormPage), satisfying the requirement for classes, objects,
    inheritance, and access modifiers.
    """

    def show(self):
        """Display this page.  Must be overridden in every sub-class."""
        pass

    def hide(self):
        """Hide this page.  Must be overridden in every sub-class."""
        pass

    def setPlaceholder(self, entryWidget, strPlaceholder):
        """
        Protected helper - restore placeholder text in an Entry widget.

        Using the 'protected' naming convention (_prefix) signals that
        this method is for internal / sub-class use, not external callers.

        Parameters
        ----------
        entry_widget  : ttk.Entry - the widget whose text will be reset
        strPlaceholder       - the string which will be present in the entry field before typing
        """
        entryWidget.delete(0, tk.END)          # clear current content
        entryWidget.insert(0, strPlaceholder)  # restore placeholder text
        entryWidget.config(show='') # un-mask any password masking



#  FORM PAGE  –  Generalisation & Inheritance


class FormPage(BasePage):
    """
    Intermediate class for pages that contain Entry widgets with
    placeholder text.

    Inherits from BasePage and generalises two shared behaviours:
      • on_entry_click - clears placeholder on focus-in
      • on_focusout    - restores placeholder on focus-out

    Sub-classes: logInPage, newAccPage, newQuizPage, kahootPage.
    Avoids code duplication and demonstrates Inheritance.
    """

    def onEntryClick(self, event, entryWidget, strPlaceholder):
        """
        Clear placeholder text when a user clicks into an Entry field.
        For password fields the characters are masked with '*'.

        Parameters
        ----------
        event         : tkinter event object (unused, required by bind)
        entry_widget  : ttk.Entry - widget that received focus
        strPlaceholder:       - the placeholder string currently shown, string as it is in an entry field
        """
        if entryWidget.get() == strPlaceholder:   # equality comparison
            entryWidget.delete(0, tk.END)
            if strPlaceholder == "Password":        # selection
                entryWidget.config(show='*')       # mask password characters

    def onFocusOut(self, event, entryWidget, strPlaceholder: str):
        """
        Restore placeholder text when the user leaves an empty Entry.

        Parameters
        ----------
        event         : tkinter event object (unused, required by bind)
        entry_widget  : ttk.Entry - widget that lost focus
        strPlaceholder: string   - placeholder string to restore, string as it is in an entry field
        """
        if not entryWidget.get():              # existence check (logical NOT)
            self.setPlaceholder(entryWidget, strPlaceholder)



#  PAGE 1 – LOGIN PAGE      logInPage(FormPage)


class logInPage(FormPage):
    """
    Login page - authenticates existing users against accounts.csv.

    Algorithm: Binary Search
        The accounts CSV is sorted alphabetically by username.
        Binary search locates the entered username in O(log n) time.

    Data structures:
        __arrUsernames - 1-D array (list[str]) of all usernames from CSV
        __arrPasswords - 1-D array (list[str]) of matching passwords

    Validation:
        • Existence check - username and password fields must not be
                            empty or contain the placeholder text
    """

    def __init__(self):
        """Initialise all widgets for the login page."""
        super().__init__()
        
        

        # Public attribute 
        self.strCurrentUsername = ""   # str – stores the logged-in username
        self.strUsernameToFind = ""  # str – last validated username

        # Private 1-D arrays (populated on each submit)
        self.arrUsernames = []   # list[str] – 1-D array of usernames
        self.arrPasswords = []   # list[str] – 1-D array of passwords

        # Widgets 
        self.lblTitle = ttk.Label(master=app, text="Squiz", font=tplFontTitle, style='TLabel')

        self.lblSubtitle = ttk.Label(master=app, text="Create, study, succeed.", font=tplSmallFont, style='Muted.TLabel')

        self.frLogin = ttk.Frame(master=app, style='TFrame', width=480, height=360)

        self.lblFormTitle = ttk.Label(master=self.frLogin, text="Welcome back", font=tplFontSubTitle, style='Card.TLabel')

        self.entryUsername = ttk.Entry(master=self.frLogin, width=22, font=tplFontPara, style='TEntry')
        self.entryUsername.insert(0, "Username")

        self.entryPassword = ttk.Entry(master=self.frLogin, width=22, font=tplFontPara, style='TEntry')
        self.entryPassword.insert(0, "Password")

        self.btnLogin = ttk.Button(master=self.frLogin, text="Log In", command=self.submit)

        self.lblNoAccount = ttk.Label(master=app, text="Don't have an account?", font=tplSmallFont, style='Muted.TLabel')

        self.btnSignUp = ttk.Button(master=app, text="Sign Up", command=self.goToNewAcc, style='Secondary.TButton')

        # Bind placeholder focus events (inherited from FormPage)
        self.entryUsername.bind('<FocusIn>', lambda event: self.onEntryClick(event, self.entryUsername, "Username"))
        self.entryUsername.bind('<FocusOut>', lambda event: self.onFocusOut(event, self.entryUsername, "Username"))
        self.entryPassword.bind('<FocusIn>', lambda event: self.onEntryClick(event, self.entryPassword, "Password"))
        self.entryPassword.bind('<FocusOut>', lambda event: self.onFocusOut(event, self.entryPassword, "Password"))
        
        # Allow the Enter key to submit
        self.entryPassword.bind('<Return>', lambda event: self.submit())

    #  Public methods 

    def show(self):
        """Display the login page and bring widgets to the front."""
        hideAll()
        self.lblTitle.place(relx=0.5, rely=0.10, anchor="center")
        self.lblSubtitle.place(relx=0.5, rely=0.19, anchor="center")
        self.frLogin.place(relx=0.5, rely=0.54, anchor="center")
        self.lblFormTitle.place(relx=0.5, rely=0.14, anchor="center")
        self.entryUsername.place(relx=0.5, rely=0.35, anchor="center")
        self.entryPassword.place(relx=0.5, rely=0.55, anchor="center")
        self.btnLogin.place(relx=0.5, rely=0.76, anchor="center")
        self.lblNoAccount.place(relx=0.5, rely=0.88, anchor="center")
        self.btnSignUp.place(relx=0.5, rely=0.93, anchor="center")
        # Lift above the main-page canvas that sits behind this page
        
        self.frLogin.lift()
        self.lblTitle.lift()
        self.lblSubtitle.lift()
        self.lblNoAccount.lift()
        self.btnSignUp.lift()
        

    def hide(self):
        """Remove all login widgets from the screen."""
        for w in (self.lblTitle, self.lblSubtitle, self.frLogin,
                  self.lblFormTitle, self.entryUsername,
                  self.entryPassword, self.btnLogin,
                  self.lblNoAccount, self.btnSignUp):
            w.place_forget()

    def goToNewAcc(self):
        """Navigate to the Sign-Up page."""
        showPage3()

    def submit(self):
        """
        Read accounts.csv into 1-D arrays and run a Binary Search to
        authenticate the entered username/password combination.

        Binary Search requires the array to be sorted A-Z by username.
        Time complexity: O(log n)

        Validation applied:
            • Existence check - both fields must contain non-empty,
                                non-placeholder text before the search runs
        """
        #  Load accounts into 1-D arrays from CSV (read from data source)
        self.arrUsernames = []
        self.arrPasswords = []
        
        with open(strAccountsPath, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.arrUsernames.append(row[0])   # text (str) – username
                self.arrPasswords.append(row[1])   # text (str) – password

        # Sort the accounts with Quick Sort
        if self.arrUsernames:
            stack = [(0, len(self.arrUsernames) - 1)]
            while stack:
                intLow, intHigh = stack.pop()
                if intLow >= intHigh:
                    continue

                pivot = self.arrUsernames[intHigh]
                intI = intLow - 1
                for intJ in range(intLow, intHigh):
                    if self.arrUsernames[intJ] <= pivot:
                        intI += 1
                        self.arrUsernames[intI], self.arrUsernames[intJ] = self.arrUsernames[intJ], self.arrUsernames[intI]
                        self.arrPasswords[intI], self.arrPasswords[intJ] = self.arrPasswords[intJ], self.arrPasswords[intI]

                self.arrUsernames[intI + 1], self.arrUsernames[intHigh] = self.arrUsernames[intHigh], self.arrUsernames[intI + 1]
                self.arrPasswords[intI + 1], self.arrPasswords[intHigh] = self.arrPasswords[intHigh], self.arrPasswords[intI + 1]
                intPartition = intI + 1

                stack.append((intLow, intPartition - 1))
                stack.append((intPartition + 1, intHigh))

        
        self.strUsernameToFind = self.entryUsername.get().strip()
        strPasswordToFind  = self.entryPassword.get()

        # Existence checks – fields must not be empty or placeholder text
        if self.strUsernameToFind == '' or self.strUsernameToFind == "Username":
            messagebox.showwarning("Missing Field", "Please enter your username.")
            return
        if strPasswordToFind == '' or strPasswordToFind == "Password":
            messagebox.showwarning("Missing Field", "Please enter your password.")
            return

        # Binary Search
        intLow = 0
        intHigh = len(self.arrUsernames) - 1 
        bFound = False 

        while bFound == False and intLow <= intHigh:   # logical NOT; ≤ operator
            intMid = (intLow + intHigh) // 2  # integer division

            if str(self.arrUsernames[intMid]) == self.strUsernameToFind:
                # Username found; now verify password
                if str(self.arrPasswords[intMid]) == strPasswordToFind:
                    bFound = True
                    self.strCurrentUsername = self.strUsernameToFind
                else:
                    # Username match but wrong password – keep searching
                    intLow = intMid + 1   # increment
            elif self.arrUsernames[intMid] > self.strUsernameToFind:
                intHigh = intMid - 1 # decrement
            else:
                intLow = intMid + 1 # increment

        #  Result ─
        if bFound == True:
            messagebox.showinfo("Login Successful", f"Welcome back, {self.strCurrentUsername}!")
            page2.show()
        else:
            messagebox.showwarning("Login Failed", "Incorrect username or password. " "Please try again.")



#  PAGE 2 – MAIN DASHBOARD      mainPage(BasePage)


class mainPage(BasePage):
    """
    Main dashboard - displays the logged-in user's quizzes in a
    scrollable, sortable list.

    Algorithm: Selection Sort (ascending or descending) toggled by
    clicking the Sort button.  Time complexity: O(n²).

    Data structures:
        quizzes       - 2-D array (list of CSV rows; each row is a record)
        quiz_frames   - 1-D array of widget references (for cleanup)

    Record structure for each quiz (field accessed by index):
        [0] title    - text  (str)
        [1] username - text  (str)
        [2] qa_data  - text  (str, string representation of a 2-D list)
    """

    def __init__(self):
        """Initialise sidebar, scrollable list, and header widgets."""
        super().__init__()

        #  Private state ─
        self.intSortClicks = 0   # int – tracks sort direction toggle

        #  Public quiz data (2-D array) 
        self.arrQuizzes = []   # list[list] – each inner list is a quiz record

        #  1-D arrays of dynamic widget references 
        self.arrQuizFrames  = []
        self.arrQuizLabels  = []
        self.arrQuizButtons = []

        #  Sidebar frame 
        self.frmSidebar = ttk.Frame(app, style='Sidebar.TFrame', width=200, height=800)

        self.lblAppName = ttk.Label(master=self.frmSidebar, text="Squiz", font=tplFontSubTitle, style='SidebarTitle.TLabel')
        self.lblAppTag = ttk.Label(master=self.frmSidebar, text="my quizzes", font=tplSmallFont, style='Sidebar.TLabel')

        self.btnSort = ttk.Button(master=self.frmSidebar, text="⇅  Sort A-Z", command=self.sort, style='Sidebar.TButton')
        self.btnAdd = ttk.Button(master=self.frmSidebar, text="+  New Quiz", command=self.add, style='Sidebar.TButton')
        self.btnManage = ttk.Button(master=self.frmSidebar, text="⚙  Account", command=self.managePage, style='Sidebar.TButton')
        self.btnLogout = ttk.Button(master=self.frmSidebar, text="← Log Out", command=showPage1, style='Sidebar.TButton')
        
        

        #  Content area header ─
        self.lblPageTitle = ttk.Label(master=app, text="My Quizzes", font=tplFontTitle, style='TLabel')

        #  Scrollable canvas for quiz cards ─
        self.canvasScroll = Canvas(app, bg=dictColours["bg"], highlightthickness=0, borderwidth=0, relief="flat")
        self.scrollbarScroll = ttk.Scrollbar(master=self.canvasScroll, orient="vertical", command=self.canvasScroll.yview, style='TScrollbar')
        self.canvasScroll.configure(yscrollcommand=self.scrollbarScroll.set)
        self.frameScrollable = Frame(self.canvasScroll, bg=dictColours["bg"])
        self.frameScrollable.bind("<Configure>", lambda e: self.canvasScroll.configure(scrollregion=self.canvasScroll.bbox("all")))
        self.intCanvasWindow = self.canvasScroll.create_window((20, 10), window=self.frameScrollable, anchor="nw")
        
        self.noquiz = ttk.Label(master=self.frameScrollable, text="No quizzes yet — press + New Quiz to get started", font=tplSmallFont, style='Muted.TLabel')

        # Bind mouse-wheel scrolling for Windows and macOS
        self.canvasScroll.bind("<MouseWheel>", lambda e: self.canvasScroll.yview_scroll(-1 * (e.delta // 120), "units"))

    #  Private helpers ─

    def buildQuizCard(self, intIndex: int):
        """
        Private - create one quiz-card widget and append it to the
        scroll area.

        Parameters
        ----------
        intIndex : int - position of the quiz in self.quizzes (2-D array)
        """
        # Access record field [0] (title – text type)
        strQuizTitle = self.arrQuizzes[intIndex][0]

        frmQuiz = ttk.Frame(self.frameScrollable, style='TFrame', width=740, height=65)
        frmQuiz.pack(pady=6, padx=15)
        frmQuiz.pack_propagate(False)   # maintain fixed height

        lblQuiz = ttk.Label(master=frmQuiz, text=strQuizTitle, font=tplSmallBold, style='Card.TLabel')
        btnPlay = ttk.Button(master=frmQuiz, text="Play →", command=lambda i=intIndex: self.playQuiz(i), style='Secondary.TButton')

        lblQuiz.place(relx=0.04, rely=0.5, anchor="w")
        btnPlay.place(relx=0.96, rely=0.5, anchor="e")

        # Append to 1-D tracking arrays for cleanup later
        self.arrQuizLabels.append(lblQuiz)
        self.arrQuizButtons.append(btnPlay)
        self.arrQuizFrames.append(frmQuiz)

    #  Public methods 

    def getQuizzes(self) -> list:
        """
        Read quizzesArray.csv (CSV, delimited) into a 2-D array and
        filter rows that belong to the logged-in user.

        Returns
        -------
        list[list] - 2-D array of quiz records (or empty list)

        Each row is a record with fields at fixed indices:
            [0] title    : str
            [1] username : str
            [2] qa_data   (string repr of a 2-D list)
        """
        strUsername = getattr(page1, 'strUsernameToFind', '').strip()
        if strUsername == '':   # existence check – must have a logged-in user
            return []

        arrAllData = []   # 1-D array of raw rows; each row is itself a list

        with open(strQuizzesPath) as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                arrAllData.append(row)   # build 2-D array

        # Filter rows whose username field matches the current user
        arrUserQuizzes = [row for row in arrAllData if row[1].strip() == strUsername]
        return arrUserQuizzes

    def playQuiz(self, intQuizIndex: int):
        """
        Load the chosen quiz and navigate to the play-mode page.

        Parameters
        ----------
        intQuizIndex : int - index of the selected quiz in self.quizzes
        """
        page6.getQuizToPlay(intQuizIndex)
        showPage6()

    def sort(self):
        """
        Toggle between ascending (A→Z) and descending (Z→A) order
        using the Selection Sort algorithm.

        Selection Sort:
            For each position i, scan the remainder to find the
            minimum (or maximum) and swap it into position i.
            Time complexity: O(n²)
        """
        self.intSortClicks += 1   # increment click counter
        intN = len(self.arrQuizzes)

        if self.intSortClicks % 2 == 0:   # modulus – even -> descending
            self.btnSort.config(text="⇅  Sort A-Z")
            #  Descending Selection Sort (Z -> A) ─
            for i in range(intN - 1):
                intMaxIdx: int = i
                for j in range(i + 1, intN):
                    if self.arrQuizzes[j][0].lower() > self.arrQuizzes[intMaxIdx][0].lower():   # > operator
                        intMaxIdx = j
                if intMaxIdx != i:
                    # Swap quiz records in the 2-D array
                    self.arrQuizzes[i], self.arrQuizzes[intMaxIdx] = self.arrQuizzes[intMaxIdx], self.arrQuizzes[i]
        else:
            self.btnSort.config(text="⇅  Sort Z-A")
            #  Ascending Selection Sort (A -> Z) 
            for i in range(intN - 1):
                intMinIdx: int = i
                for j in range(i + 1, intN):
                    if self.arrQuizzes[j][0].lower() < self.arrQuizzes[intMinIdx][0].lower():   # < operator
                        intMinIdx = j
                if intMinIdx != i:
                    self.arrQuizzes[i], self.arrQuizzes[intMinIdx] = self.arrQuizzes[intMinIdx], self.arrQuizzes[i]

        self.show(reload_quizzes=False)   # re-render with sorted order

    def add(self):
        """Navigate to the Create Quiz page."""
        showPage5()

    def managePage(self):
        """Navigate to the Manage Account page."""
        page4.show()

    def show(self, reload_quizzes = True):
        """
        Display the main dashboard.

        Parameters
        ----------
        reload_quizzes : bool - True  -> re-read quizzes from CSV
                                False -> use current self.quizzes (after sort)
        """
        hideAll()
        self.hide()   # destroy previously rendered quiz cards

        if reload_quizzes:
            self.arrQuizzes = self.getQuizzes()
        if self.arrQuizzes is None:
            self.arrQuizzes = []

        #  Place sidebar ─
        self.frmSidebar.place(x=0, y=0, width=200, height=800)
        self.lblAppName.place(relx=0.5, rely=0.06, anchor="center")
        self.lblAppTag.place(relx=0.5, rely=0.12, anchor="center")
        self.btnSort.place(relx=0.5, rely=0.30, anchor="center", width=170)
        self.btnAdd.place(relx=0.5, rely=0.40, anchor="center", width=170)
        self.btnManage.place(relx=0.5, rely=0.50, anchor="center", width=170)
        self.btnLogout.place(relx=0.5, rely=0.94, anchor="center", width=170)

        #  Place content area ─
        self.lblPageTitle.place(relx=0.62, rely=0.09, anchor="center")
        self.canvasScroll.place(relx=0.62, rely=0.57, anchor="center", width=820, height=550)
        self.scrollbarScroll.pack(side=RIGHT, fill=Y)

        # Render a quiz card for each quiz record (iteration over 2-D array)
        for i in range(len(self.arrQuizzes)):
            self.buildQuizCard(i)

        # Show empty-state hint when the user has no quizzes yet
        if len(self.arrQuizzes) == 0:
            self.noquiz.pack(pady=40)

    def hide(self):
        """Destroy quiz cards and hide all static widgets."""
        # Destroy dynamically created quiz cards (iteration over 1-D array)
        for frame in self.arrQuizFrames:
            frame.destroy()
        self.arrQuizLabels.clear()
        self.arrQuizButtons.clear()
        self.arrQuizFrames.clear()

        # Hide static widgets
        self.frmSidebar.place_forget()
        self.lblPageTitle.place_forget()
        self.scrollbarScroll.pack_forget()
        
        self.noquiz.pack_forget()

        # Lower the canvas below the login frame to prevent it covering page 1
        try:
            self.canvasScroll.lower(page1.frLogin)
        except Exception:
            try:
                self.canvasScroll.lower()
            except Exception:
                pass



#  PAGE 3 – SIGN-UP PAGE      newAccPage(FormPage)


class newAccPage(FormPage):
    """
    Registration page for new users.

    Validation applied (all three required techniques):
        1. Existence check   - username and password must not be empty
        2. Type check        - username must be alphanumeric/underscore only
        3. Range check       - password must be ≥ MIN_PASSWORD_LENGTH chars
        4. Uniqueness check  - Linear Search to confirm username is free
    """

    def __init__(self):
        """Initialise all sign-up page widgets."""
        super().__init__()
        
        self.intMinPasswordLength = 8
        
        

        #  Private 1-D arrays 
        self.arrUsernames = []   # list[str]
        self.arrPasswords = []   # list[str]

        #  Widgets 
        self.lblTitle = ttk.Label(master=app, text="Create Account", font=tplFontTitle, style='TLabel')
        self.lblSubtitle = ttk.Label(master=app, text="Join Squiz today — it's free.", font=tplSmallFont, style='Muted.TLabel')

        self.frmSignUp = ttk.Frame(master=app, style='TFrame', width=480, height=380)
        self.lblFormTitle = ttk.Label( master=self.frmSignUp, text="Sign Up", font=tplFontSubTitle, style='Card.TLabel')

        self.entryNewUsername = ttk.Entry(master=self.frmSignUp, width=22, font=tplFontPara, style='TEntry')
        self.entryNewUsername.insert(0, "Username")

        self.entryNewPassword = ttk.Entry(master=self.frmSignUp, width=22, font=tplFontPara, style='TEntry')
        self.entryNewPassword.insert(0, "Password")

        self.btnSubmit = ttk.Button(master=self.frmSignUp, text="Create Account", command=self.createNewAcc)
        self.btnBackToLogin = ttk.Button(master=app, text="← Back to Login", command=self.goToLogin, style='Secondary.TButton')

        # Bind placeholder focus events (inherited from FormPage)
        self.entryNewUsername.bind('<FocusIn>', lambda e: self.onEntryClick(e, self.entryNewUsername, "Username"))
        self.entryNewUsername.bind('<FocusOut>', lambda e: self.onFocusOut(e, self.entryNewUsername, "Username"))
        self.entryNewPassword.bind('<FocusIn>', lambda e: self.onEntryClick(e, self.entryNewPassword, "Password"))
        self.entryNewPassword.bind('<FocusOut>', lambda e: self.onFocusOut(e, self.entryNewPassword, "Password"))

    #  Public methods 

    def goToLogin(self):
        """Return to the Login page."""
        showPage1()

    def createNewAcc(self):
        """
        Validate input and write a new account record to accounts.csv.

        Validation sequence:
            1. Existence check  - fields must not be empty or placeholder
            2. Type check       - username must be alphanumeric/underscore
            3. Uniqueness check - Linear Search through existing usernames
            4. Range check      - password length ≥ MIN_PASSWORD_LENGTH
            
        INPUT
            - arrUsernames of current accounts and passwords
            - new username and new password
        
        PROCESS
            - validate the new username and new password
            - use linear search to check whether username already exists
            
        OUTPUT
            - show messagebox when account has been created
        """
        #  Load existing accounts into 1-D arrays ─
        self.arrUsernames = []
        self.arrPasswords = []
        with open(strAccountsPath, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.arrUsernames.append(row[0])
                self.arrPasswords.append(row[1])

        strNewUsername = self.entryNewUsername.get().strip()
        strNewPassword = self.entryNewPassword.get()

        #  1. Existence check – username 
        if strNewUsername == '' or strNewUsername == "Username":
            messagebox.showwarning("Missing Username",
                                   "Please enter a username.")
            return

        #  2. Type check – alphanumeric characters and underscores only
        bValidChars = all(ch.isalnum() or ch == '_' for ch in strNewUsername)
        if not bValidChars:   # logical NOT
            messagebox.showwarning("Invalid Username", "Username may only contain letters, " "numbers and underscores ( _ ).")
            return

        #  3. Uniqueness check – Linear Search through 1-D array 
        for i in range(len(self.arrUsernames)):   # iteration
            if strNewUsername == self.arrUsernames[i]:   # equality
                messagebox.showwarning("Username Taken", "That username is already in use. " "Please choose a different one.")
                return

        #  1. Existence check – password ─
        if not strNewPassword or strNewPassword == "Password":
            messagebox.showwarning("Missing Password", "Please enter a password.")
            return

        #  4. Range check – password must be long enough ─
        if len(strNewPassword) < self.intMinPasswordLength:   # < comparison
            messagebox.showwarning("Weak Password", f"Password must be at least " f"{self.intMinPasswordLength} characters long.")
            return

        #  Write new account record to CSV (write to data source) ─
        with open(strAccountsPath, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([strNewUsername, strNewPassword])

        messagebox.showinfo("Account Created", "Your account has been created. Please log in.")
        showPage1()

    def show(self):
        """Display the sign-up page."""
        hideAll()
        self.lblTitle.place(relx=0.5, rely=0.10, anchor="center")
        self.lblSubtitle.place(relx=0.5, rely=0.19, anchor="center")
        self.frmSignUp.place(relx=0.5, rely=0.54, anchor="center")
        self.lblFormTitle.place(relx=0.5, rely=0.14, anchor="center")
        self.entryNewUsername.place(relx=0.5, rely=0.35, anchor="center")
        self.entryNewPassword.place(relx=0.5, rely=0.55, anchor="center")
        self.btnSubmit.place(relx=0.5, rely=0.76, anchor="center")
        self.btnBackToLogin.place(relx=0.5, rely=0.93, anchor="center")

    def hide(self):
        """Remove all sign-up widgets from the screen."""
        for w in (self.lblTitle, self.lblSubtitle, self.frmSignUp,
                  self.lblFormTitle, self.entryNewUsername,
                  self.entryNewPassword, self.btnSubmit,
                  self.btnBackToLogin):
            w.place_forget()



#  PAGE 4 – MANAGE ACCOUNT PAGE      manageAccPage(BasePage)


class manageAccPage(BasePage):
    """
    Account management page.

    Allows the logged-in user to permanently delete their account and
    all associated quizzes from both CSV files.
    """

    def __init__(self):
        """Initialise widgets for the manage account page."""
        super().__init__()

        self.lblTitle = ttk.Label(master=app, text="My Account", font=tplFontTitle, style='TLabel')
        self.lblSubtitle = ttk.Label(master=app, text="Manage your Squiz account settings.", font=tplSmallFont, style='Muted.TLabel')

        self.frmManage = ttk.Frame(master=app, style='TFrame', width=520, height=320)
        self.lblWarningHeader = ttk.Label(master=self.frmManage, text="Danger Zone", font=tplSmallBold, style='Warning.TLabel')
        self.lblWarning = ttk.Label(master=self.frmManage, text="Deleting your account is permanent\n""and removes all your quizzes.", font=tplSmallFont, style='MutedCard.TLabel')
        self.btnDeleteAcc = ttk.Button(master=self.frmManage, text="Delete My Account", command=self.deleteAcc, style='Danger.TButton')
        self.btnDone = ttk.Button(master=self.frmManage, text="← Back to Quizzes", command=self.done)

    def done(self):
        """Return to the main quiz dashboard."""
        page2.show()

    def deleteAcc(self):
        """
        Confirm deletion, then remove the user's record from both CSVs.

        Writes the filtered lines back to each file (write to data source).
        INPUT
            - boolean confirmation to delete account
        
        PROCESS 
            - check whether user's confirmation is true
            - search csv for username and delete corresponding rows of quizzes and account
        
        OUTPUT
            - Display message box showing that the account has been deleted
        """
        bConfirmed = messagebox.askyesno("Delete Account", "Are you sure you want to permanently delete your account?\n" "All your quizzes will be lost.")

        if not bConfirmed:   # logical NOT – user chose 'No'
            return

        #strUsername = getattr(page1, 'strUsernameToFind', '').strip()
        strUsername = page1.strUsernameToFind.strip()
        if not strUsername:   # existence check
            messagebox.showerror("Error", "Could not identify the logged-in account.")
            return

        #  Remove user from accounts.csv 
        with open(strAccountsPath, mode='r') as file:
            arrLines = file.readlines()   # 1-D array of file lines
        arrUpdated = [ln for ln in arrLines if not ln.startswith(strUsername + ',')]
        with open(strAccountsPath, mode='w') as file:
            file.writelines(arrUpdated)

        #  Remove user's quizzes from quizzesArray.csv 
        with open(strQuizzesPath, mode='r') as file:
            arrLines = file.readlines()
        arrUpdated = [ln for ln in arrLines if not (';' + strUsername + ';') in ln]
        with open(strQuizzesPath, mode='w') as file:
            file.writelines(arrUpdated)

        messagebox.showinfo("Account Deleted", "Your account has been successfully deleted.")
        showPage1()

    def show(self):
        """Display the manage account page."""
        hideAll()
        self.lblTitle.place(relx=0.5, rely=0.12, anchor="center")
        self.lblSubtitle.place(relx=0.5, rely=0.21, anchor="center")
        self.frmManage.place(relx=0.5, rely=0.55, anchor="center")
        self.lblWarningHeader.place(relx=0.5, rely=0.18, anchor="center")
        self.lblWarning.place(relx=0.5, rely=0.34, anchor="center")
        self.btnDeleteAcc.place(relx=0.5, rely=0.58, anchor="center")
        self.btnDone.place(relx=0.5, rely=0.80, anchor="center")

    def hide(self):
        """Remove all manage account widgets from the screen."""
        for w in (self.lblTitle, self.lblSubtitle, self.frmManage, self.lblWarningHeader, self.lblWarning, self.btnDeleteAcc, self.btnDone):
            w.place_forget()



#  PAGE 5 – CREATE QUIZ PAGE -- newQuizPage(FormPage)


class newQuizPage(FormPage):
    """
    Page for building a new quiz question by question.

    Data structures:
        arrQuizQuestions - 1-D array (list[str]) of entered questions
        arrQuizAnswers   - 1-D array (list[str]) of matching answers
        Together they form a 2-D structure when zipped for CSV storage.

    Validation:
        • Existence check - question, answer, title must not be empty
        • Range check     - question ≤ MAX_QUESTION_LENGTH characters
                            answer   ≤ MAX_ANSWER_LENGTH characters
                            at least MIN_QUESTIONS pairs before saving
    """

    def __init__(self):
        """Initialise all create-quiz page widgets."""
        super().__init__()
        
        self.intMinQuestions = 5
        
        self.intMaxQuestioLength = 37
        
        self.intMaxAnswerLength = 13

        #  Private 1-D arrays 
        self.arrQuizQuestions = []   # list[str]
        self.arrQuizAnswers   = []   # list[str]

        #  Widgets 
        self.lblTitle = ttk.Label(master=app, text="Create Quiz", font=tplFontTitle, style='TLabel')

        self.lblCount = ttk.Label(master=app, text=f"Questions added: 0  (minimum {self.intMinQuestions})", font=tplSmallFont, style='Muted.TLabel')

        self.frmCard = ttk.Frame(master=app, style='TFrame', width=580, height=440)

        self.entryQuizTitle = ttk.Entry(master=self.frmCard, width=26, font=tplFontPara, style='TEntry')
        self.entryQuizTitle.insert(0, "Quiz Title")

        self.lblDivider = ttk.Label(master=self.frmCard, text=" Add Questions ", font=tplSmallFont, style='MutedCard.TLabel')

        self.entryQuestion = ttk.Entry(master=self.frmCard, width=26, font=tplFontPara, style='TEntry')
        self.entryQuestion.insert(0, "Question")

        self.entryAnswer = ttk.Entry(master=self.frmCard, width=26, font=tplFontPara, style='TEntry')
        self.entryAnswer.insert(0, "Answer")

        self.btnNext = ttk.Button(master=self.frmCard, text="Add Question ＋", command=self.nextQuestion)
        self.btnFinish = ttk.Button(master=self.frmCard, text="Save Quiz ✓", command=self.finishQuiz)
        self.btnExit = ttk.Button(master=app, text="Discard", command=self.exit, style='Secondary.TButton')

        # Bind placeholder events (inherited from FormPage)
        for entry, placeholder in [(self.entryQuizTitle, "Quiz Title"), (self.entryQuestion,  "Question"),(self.entryAnswer,    "Answer"),]:
            entry.bind('<FocusIn>', lambda e, w=entry, p=placeholder: self.onEntryClick(e, w, p))
            entry.bind('<FocusOut>',lambda e, w=entry, p=placeholder: self.onFocusOut(e, w, p))

    #  Public methods 

    def exit(self):
        """Confirm discard and return to the main dashboard."""
        bConfirmed: bool = messagebox.askyesno("Discard Quiz", "Exit without saving? All questions will be lost.")
        if bConfirmed:   # selection
            self.arrQuizQuestions.clear()
            self.arrQuizAnswers.clear()
            self.lblCount.config(text=f"Questions added: 0  (minimum {self.intMinQuestions})")
            showPage2()

    def nextQuestion(self):
        """
        Validate the current Q&A pair and append to the 1-D arrays.

        Validation:
            • Existence check - both fields must not be empty
            • Range check     - lengths must not exceed defined limits
            
        INPUT
            - question from user
            - answer from user
        
        PROCESS
            - existence check question and answer input
            - range check answer and question
        
        OUTPUT
            - append answers and questions to array
        """
        strQuestion = self.entryQuestion.get().strip()
        strAnswer = self.entryAnswer.get().strip()

        # Existence checks
        if not strQuestion or strQuestion == "Question":
            messagebox.showwarning("Missing Question", "Please type a question before adding.")
            return
        if not strAnswer or strAnswer == "Answer":
            messagebox.showwarning("Missing Answer", "Please type an answer before adding.")
            return

        # Range checks
        if len(strQuestion) > self.intMaxQuestioLength:   # > operator
            messagebox.showwarning("Question Too Long", f"Questions must be ≤ " f"{self.intMaxQuestioLength} characters.")
            return
        if len(strAnswer) > self.intMaxAnswerLength:
            messagebox.showwarning("Answer Too Long", f"Answers must be ≤ " f"{self.intMaxAnswerLength} characters.")
            return

        # Append to 1-D arrays
        self.arrQuizQuestions.append(strQuestion)
        self.arrQuizAnswers.append(strAnswer)

        # Update counter display
        intCount = len(self.arrQuizQuestions)   # int – current count
        self.lblCount.config(text=f"Questions added: {intCount}  (minimum {self.intMinQuestions})")

        # Reset entry fields to their placeholders
        self.setPlaceholder(self.entryQuestion, "Question")
        self.setPlaceholder(self.entryAnswer,   "Answer")

    def finishQuiz(self):
        """
        Validate the completed quiz and write it to quizzesArray.csv.

        Builds a 2-D list of [question, answer] pairs and stores it as a
        single CSV field, along with the title and owner username.

        Validation:
            • Existence check - title must not be empty
            • Range check     - at least MIN_QUESTIONS questions required
        """
        strQuizTitle = self.entryQuizTitle.get().strip()

        # Existence check – title
        if not strQuizTitle or strQuizTitle == "Quiz Title":
            messagebox.showwarning("Missing Title", "Please enter a title for your quiz.")
            return

        # Range check – minimum question count
        if len(self.arrQuizQuestions) < self.intMinQuestions:   # < operator
            messagebox.showwarning("Not Enough Questions", f"A quiz needs at least {self.intMinQuestions} " f"questions. Please add more.")
            return

        # Build 2-D array of question/answer pairs
        arrQuizData = [[q, a] for q, a in zip(self.arrQuizQuestions, self.arrQuizAnswers)]

        # Write quiz record to CSV (write to data source)
        with open(strQuizzesPath, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([strQuizTitle, page1.strCurrentUsername, arrQuizData])

        # Reset state
        self.arrQuizQuestions.clear()
        self.arrQuizAnswers.clear()
        self.setPlaceholder(self.entryQuizTitle, "Quiz Title")
        self.lblCount.config(text=f"Questions added: 0  (minimum {self.intMinQuestions})")

        messagebox.showinfo("Quiz Saved", f'"{strQuizTitle}" has been saved!')
        showPage2()

    def show(self):
        """Display the create-quiz page."""
        hideAll()
        self.lblTitle.place(relx=0.5, rely=0.08, anchor="center")
        self.lblCount.place(relx=0.5, rely=0.16, anchor="center")
        self.frmCard.place(relx=0.5, rely=0.56, anchor="center")
        self.entryQuizTitle.place(relx=0.5, rely=0.11, anchor="center")
        self.lblDivider.place(relx=0.5, rely=0.26, anchor="center")
        self.entryQuestion.place(relx=0.5, rely=0.41, anchor="center")
        self.entryAnswer.place(relx=0.5, rely=0.56, anchor="center")
        self.btnNext.place(relx=0.5, rely=0.71, anchor="center")
        self.btnFinish.place(relx=0.5, rely=0.87, anchor="center")
        self.btnExit.place(relx=0.92, rely=0.96, anchor="center")

    def hide(self):
        """Remove all create-quiz widgets from the screen."""
        for w in (self.lblTitle, self.lblCount, self.frmCard,
                  self.entryQuizTitle, self.lblDivider,
                  self.entryQuestion, self.entryAnswer,
                  self.btnNext, self.btnFinish, self.btnExit):
            w.place_forget()



#  PAGE 6 – PLAY MODE SELECTION      playQuizPage(BasePage)


class playQuizPage(BasePage):
    """
    Displayed after the user selects a quiz to play.
    Lets the user choose between Flashcard and Quiz (Kahoot) mode.

    Data:
        arrQuizToPlay - 2-D list of [question, answer] pairs
        strQuizTitle  - text (str) of the selected quiz
    """

    def __init__(self):
        """Initialise mode-selection widgets."""
        super().__init__()

        #  Public quiz data (consumed by page7 and page8) 
        self.arrQuizToPlay = []   # list[list] – 2-D array [[q, a], ...]
        self.strQuizTitle  = ""   # str – quiz title

        #  Widgets 
        self.lblQuizName = ttk.Label(master=app, text="", font=tplFontTitle, style='TLabel')
        self.lblSubtitle = ttk.Label(master=app, text="Choose how you'd like to study", font=tplSmallFont, style='Muted.TLabel')

        self.frmPlay = ttk.Frame(master=app, style='TFrame', width=520, height=320)

        self.btnFlashCard = ttk.Button(master=self.frmPlay, text="🃏   Flashcards", command=self.flashCard)
        self.lblFlashDesc = ttk.Label(master=self.frmPlay, text="Flip through cards at your own pace", font=tplSmallFont, style='MutedCard.TLabel')

        self.btnKahoot = ttk.Button(master=self.frmPlay, text="⚡   Quiz Mode", command=self.kahoot)
        self.lblKahootDesc = ttk.Label(master=self.frmPlay, text="Multiple-choice questions", font=tplSmallFont, style='MutedCard.TLabel')

        self.btnCancel = ttk.Button(master=self.frmPlay, text="← Back", command=self.cancel)

    def getQuizToPlay(self, intQuizIndex):
        """
        Load the quiz at the given index from the main page's 2-D array.

        Record fields accessed by index:
            [0] title   : str
            [1] username: str
            [2] data     (string repr of 2-D [[q, a], ...] list)

        Parameters
        ----------
        intQuizIndex : int – index in page2.quizzes
        """
        self.strQuizTitle = page2.arrQuizzes[intQuizIndex][0]   # text
        strRawData = page2.arrQuizzes[intQuizIndex][2]   # text
        # Convert the stored string back to a Python 2-D list
        self.arrQuizToPlay = eval(strRawData)

    def cancel(self):
        """Return to the main quiz dashboard."""
        showPage2()

    def flashCard(self):
        """Navigate to Flashcard mode."""
        showPage7()

    def kahoot(self):
        """Navigate to Quiz (Kahoot) mode."""
        showPage8()

    def show(self):
        """Display the mode selection page."""
        hideAll()
        self.lblQuizName.config(text=self.strQuizTitle)
        self.lblQuizName.place(relx=0.5, rely=0.13, anchor="center")
        self.lblSubtitle.place(relx=0.5, rely=0.22, anchor="center")
        self.frmPlay.place(relx=0.5, rely=0.56, anchor="center")
        self.btnFlashCard.place(relx=0.5, rely=0.22, anchor="center", width=360)
        self.lblFlashDesc.place(relx=0.5, rely=0.38, anchor="center")
        self.btnKahoot.place(relx=0.5, rely=0.55, anchor="center", width=360)
        self.lblKahootDesc.place(relx=0.5, rely=0.71, anchor="center")
        self.btnCancel.place(relx=0.5, rely=0.88, anchor="center")

    def hide(self):
        """Remove all mode-selection widgets from the screen."""
        for w in (self.lblQuizName, self.lblSubtitle, self.frmPlay,
                  self.btnFlashCard, self.lblFlashDesc,
                  self.btnKahoot, self.lblKahootDesc, self.btnCancel):
            w.place_forget()



#  PAGE 7 – FLASHCARD MODE      flashCardPage(BasePage)


class flashCardPage(BasePage):
    """
    Flashcard study mode.

    Displays one card at a time; the user flips it to reveal the answer
    and advances at their own pace.  Cards wrap around when the end is
    reached.

    Data: page6.arrQuizToPlay - 2-D list of [question, answer] pairs.
    """

    def __init__(self):
        """Initialise flashcard widgets."""
        super().__init__()

        #  Private state ─
        self.intClicks = 0   # flip-click counter (even = Q, odd = A)
        self.intN = 0   # current card index

        #  Widgets 
        self.lblQuizTitle = ttk.Label(master=app, text="", font=tplFontSubTitle, style='TLabel')
        self.lblProgress = ttk.Label(master=app, text="", font=tplSmallFont, style='Muted.TLabel')

        self.crdFlashCard = ttk.Frame(master=app, style='TFrame', width=720, height=340)
        self.lblSide = ttk.Label(master=self.crdFlashCard, text="QUESTION", font=tplSmallBold, style='MutedCard.TLabel')
        self.lblContent = ttk.Label(master=self.crdFlashCard, text="", font=tplFontPara, style='Card.TLabel', wraplength=660)

        self.btnFlip = ttk.Button(master=app, text="Flip Card ↺", command=self.flipCard)
        self.btnNext = ttk.Button(master=app, text="Next →", command=self.nextCard)
        self.btnFinish = ttk.Button(master=app, text="Finish", command=self.finishQuiz, style='Secondary.TButton')

    #  Private helpers ─

    def refreshCard(self):
        """
        Private - update the progress label and show the question side
        of the current card.
        """
        intTotal: int = len(page6.arrQuizToPlay)   # int – total cards
        # Progress: addition operator used (self.__intN + 1)
        self.lblProgress.config(text=f"Card {self.intN + 1} of {intTotal}")
        self.lblSide.config(text="QUESTION")
        self.lblContent.config(text=page6.arrQuizToPlay[self.intN][0])   # field [0] = question

    #  Public methods 

    def flipCard(self):
        """Toggle the card between question (front) and answer (back)."""
        self.intClicks += 1   # increment

        if self.intClicks % 2 == 0:   # modulus – even -> question side
            self.lblSide.config(text="QUESTION")
            self.lblContent.config(text=page6.arrQuizToPlay[self.intN][0])
        else:                           # odd -> answer side
            self.lblSide.config(text="ANSWER")
            self.lblContent.config(text=page6.arrQuizToPlay[self.intN][1])   # field [1]

    def nextCard(self):
        """Advance to the next card; wrap back to the first when at the end."""
        intTotal: int = len(page6.arrQuizToPlay)
        self.intN      = (self.intN + 1) % intTotal 
        self.intClicks = 0
        self.refreshCard()

    def finishQuiz(self):
        """End the flashcard session and return to the main page."""
        self.intN      = 0
        self.intClicks = 0
        showPage2()

    def show(self):
        """Reset state and display the flashcard page."""
        hideAll()
        self.intN      = 0
        self.intClicks = 0
        self.lblQuizTitle.config(text=page6.strQuizTitle)
        self.refreshCard()

        self.lblQuizTitle.place(relx=0.5, rely=0.08, anchor="center")
        self.lblProgress.place(relx=0.5, rely=0.17, anchor="center")
        self.crdFlashCard.place(relx=0.5, rely=0.48, anchor="center")
        self.lblSide.place(relx=0.5, rely=0.16, anchor="center")
        self.lblContent.place(relx=0.5, rely=0.52, anchor="center")
        self.btnFlip.place(relx=0.33, rely=0.83, anchor="center")
        self.btnNext.place(relx=0.67, rely=0.83, anchor="center")
        self.btnFinish.place(relx=0.5, rely=0.95, anchor="center")

    def hide(self):
        """Remove all flashcard widgets from the screen."""
        for w in (self.lblQuizTitle, self.lblProgress,
                  self.crdFlashCard, self.lblSide, self.lblContent,
                  self.btnFlip, self.btnNext, self.btnFinish):
            w.place_forget()



#  PAGE 8 – KAHOOT / QUIZ MODE      kahootPage(FormPage)


class kahootPage(FormPage):
    """
    Multiple-choice quiz mode.

    For each question, four answer options are shown (one correct,
    three randomly sampled from other quiz answers).  Score is
    accumulated and a results screen is shown at the end.

    Data structures:
        allAnswers   - 2-D list for each question, 4 shuffled options
        allQuestions - 1-D list of question strings
        ansPositions - 1-D list of ints: correct-answer index per question

    Validation (time-per-question entry):
        • Type check  - input must be a whole number (isdigit)
        • Range check - must be between MIN_TIME_PER_Q and MAX_TIME_PER_Q
    """

    def __init__(self):
        """Initialise all Kahoot mode widgets."""
        super().__init__()

        #  Private quiz-state variables ─
        self.intN = 0 # current question index
        self.intCorrect = 0 # correct-answer count
        self.intIncorrect: int = 0 # incorrect-answer count
        self.allAnswers = [] # 2-D array of 4 options
        self.allQuestions = [] # 1-D array of questions
        self.ansPositions = [] # 1-D correct-index array

        #  Settings screen ─
        self.lblKahoot = ttk.Label(master=app, text="Quiz Mode", font=tplFontTitle, style='TLabel')
        self.lblSubtitle = ttk.Label(master=app, text="Multiple-choice", font=tplSmallFont, style='Muted.TLabel')

        self.frmSettings = ttk.Frame(master=app, style='TFrame', width=560, height=340)
    

        self.btnStart = ttk.Button(master=self.frmSettings, text="Start Quiz ▶", command=self.getAnswers)

        #  Live question display 
        self.lblQuestion = ttk.Label(master=app, text="", font=tplFontSubTitle, style='TLabel', wraplength=900)
        
        self.btnCancel = ttk.Button(master=app, text="Cancel", command=self.cancel, style='Secondary.TButton')

        # Answer tiles: each is a coloured button with an overlaid label
        # (label carries the answer text; button colour provides visual hit area)
        self.btnAns1 = ttk.Button(master=app, text=" ", command=self.ans1Selected, style='Tile.TButton')
        self.lblAns1 = ttk.Label(master=app, text="", font=tplFontAnswer, style='TileText.TLabel', wraplength=420)

        self.btnAns2 = ttk.Button(master=app, text=" ", command=self.ans2Selected, style='Tile.TButton')
        self.lblAns2 = ttk.Label(master=app, text="", font=tplFontAnswer, style='TileText.TLabel', wraplength=420)

        self.btnAns3 = ttk.Button(master=app, text=" ", command=self.ans3Selected, style='Tile.TButton')
        self.lblAns3 = ttk.Label(master=app, text="", font=tplFontAnswer, style='TileText.TLabel', wraplength=420)

        self.btnAns4 = ttk.Button(master=app, text=" ", command=self.ans4Selected, style='Tile.TButton')
        self.lblAns4 = ttk.Label(master=app, text="", font=tplFontAnswer, style='TileText.TLabel', wraplength=420)

        #  Results screen 
        self.lblResults = ttk.Label(master=app, text="Results", font=tplFontTitle, style='TLabel')

        self.frmResults = ttk.Frame(master=app, style='TFrame', width=700, height=440)
        self.lblCorrectHdr = ttk.Label(master=self.frmResults, text="Correct", font=tplSmallBold, style='Card.TLabel')
        self.lblCorrect = ttk.Label(master=self.frmResults, text="", font=tplFontHuge, style='Success.TLabel')
        self.lblIncorrectHdr = ttk.Label(master=self.frmResults, text="Incorrect", font=tplSmallBold, style='Card.TLabel')
        self.lblIncorrect = ttk.Label(master=self.frmResults, text="",font=tplFontHuge, style='Warning.TLabel')
        self.lblScoreHdr = ttk.Label(master=self.frmResults, text="Score", font=tplSmallBold, style='Card.TLabel')
        self.lblPercentage = ttk.Label(master=self.frmResults, text="", font=tplFontSubTitle, style='Card.TLabel')
        self.btnDone = ttk.Button(master=self.frmResults, text="Back to Quizzes", command=self.finishKahoot)
        
    def cancel(self):
        self.intN      = 0

        showPage2()

    #  Private helpers ─

    def processAnswer(self, strSelected: str):
        """
        Private - evaluate whether the selected answer is correct and
        advance to the next question.

        Parameters
        ----------
        strSelected  - the answer text from the clicked label, string as it is the text from the selected answer
        
        INPUT
            - strCorrect
            - strSelected
            
        PROCESS
            - check whether selected answer is the same as the corect answer
            
        OUTPUT
            - increase the corresponding counter (intCorrect or intIncorrect)
        """
        # Retrieve the correct answer using the pre-stored position index
        strCorrect = self.allAnswers[self.intN][self.ansPositions[self.intN]]

        if strSelected == strCorrect:   # equality comparison
            self.intCorrect   += 1   # increment
        else:
            self.intIncorrect += 1   # increment

        self.intN += 1               # advance to next question
        self.showQuestion()

    def showQuestion(self):
        """
        Private - render the current question and four answer tiles, or
        show the results screen when all questions are exhausted.
        """
        if self.intN >= len(self.allQuestions):   # ≥ comparison
            self.showResults()
            return

        # Update question text
        self.lblQuestion.config(text=self.allQuestions[self.intN])

        # Retrieve 4 shuffled options for this question (2-D array access)
        arrOptions = self.allAnswers[self.intN]
        self.lblAns1.config(text=arrOptions[0])
        self.lblAns2.config(text=arrOptions[1])
        self.lblAns3.config(text=arrOptions[2])
        self.lblAns4.config(text=arrOptions[3])

        # Place question label at top centre
        self.lblQuestion.place(relx=0.5, rely=0.12, anchor="center")

        # Place four answer tiles in a 2×2 grid
        # Top-left
        self.btnAns1.place(relx=0.26, rely=0.45, anchor="center", width=520, height=175)
        self.lblAns1.place(relx=0.26, rely=0.45, anchor="center")
        # Top-right
        self.btnAns2.place(relx=0.74, rely=0.45, anchor="center", width=520, height=175)
        self.lblAns2.place(relx=0.74, rely=0.45, anchor="center")
        # Bottom-left
        self.btnAns3.place(relx=0.26, rely=0.78, anchor="center", width=520, height=175)
        self.lblAns3.place(relx=0.26, rely=0.78, anchor="center")
        # Bottom-right
        self.btnAns4.place(relx=0.74, rely=0.78, anchor="center", width=520, height=175)
        self.lblAns4.place(relx=0.74, rely=0.78, anchor="center")
        
        self.btnCancel.place(relx=0.5, rely=0.95, anchor="center")

    def showResults(self):
        """
        Private - calculate the final score and display the results panel.

        The percentage is stored as a floating-point number (float).
        
        INPUT
            - intTotal
            - intCorrect
            
        PROCESS
            - calculate percentage of correct questions of all the marks
            
        OUTPUT
            - display the percentage correct, amount incorrect and amount correct to the screen
        """
        hideAll()

        intTotal = len(self.allQuestions) # int
        
        # Calculate score as floating-point percentage (float data type)
        fltPercentage = (self.intCorrect / intTotal) * 100.0

        self.lblResults.place(relx=0.5, rely=0.08, anchor="center")
        self.frmResults.place(relx=0.5, rely=0.56, anchor="center")

        self.lblCorrectHdr.place(relx=0.25, rely=0.16, anchor="center")
        self.lblCorrect.config(text=str(self.intCorrect))
        self.lblCorrect.place(relx=0.25, rely=0.36, anchor="center")

        self.lblIncorrectHdr.place(relx=0.75, rely=0.16, anchor="center")
        self.lblIncorrect.config(text=str(self.intIncorrect))
        self.lblIncorrect.place(relx=0.75, rely=0.36, anchor="center")

        self.lblScoreHdr.place(relx=0.5, rely=0.62, anchor="center")
        
        # Round float to 1 decimal place for display
        self.lblPercentage.config(text=f"{round(fltPercentage, 1)}%")
        self.lblPercentage.place(relx=0.5, rely=0.76, anchor="center")

        self.btnDone.place(relx=0.5, rely=0.92, anchor="center")

    #  Public answer callbacks 

    def ans1Selected(self):
        """Handle selection of answer tile 1."""
        self.processAnswer(self.lblAns1.cget('text'))

    def ans2Selected(self):
        """Handle selection of answer tile 2."""
        self.processAnswer(self.lblAns2.cget('text'))

    def ans3Selected(self):
        """Handle selection of answer tile 3."""
        self.processAnswer(self.lblAns3.cget('text'))

    def ans4Selected(self):
        """Handle selection of answer tile 4."""
        self.processAnswer(self.lblAns4.cget('text'))

    def getAnswers(self):
        """
        Validate settings, build randomised answer sets for every question,
        and launch the quiz.
        
        INPUT
            - arrQuizToPlay
            
        PROCESS
            - create randomised answer options in a 2-D Array
            
        OUTPUT
            - append the three distractor answers to allAnswers
            - append the corresponding answer to arrQuestions
            - append the corresponding answer position to andPositions

        """
        

        #  Reset quiz-state counters and arrays ─
        self.intN = 0
        self.intCorrect = 0
        self.intIncorrect = 0
        self.allAnswers = []
        self.allQuestions = []
        self.ansPositions = []

        arrPossible = []   # distractor pool for current question

        # Build 2-D array of randomised answer options (iteration)
        for strQuestion, strAnswer in page6.arrQuizToPlay:
            # Collect all other answers as possible distractors
            for qa in page6.arrQuizToPlay:
                if qa[1] != strAnswer:   # inequality comparison
                    arrPossible.append(qa[1])

            # Randomly sample 3 distractors without replacement
            arrDistractors = random.sample(arrPossible, 3)

            # Pick a random position (0–3) for the correct answer
            intAnsPos: int = random.randint(0, 3)
            arrDistractors.insert(intAnsPos, strAnswer)

            self.allAnswers.append(arrDistractors)     # row in 2-D array
            self.allQuestions.append(strQuestion)
            self.ansPositions.append(intAnsPos)
            arrPossible = []   # reset for next iteration

        hideAll()
        self.showQuestion()

    def finishKahoot(self):
        """Return to the main quiz dashboard."""
        showPage2()

    def show(self):
        """Display the Kahoot settings panel."""
        hideAll()
        self.lblKahoot.place(relx=0.5, rely=0.10, anchor="center")
        self.lblSubtitle.place(relx=0.5, rely=0.19, anchor="center")
        self.frmSettings.place(relx=0.5, rely=0.54, anchor="center")
        
        self.btnStart.place(relx=0.5, rely=0.5, anchor="center")
        

    def hide(self):
        """Remove all Kahoot mode widgets from the screen."""
        for w in (self.lblKahoot, self.lblSubtitle, self.frmSettings,
                  self.btnStart,
                  self.lblQuestion,
                  self.btnAns1, self.lblAns1,
                  self.btnAns2, self.lblAns2,
                  self.btnAns3, self.lblAns3,
                  self.btnAns4, self.lblAns4,
                  self.lblResults, self.frmResults,
                  self.lblCorrectHdr, self.lblCorrect,
                  self.lblIncorrectHdr, self.lblIncorrect,
                  self.lblScoreHdr, self.lblPercentage,
                  self.btnDone, self.btnCancel):
            w.place_forget()



#  INSTANTIATE PAGE OBJECTS


page1 = logInPage()       # Login page          – logInPage(FormPage -> BasePage)
page2 = mainPage()        # Main dashboard      – mainPage(BasePage)
page3 = newAccPage()      # Sign-Up page        – newAccPage(FormPage -> BasePage)
page4 = manageAccPage()   # Manage account      – manageAccPage(BasePage)
page5 = newQuizPage()     # Create quiz         – newQuizPage(FormPage -> BasePage)
page6 = playQuizPage()    # Play mode selection – playQuizPage(BasePage)
page7 = flashCardPage()   # Flashcard mode      – flashCardPage(BasePage)
page8 = kahootPage()      # Kahoot/Quiz mode    – kahootPage(FormPage -> BasePage)



#  LAUNCH APPLICATION


showPage1()       # Start at the login screen
app.mainloop()     # Enter the Tkinter event loop
