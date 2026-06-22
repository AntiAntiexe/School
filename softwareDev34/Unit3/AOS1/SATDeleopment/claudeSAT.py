"""
Squiz – A quiz creation and study application.
VCE Software Development – Unit 4 AOS1

OOP Language: Python 3  |  GUI Library: Tkinter
File formats used: CSV (delimited)

Inheritance hierarchy:
    BasePage
    ├── FormPage          (generalises shared form-entry behaviour)
    │   ├── logInPage     (page 1)
    │   ├── newAccPage    (page 3)
    │   ├── newQuizPage   (page 5)
    │   └── kahootPage    (page 8)
    ├── mainPage          (page 2)
    ├── manageAccPage     (page 4)
    ├── playQuizPage      (page 6)
    └── flashCardPage     (page 7)
"""

import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import time


# ══════════════════════════════════════════════════════════════════════
#  CONSTANTS  (global, read-only – named in UPPER_SNAKE_CASE)
# ══════════════════════════════════════════════════════════════════════

ACCOUNTS_FILE_PATH  = 'softwareDev34/Unit3/AOS1/SATDeleopment/accounts.csv'
QUIZZES_FILE_PATH   = 'softwareDev34/Unit3/AOS1/SATDeleopment/quizzesArray.csv'
ICON_FILE_PATH      = 'softwareDev34/Unit3/AOS1/SATDeleopment/whiteArrowIcon.png'

MIN_PASSWORD_LENGTH = 8    # int – minimum characters required for a valid password
MIN_QUESTIONS       = 5    # int – minimum Q&A pairs required to save a quiz
MAX_QUESTION_LENGTH = 37   # int – max characters allowed in one question field
MAX_ANSWER_LENGTH   = 13   # int – max characters allowed in one answer field
MIN_TIME_PER_Q      = 5    # int – minimum seconds per Kahoot question (range check)
MAX_TIME_PER_Q      = 120  # int – maximum seconds per Kahoot question (range check)
DEFAULT_TIME_PER_Q  = 30   # int – default seconds per Kahoot question


# ══════════════════════════════════════════════════════════════════════
#  COLOUR PALETTE  (global dict – text type: str)
# ══════════════════════════════════════════════════════════════════════

colours = {
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


# ══════════════════════════════════════════════════════════════════════
#  APPLICATION WINDOW
# ══════════════════════════════════════════════════════════════════════

app = tk.Tk()
app.title("Squiz")
app.geometry("1100x800")
app.resizable(False, False)
app.configure(bg=colours["bg"])


# ══════════════════════════════════════════════════════════════════════
#  FONTS  (global tuples – used across all pages)
# ══════════════════════════════════════════════════════════════════════

font_title    = ("Helvetica", 48, "bold")     # page headings
font_subtitle = ("Helvetica", 28, "bold")     # section headings
font_para     = ("Helvetica", 22, "normal")   # body / entry text
small_bold    = ("Helvetica", 16, "bold")     # quiz card title
small_font    = ("Helvetica", 16, "normal")   # muted / secondary text
font_answer   = ("Helvetica", 18, "bold")     # Kahoot answer label text
font_huge     = ("Helvetica", 72, "bold")     # large score numbers


# ══════════════════════════════════════════════════════════════════════
#  TTK STYLE CONFIGURATION
# ══════════════════════════════════════════════════════════════════════

style = ttk.Style()
style.theme_use('classic')

# ── Buttons ──────────────────────────────────────────────────────────

# Primary action button (large)
style.configure('TButton',
    font=font_para,
    background=colours["primary"],
    foreground=colours["lightText"],
    borderwidth=0, relief="flat",
    focusthickness=0, highlightthickness=0,
    padding=(24, 10))
style.map('TButton',
    background=[('active', colours["primaryHov"])])

# Secondary / smaller button
style.configure('Secondary.TButton',
    font=small_font,
    background=colours["primary"],
    foreground=colours["lightText"],
    borderwidth=0, relief="flat",
    focusthickness=0, highlightthickness=0,
    padding=(14, 7))
style.map('Secondary.TButton',
    background=[('active', colours["primaryHov"])])

# Ghost sidebar button
style.configure('Sidebar.TButton',
    font=small_font,
    background=colours["sidebar"],
    foreground=colours["muted"],
    borderwidth=0, relief="flat",
    focusthickness=0, highlightthickness=0,
    padding=(14, 10))
style.map('Sidebar.TButton',
    background=[('active', colours["border"])],
    foreground=[('active', colours["text"])])

# Destructive / danger button
style.configure('Danger.TButton',
    font=font_para,
    background=colours["danger"],
    foreground=colours["lightText"],
    borderwidth=0, relief="flat",
    focusthickness=0, highlightthickness=0,
    padding=(24, 10))
style.map('Danger.TButton',
    background=[('active', colours["dangerHov"])])

# Kahoot answer tile (large square button – text hidden; label is overlaid)
style.configure('Tile.TButton',
    padding=20,
    font=("Helvetica", 60),
    background=colours["answerTile"],
    foreground=colours["answerTile"],   # invisible placeholder text
    borderwidth=0, relief="flat",
    focusthickness=0, highlightthickness=0)
style.map('Tile.TButton',
    background=[('active', colours["border"])],
    foreground=[('active', colours["border"])])

# ── Labels ───────────────────────────────────────────────────────────

style.configure('TLabel',
    background=colours["bg"],
    foreground=colours["text"])
style.configure('Card.TLabel',
    background=colours["card"],
    foreground=colours["text"])
style.configure('Muted.TLabel',
    background=colours["bg"],
    foreground=colours["muted"])
style.configure('MutedCard.TLabel',
    background=colours["card"],
    foreground=colours["muted"])
style.configure('Sidebar.TLabel',
    background=colours["sidebar"],
    foreground=colours["muted"])
style.configure('SidebarTitle.TLabel',
    background=colours["sidebar"],
    foreground=colours["lightText"])
style.configure('Success.TLabel',
    background=colours["card"],
    foreground=colours["success"])
style.configure('Warning.TLabel',
    background=colours["card"],
    foreground=colours["warning"])
style.configure('TileText.TLabel',
    background=colours["answerTile"],
    foreground=colours["lightText"])

# ── Entry fields ─────────────────────────────────────────────────────

style.configure('TEntry',
    background=colours["inputBg"],
    foreground=colours["lightText"],
    fieldbackground=colours["inputBg"],
    relief="flat", borderwidth=0,
    insertcolor=colours["lightText"])

# ── Frames ───────────────────────────────────────────────────────────

style.configure('TFrame',
    background=colours["card"])
style.configure('Sidebar.TFrame',
    background=colours["sidebar"])
style.configure('BG.TFrame',
    background=colours["bg"])

# ── Scrollbar ────────────────────────────────────────────────────────

style.configure('TScrollbar',
    arrowcolor=colours["primary"],
    relief="flat", arrowsize=0,
    background=colours["border"],
    width=6,
    troughcolor=colours["card"],
    bordercolor=colours["card"],
    borderwidth=0,
    highlightthickness=0)
style.map('TScrollbar',
    background=[('active', colours["primary"])])


# ══════════════════════════════════════════════════════════════════════
#  PAGE NAVIGATION HELPERS  (global functions)
# ══════════════════════════════════════════════════════════════════════

def hide_all() -> None:
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

def show_page1() -> None:
    """Navigate to the Login page (page 1)."""
    page1.show()

def show_page2() -> None:
    """Navigate to the Main dashboard (page 2)."""
    page2.show()

def show_page3() -> None:
    """Navigate to the Sign-Up page (page 3)."""
    page3.show()

def show_page4() -> None:
    """Navigate to the Manage Account page (page 4)."""
    page4.show()

def show_page5() -> None:
    """Navigate to the Create Quiz page (page 5)."""
    page5.show()

def show_page6() -> None:
    """Navigate to the Play Mode Selection page (page 6)."""
    page6.show()

def show_page7() -> None:
    """Navigate to the Flashcard Mode page (page 7)."""
    page7.show()

def show_page8() -> None:
    """Navigate to the Kahoot/Quiz Mode page (page 8)."""
    page8.show()


# ══════════════════════════════════════════════════════════════════════
#  BASE PAGE  –  Abstraction & Generalisation
# ══════════════════════════════════════════════════════════════════════

class BasePage:
    """
    Abstract base class for every page in the application.

    OOP Principles demonstrated:
      • Abstraction    – the internal implementation of each page is
                         hidden; only show() and hide() are exposed.
      • Generalisation – common behaviour (_set_placeholder) is defined
                         once here and shared by all sub-classes.

    All eight page classes inherit from BasePage (or its sub-class
    FormPage), satisfying the requirement for classes, objects,
    inheritance, and access modifiers.
    """

    def show(self) -> None:
        """Display this page.  Must be overridden in every sub-class."""
        raise NotImplementedError("Sub-classes must override show()")

    def hide(self) -> None:
        """Hide this page.  Must be overridden in every sub-class."""
        raise NotImplementedError("Sub-classes must override hide()")

    def _set_placeholder(self,
                         entry_widget,
                         strPlaceholder: str) -> None:
        """
        Protected helper – restore placeholder text in an Entry widget.

        Using the 'protected' naming convention (_prefix) signals that
        this method is for internal / sub-class use, not external callers.

        Parameters
        ----------
        entry_widget  : ttk.Entry – the widget whose text will be reset
        strPlaceholder: str       – the placeholder string to insert
        """
        entry_widget.delete(0, tk.END)          # clear current content
        entry_widget.insert(0, strPlaceholder)  # restore placeholder text
        entry_widget.config(show='')            # un-mask any password masking


# ══════════════════════════════════════════════════════════════════════
#  FORM PAGE  –  Generalisation & Inheritance
# ══════════════════════════════════════════════════════════════════════

class FormPage(BasePage):
    """
    Intermediate class for pages that contain Entry widgets with
    placeholder text.

    Inherits from BasePage and generalises two shared behaviours:
      • on_entry_click – clears placeholder on focus-in
      • on_focusout    – restores placeholder on focus-out

    Sub-classes: logInPage, newAccPage, newQuizPage, kahootPage.
    Avoids code duplication and demonstrates Inheritance.
    """

    def on_entry_click(self,
                       event,
                       entry_widget,
                       strPlaceholder: str) -> None:
        """
        Clear placeholder text when a user clicks into an Entry field.
        For password fields the characters are masked with '*'.

        Parameters
        ----------
        event         : tkinter event object (unused, required by bind)
        entry_widget  : ttk.Entry – widget that received focus
        strPlaceholder: str       – the placeholder string currently shown
        """
        if entry_widget.get() == strPlaceholder:   # equality comparison
            entry_widget.delete(0, tk.END)
            if strPlaceholder == "Password":        # selection
                entry_widget.config(show='*')       # mask password characters

    def on_focusout(self,
                    event,
                    entry_widget,
                    strPlaceholder: str) -> None:
        """
        Restore placeholder text when the user leaves an empty Entry.

        Parameters
        ----------
        event         : tkinter event object (unused, required by bind)
        entry_widget  : ttk.Entry – widget that lost focus
        strPlaceholder: str       – placeholder string to restore
        """
        if not entry_widget.get():              # existence check (logical NOT)
            self._set_placeholder(entry_widget, strPlaceholder)


# ══════════════════════════════════════════════════════════════════════
#  PAGE 1 – LOGIN PAGE      logInPage(FormPage)
# ══════════════════════════════════════════════════════════════════════

class logInPage(FormPage):
    """
    Login page – authenticates existing users against accounts.csv.

    Algorithm: Binary Search
        The accounts CSV is sorted alphabetically by username.
        Binary search locates the entered username in O(log n) time.

    Data structures:
        __arrUsernames – 1-D array (list[str]) of all usernames from CSV
        __arrPasswords – 1-D array (list[str]) of matching passwords

    Validation:
        • Existence check – username and password fields must not be
                            empty or contain the placeholder text
    """

    def __init__(self) -> None:
        """Initialise all widgets for the login page."""
        super().__init__()

        # ── Public attribute ───────────────────────────────────────
        self.current_username: str = ""   # str – stores the logged-in username
        self.strUsernameToFind: str = ""  # str – last validated username

        # ── Private 1-D arrays (populated on each submit) ─────────
        self.__arrUsernames = []   # list[str] – 1-D array of usernames
        self.__arrPasswords = []   # list[str] – 1-D array of passwords

        # ── Widgets ───────────────────────────────────────────────
        self.lblTitle = ttk.Label(
            master=app, text="Squiz",
            font=font_title, style='TLabel')

        self.lblSubtitle = ttk.Label(
            master=app, text="Create, study, succeed.",
            font=small_font, style='Muted.TLabel')

        self.frLogin = ttk.Frame(
            master=app, style='TFrame', width=480, height=360)

        self.lblFormTitle = ttk.Label(
            master=self.frLogin, text="Welcome back",
            font=font_subtitle, style='Card.TLabel')

        self.entryUsername = ttk.Entry(
            master=self.frLogin, width=22,
            font=font_para, style='TEntry')
        self.entryUsername.insert(0, "Username")

        self.entryPassword = ttk.Entry(
            master=self.frLogin, width=22,
            font=font_para, style='TEntry')
        self.entryPassword.insert(0, "Password")

        self.btnLogin = ttk.Button(
            master=self.frLogin, text="Log In",
            command=self.submit)

        self.lblNoAccount = ttk.Label(
            master=app, text="Don't have an account?",
            font=small_font, style='Muted.TLabel')

        self.btnSignUp = ttk.Button(
            master=app, text="Sign Up",
            command=self.goToNewAcc,
            style='Secondary.TButton')

        # Bind placeholder focus events (inherited from FormPage)
        self.entryUsername.bind(
            '<FocusIn>',
            lambda e: self.on_entry_click(e, self.entryUsername, "Username"))
        self.entryUsername.bind(
            '<FocusOut>',
            lambda e: self.on_focusout(e, self.entryUsername, "Username"))
        self.entryPassword.bind(
            '<FocusIn>',
            lambda e: self.on_entry_click(e, self.entryPassword, "Password"))
        self.entryPassword.bind(
            '<FocusOut>',
            lambda e: self.on_focusout(e, self.entryPassword, "Password"))
        # Allow the Enter key to submit
        self.entryPassword.bind('<Return>', lambda e: self.submit())

    # ── Public methods ─────────────────────────────────────────────

    def show(self) -> None:
        """Display the login page and bring widgets to the front."""
        hide_all()
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
        try:
            self.frLogin.lift()
            self.lblTitle.lift()
            self.lblSubtitle.lift()
            self.lblNoAccount.lift()
            self.btnSignUp.lift()
        except Exception:
            pass

    def hide(self) -> None:
        """Remove all login widgets from the screen."""
        for w in (self.lblTitle, self.lblSubtitle, self.frLogin,
                  self.lblFormTitle, self.entryUsername,
                  self.entryPassword, self.btnLogin,
                  self.lblNoAccount, self.btnSignUp):
            w.place_forget()

    def goToNewAcc(self) -> None:
        """Navigate to the Sign-Up page."""
        show_page3()

    def submit(self) -> None:
        """
        Read accounts.csv into 1-D arrays and run a Binary Search to
        authenticate the entered username/password combination.

        Binary Search requires the array to be sorted A-Z by username.
        Time complexity: O(log n)

        Validation applied:
            • Existence check – both fields must contain non-empty,
                                non-placeholder text before the search runs
        """
        # ── Load accounts into 1-D arrays from CSV (read from data source)
        self.__arrUsernames = []
        self.__arrPasswords = []
        with open(ACCOUNTS_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.__arrUsernames.append(row[0])   # text (str) – username
                self.__arrPasswords.append(row[1])   # text (str) – password

        # ── Retrieve and sanitise input ────────────────────────────
        self.strUsernameToFind = self.entryUsername.get().strip()
        strPasswordToFind: str  = self.entryPassword.get()

        # Existence checks – fields must not be empty or placeholder text
        if not self.strUsernameToFind or self.strUsernameToFind == "Username":
            messagebox.showwarning("Missing Field",
                                   "Please enter your username.")
            return
        if not strPasswordToFind or strPasswordToFind == "Password":
            messagebox.showwarning("Missing Field",
                                   "Please enter your password.")
            return

        # ── Binary Search ──────────────────────────────────────────
        intLow:  int  = 0
        intHigh: int  = len(self.__arrUsernames) - 1   # int
        bFound:  bool = False                           # Boolean flag

        while not bFound and intLow <= intHigh:   # logical NOT; ≤ operator
            intMid: int = (intLow + intHigh) // 2  # integer division

            if self.__arrUsernames[intMid] == self.strUsernameToFind:
                # Username found; now verify password
                if self.__arrPasswords[intMid] == strPasswordToFind:
                    bFound = True
                    self.current_username = self.strUsernameToFind
                else:
                    # Username match but wrong password – keep searching
                    intLow = intMid + 1   # increment
            elif self.__arrUsernames[intMid] > self.strUsernameToFind:
                intHigh = intMid - 1      # decrement
            else:
                intLow = intMid + 1       # increment

        # ── Result ────────────────────────────────────────────────
        if bFound:
            messagebox.showinfo("Login Successful",
                                f"Welcome back, {self.current_username}!")
            page2.show()
        else:
            messagebox.showwarning("Login Failed",
                                   "Incorrect username or password. "
                                   "Please try again.")


# ══════════════════════════════════════════════════════════════════════
#  PAGE 2 – MAIN DASHBOARD      mainPage(BasePage)
# ══════════════════════════════════════════════════════════════════════

class mainPage(BasePage):
    """
    Main dashboard – displays the logged-in user's quizzes in a
    scrollable, sortable list.

    Algorithm: Selection Sort (ascending or descending) toggled by
    clicking the Sort button.  Time complexity: O(n²).

    Data structures:
        quizzes       – 2-D array (list of CSV rows; each row is a record)
        quiz_frames   – 1-D array of widget references (for cleanup)

    Record structure for each quiz (field accessed by index):
        [0] title    – text  (str)
        [1] username – text  (str)
        [2] qa_data  – text  (str, string representation of a 2-D list)
    """

    def __init__(self) -> None:
        """Initialise sidebar, scrollable list, and header widgets."""
        super().__init__()

        # ── Private state ──────────────────────────────────────────
        self.__intSortClicks: int = 0   # int – tracks sort direction toggle

        # ── Public quiz data (2-D array) ──────────────────────────
        self.quizzes = []   # list[list] – each inner list is a quiz record

        # ── 1-D arrays of dynamic widget references ────────────────
        self.quiz_frames  = []
        self.quiz_labels  = []
        self.quiz_buttons = []

        # ── Sidebar frame ─────────────────────────────────────────
        self.frmSidebar = ttk.Frame(
            app, style='Sidebar.TFrame', width=200, height=800)

        self.lblAppName = ttk.Label(
            master=self.frmSidebar, text="Squiz",
            font=font_subtitle, style='SidebarTitle.TLabel')
        self.lblAppTag = ttk.Label(
            master=self.frmSidebar, text="my quizzes",
            font=small_font, style='Sidebar.TLabel')

        self.btnSort = ttk.Button(
            master=self.frmSidebar, text="⇅  Sort A–Z",
            command=self.sort, style='Sidebar.TButton')
        self.btnAdd = ttk.Button(
            master=self.frmSidebar, text="＋  New Quiz",
            command=self.add, style='Sidebar.TButton')
        self.btnManage = ttk.Button(
            master=self.frmSidebar, text="⚙  Account",
            command=self.managePage, style='Sidebar.TButton')
        self.btnLogout = ttk.Button(
            master=self.frmSidebar, text="← Log Out",
            command=show_page1, style='Sidebar.TButton')

        # ── Content area header ───────────────────────────────────
        self.lblPageTitle = ttk.Label(
            master=app, text="My Quizzes",
            font=font_title, style='TLabel')

        # ── Scrollable canvas for quiz cards ─────────────────────
        self.canvas = Canvas(
            app, bg=colours["bg"],
            highlightthickness=0, borderwidth=0, relief="flat")
        self.scrollbar = ttk.Scrollbar(
            master=self.canvas, orient="vertical",
            command=self.canvas.yview, style='TScrollbar')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_frame = Frame(self.canvas, bg=colours["bg"])
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")))
        self.canvas_window = self.canvas.create_window(
            (20, 10), window=self.scrollable_frame, anchor="nw")

        # Bind mouse-wheel scrolling for Windows and macOS
        self.canvas.bind(
            "<MouseWheel>",
            lambda e: self.canvas.yview_scroll(
                -1 * (e.delta // 120), "units"))

    # ── Private helpers ────────────────────────────────────────────

    def __buildQuizCard(self, intIndex: int) -> None:
        """
        Private – create one quiz-card widget and append it to the
        scroll area.

        Parameters
        ----------
        intIndex : int – position of the quiz in self.quizzes (2-D array)
        """
        # Access record field [0] (title – text type)
        strQuizTitle: str = self.quizzes[intIndex][0]

        frmQuiz = ttk.Frame(
            self.scrollable_frame, style='TFrame', width=740, height=65)
        frmQuiz.pack(pady=6, padx=15)
        frmQuiz.pack_propagate(False)   # maintain fixed height

        lblQuiz = ttk.Label(
            master=frmQuiz, text=strQuizTitle,
            font=small_bold, style='Card.TLabel')
        btnPlay = ttk.Button(
            master=frmQuiz, text="Play →",
            command=lambda i=intIndex: self.playQuiz(i),
            style='Secondary.TButton')

        lblQuiz.place(relx=0.04, rely=0.5, anchor="w")
        btnPlay.place(relx=0.96, rely=0.5, anchor="e")

        # Append to 1-D tracking arrays for cleanup later
        self.quiz_labels.append(lblQuiz)
        self.quiz_buttons.append(btnPlay)
        self.quiz_frames.append(frmQuiz)

    # ── Public methods ─────────────────────────────────────────────

    def getQuizzes(self) -> list:
        """
        Read quizzesArray.csv (CSV, delimited) into a 2-D array and
        filter rows that belong to the logged-in user.

        Returns
        -------
        list[list] – 2-D array of quiz records (or empty list)

        Each row is a record with fields at fixed indices:
            [0] title    : str
            [1] username : str
            [2] qa_data  : str (string repr of a 2-D list)
        """
        strUsername: str = getattr(page1, 'strUsernameToFind', '').strip()
        if not strUsername:   # existence check – must have a logged-in user
            return []

        arrAllData = []   # 1-D array of raw rows; each row is itself a list

        with open(QUIZZES_FILE_PATH) as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                arrAllData.append(row)   # build 2-D array

        # Filter rows whose username field matches the current user
        arrUserQuizzes = [row for row in arrAllData
                          if row[1].strip() == strUsername]
        return arrUserQuizzes

    def playQuiz(self, intQuizIndex: int) -> None:
        """
        Load the chosen quiz and navigate to the play-mode page.

        Parameters
        ----------
        intQuizIndex : int – index of the selected quiz in self.quizzes
        """
        page6.getQuizToPlay(intQuizIndex)
        show_page6()

    def sort(self) -> None:
        """
        Toggle between ascending (A→Z) and descending (Z→A) order
        using the Selection Sort algorithm.

        Selection Sort:
            For each position i, scan the remainder to find the
            minimum (or maximum) and swap it into position i.
            Time complexity: O(n²)
        """
        self.__intSortClicks += 1   # increment click counter
        intN: int = len(self.quizzes)

        if self.__intSortClicks % 2 == 0:   # modulus – even → descending
            self.btnSort.config(text="⇅  Sort A–Z")
            # ── Descending Selection Sort (Z → A) ─────────────────
            for i in range(intN - 1):
                intMaxIdx: int = i
                for j in range(i + 1, intN):
                    if self.quizzes[j][0].lower() > \
                            self.quizzes[intMaxIdx][0].lower():   # > operator
                        intMaxIdx = j
                if intMaxIdx != i:
                    # Swap quiz records in the 2-D array
                    self.quizzes[i], self.quizzes[intMaxIdx] = \
                        self.quizzes[intMaxIdx], self.quizzes[i]
        else:
            self.btnSort.config(text="⇅  Sort Z–A")
            # ── Ascending Selection Sort (A → Z) ──────────────────
            for i in range(intN - 1):
                intMinIdx: int = i
                for j in range(i + 1, intN):
                    if self.quizzes[j][0].lower() < \
                            self.quizzes[intMinIdx][0].lower():   # < operator
                        intMinIdx = j
                if intMinIdx != i:
                    self.quizzes[i], self.quizzes[intMinIdx] = \
                        self.quizzes[intMinIdx], self.quizzes[i]

        self.show(reload_quizzes=False)   # re-render with sorted order

    def add(self) -> None:
        """Navigate to the Create Quiz page."""
        show_page5()

    def managePage(self) -> None:
        """Navigate to the Manage Account page."""
        page4.show()

    def show(self, reload_quizzes: bool = True) -> None:
        """
        Display the main dashboard.

        Parameters
        ----------
        reload_quizzes : bool – True  → re-read quizzes from CSV
                                False → use current self.quizzes (after sort)
        """
        hide_all()
        self.hide()   # destroy previously rendered quiz cards

        if reload_quizzes:
            self.quizzes = self.getQuizzes()
        if self.quizzes is None:
            self.quizzes = []

        # ── Place sidebar ──────────────────────────────────────────
        self.frmSidebar.place(x=0, y=0, width=200, height=800)
        self.lblAppName.place(relx=0.5, rely=0.06, anchor="center")
        self.lblAppTag.place(relx=0.5, rely=0.12, anchor="center")
        self.btnSort.place(relx=0.5, rely=0.30, anchor="center",
                           width=170)
        self.btnAdd.place(relx=0.5, rely=0.40, anchor="center",
                          width=170)
        self.btnManage.place(relx=0.5, rely=0.50, anchor="center",
                             width=170)
        self.btnLogout.place(relx=0.5, rely=0.94, anchor="center",
                             width=170)

        # ── Place content area ─────────────────────────────────────
        self.lblPageTitle.place(relx=0.62, rely=0.09, anchor="center")
        self.canvas.place(relx=0.62, rely=0.57, anchor="center",
                          width=820, height=550)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Render a quiz card for each quiz record (iteration over 2-D array)
        for i in range(len(self.quizzes)):
            self.__buildQuizCard(i)

        # Show empty-state hint when the user has no quizzes yet
        if len(self.quizzes) == 0:
            ttk.Label(
                master=self.scrollable_frame,
                text="No quizzes yet — press ＋ New Quiz to get started",
                font=small_font, style='Muted.TLabel'
            ).pack(pady=40)

    def hide(self) -> None:
        """Destroy quiz cards and hide all static widgets."""
        # Destroy dynamically created quiz cards (iteration over 1-D array)
        for frame in self.quiz_frames:
            frame.destroy()
        self.quiz_labels.clear()
        self.quiz_buttons.clear()
        self.quiz_frames.clear()

        # Hide static widgets
        self.frmSidebar.place_forget()
        self.lblPageTitle.place_forget()
        self.scrollbar.pack_forget()

        # Lower the canvas below the login frame to prevent it covering page 1
        try:
            self.canvas.lower(page1.frLogin)
        except Exception:
            try:
                self.canvas.lower()
            except Exception:
                pass


# ══════════════════════════════════════════════════════════════════════
#  PAGE 3 – SIGN-UP PAGE      newAccPage(FormPage)
# ══════════════════════════════════════════════════════════════════════

class newAccPage(FormPage):
    """
    Registration page for new users.

    Validation applied (all three required techniques):
        1. Existence check   – username and password must not be empty
        2. Type check        – username must be alphanumeric/underscore only
        3. Range check       – password must be ≥ MIN_PASSWORD_LENGTH chars
        4. Uniqueness check  – Linear Search to confirm username is free
    """

    def __init__(self) -> None:
        """Initialise all sign-up page widgets."""
        super().__init__()

        # ── Private 1-D arrays ────────────────────────────────────
        self.__arrUsernames = []   # list[str]
        self.__arrPasswords = []   # list[str]

        # ── Widgets ───────────────────────────────────────────────
        self.lblTitle = ttk.Label(
            master=app, text="Create Account",
            font=font_title, style='TLabel')
        self.lblSubtitle = ttk.Label(
            master=app, text="Join Squiz today — it's free.",
            font=small_font, style='Muted.TLabel')

        self.frmSignUp = ttk.Frame(
            master=app, style='TFrame', width=480, height=380)
        self.lblFormTitle = ttk.Label(
            master=self.frmSignUp, text="Sign Up",
            font=font_subtitle, style='Card.TLabel')

        self.entryNewUsername = ttk.Entry(
            master=self.frmSignUp, width=22,
            font=font_para, style='TEntry')
        self.entryNewUsername.insert(0, "Username")

        self.entryNewPassword = ttk.Entry(
            master=self.frmSignUp, width=22,
            font=font_para, style='TEntry')
        self.entryNewPassword.insert(0, "Password")

        self.btnSubmit = ttk.Button(
            master=self.frmSignUp, text="Create Account",
            command=self.createNewAcc)
        self.btnBackToLogin = ttk.Button(
            master=app, text="← Back to Login",
            command=self.goToLogin,
            style='Secondary.TButton')

        # Bind placeholder focus events (inherited from FormPage)
        self.entryNewUsername.bind(
            '<FocusIn>',
            lambda e: self.on_entry_click(e, self.entryNewUsername, "Username"))
        self.entryNewUsername.bind(
            '<FocusOut>',
            lambda e: self.on_focusout(e, self.entryNewUsername, "Username"))
        self.entryNewPassword.bind(
            '<FocusIn>',
            lambda e: self.on_entry_click(e, self.entryNewPassword, "Password"))
        self.entryNewPassword.bind(
            '<FocusOut>',
            lambda e: self.on_focusout(e, self.entryNewPassword, "Password"))

    # ── Public methods ─────────────────────────────────────────────

    def goToLogin(self) -> None:
        """Return to the Login page."""
        show_page1()

    def createNewAcc(self) -> None:
        """
        Validate input and write a new account record to accounts.csv.

        Validation sequence:
            1. Existence check  – fields must not be empty or placeholder
            2. Type check       – username must be alphanumeric/underscore
            3. Uniqueness check – Linear Search through existing usernames
            4. Range check      – password length ≥ MIN_PASSWORD_LENGTH
        """
        # ── Load existing accounts into 1-D arrays ─────────────────
        self.__arrUsernames = []
        self.__arrPasswords = []
        with open(ACCOUNTS_FILE_PATH, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.__arrUsernames.append(row[0])
                self.__arrPasswords.append(row[1])

        strNewUsername: str = self.entryNewUsername.get().strip()
        strNewPassword: str = self.entryNewPassword.get()

        # ── 1. Existence check – username ──────────────────────────
        if not strNewUsername or strNewUsername == "Username":
            messagebox.showwarning("Missing Username",
                                   "Please enter a username.")
            return

        # ── 2. Type check – alphanumeric characters and underscores only
        bValidChars: bool = all(
            ch.isalnum() or ch == '_' for ch in strNewUsername)
        if not bValidChars:   # logical NOT
            messagebox.showwarning("Invalid Username",
                                   "Username may only contain letters, "
                                   "numbers and underscores ( _ ).")
            return

        # ── 3. Uniqueness check – Linear Search through 1-D array ──
        for i in range(len(self.__arrUsernames)):   # iteration
            if strNewUsername == self.__arrUsernames[i]:   # equality
                messagebox.showwarning("Username Taken",
                                       "That username is already in use. "
                                       "Please choose a different one.")
                return

        # ── 1. Existence check – password ─────────────────────────
        if not strNewPassword or strNewPassword == "Password":
            messagebox.showwarning("Missing Password",
                                   "Please enter a password.")
            return

        # ── 4. Range check – password must be long enough ─────────
        if len(strNewPassword) < MIN_PASSWORD_LENGTH:   # < comparison
            messagebox.showwarning("Weak Password",
                                   f"Password must be at least "
                                   f"{MIN_PASSWORD_LENGTH} characters long.")
            return

        # ── Write new account record to CSV (write to data source) ─
        with open(ACCOUNTS_FILE_PATH, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([strNewUsername, strNewPassword])

        messagebox.showinfo("Account Created",
                            "Your account has been created. Please log in.")
        show_page1()

    def show(self) -> None:
        """Display the sign-up page."""
        hide_all()
        self.lblTitle.place(relx=0.5, rely=0.10, anchor="center")
        self.lblSubtitle.place(relx=0.5, rely=0.19, anchor="center")
        self.frmSignUp.place(relx=0.5, rely=0.54, anchor="center")
        self.lblFormTitle.place(relx=0.5, rely=0.14, anchor="center")
        self.entryNewUsername.place(relx=0.5, rely=0.35, anchor="center")
        self.entryNewPassword.place(relx=0.5, rely=0.55, anchor="center")
        self.btnSubmit.place(relx=0.5, rely=0.76, anchor="center")
        self.btnBackToLogin.place(relx=0.5, rely=0.93, anchor="center")

    def hide(self) -> None:
        """Remove all sign-up widgets from the screen."""
        for w in (self.lblTitle, self.lblSubtitle, self.frmSignUp,
                  self.lblFormTitle, self.entryNewUsername,
                  self.entryNewPassword, self.btnSubmit,
                  self.btnBackToLogin):
            w.place_forget()


# ══════════════════════════════════════════════════════════════════════
#  PAGE 4 – MANAGE ACCOUNT PAGE      manageAccPage(BasePage)
# ══════════════════════════════════════════════════════════════════════

class manageAccPage(BasePage):
    """
    Account management page.

    Allows the logged-in user to permanently delete their account and
    all associated quizzes from both CSV files.
    """

    def __init__(self) -> None:
        """Initialise widgets for the manage account page."""
        super().__init__()

        self.lblTitle = ttk.Label(
            master=app, text="My Account",
            font=font_title, style='TLabel')
        self.lblSubtitle = ttk.Label(
            master=app, text="Manage your Squiz account settings.",
            font=small_font, style='Muted.TLabel')

        self.frmManage = ttk.Frame(
            master=app, style='TFrame', width=520, height=320)
        self.lblWarningHeader = ttk.Label(
            master=self.frmManage, text="Danger Zone",
            font=small_bold, style='Warning.TLabel')
        self.lblWarning = ttk.Label(
            master=self.frmManage,
            text="Deleting your account is permanent\n"
                 "and removes all your quizzes.",
            font=small_font, style='MutedCard.TLabel')
        self.btnDeleteAcc = ttk.Button(
            master=self.frmManage, text="Delete My Account",
            command=self.deleteAcc, style='Danger.TButton')
        self.btnDone = ttk.Button(
            master=self.frmManage, text="← Back to Quizzes",
            command=self.done)

    def done(self) -> None:
        """Return to the main quiz dashboard."""
        page2.show()

    def deleteAcc(self) -> None:
        """
        Confirm deletion, then remove the user's record from both CSVs.

        Writes the filtered lines back to each file (write to data source).
        """
        bConfirmed: bool = messagebox.askyesno(
            "Delete Account",
            "Are you sure you want to permanently delete your account?\n"
            "All your quizzes will be lost.")

        if not bConfirmed:   # logical NOT – user chose 'No'
            return

        strUsername: str = getattr(page1, 'strUsernameToFind', '').strip()
        if not strUsername:   # existence check
            messagebox.showerror("Error",
                                 "Could not identify the logged-in account.")
            return

        # ── Remove user from accounts.csv ──────────────────────────
        with open(ACCOUNTS_FILE_PATH, mode='r') as file:
            arrLines = file.readlines()   # 1-D array of file lines
        arrUpdated = [ln for ln in arrLines
                      if not ln.startswith(strUsername + ',')]
        with open(ACCOUNTS_FILE_PATH, mode='w') as file:
            file.writelines(arrUpdated)

        # ── Remove user's quizzes from quizzesArray.csv ────────────
        with open(QUIZZES_FILE_PATH, mode='r') as file:
            arrLines = file.readlines()
        arrUpdated = [ln for ln in arrLines
                      if not (';' + strUsername + ';') in ln]
        with open(QUIZZES_FILE_PATH, mode='w') as file:
            file.writelines(arrUpdated)

        messagebox.showinfo("Account Deleted",
                            "Your account has been successfully deleted.")
        show_page1()

    def show(self) -> None:
        """Display the manage account page."""
        hide_all()
        self.lblTitle.place(relx=0.5, rely=0.12, anchor="center")
        self.lblSubtitle.place(relx=0.5, rely=0.21, anchor="center")
        self.frmManage.place(relx=0.5, rely=0.55, anchor="center")
        self.lblWarningHeader.place(relx=0.5, rely=0.18, anchor="center")
        self.lblWarning.place(relx=0.5, rely=0.34, anchor="center")
        self.btnDeleteAcc.place(relx=0.5, rely=0.58, anchor="center")
        self.btnDone.place(relx=0.5, rely=0.80, anchor="center")

    def hide(self) -> None:
        """Remove all manage account widgets from the screen."""
        for w in (self.lblTitle, self.lblSubtitle, self.frmManage,
                  self.lblWarningHeader, self.lblWarning,
                  self.btnDeleteAcc, self.btnDone):
            w.place_forget()


# ══════════════════════════════════════════════════════════════════════
#  PAGE 5 – CREATE QUIZ PAGE      newQuizPage(FormPage)
# ══════════════════════════════════════════════════════════════════════

class newQuizPage(FormPage):
    """
    Page for building a new quiz question by question.

    Data structures:
        __arrQuizQuestions – 1-D array (list[str]) of entered questions
        __arrQuizAnswers   – 1-D array (list[str]) of matching answers
        Together they form a 2-D structure when zipped for CSV storage.

    Validation:
        • Existence check – question, answer, title must not be empty
        • Range check     – question ≤ MAX_QUESTION_LENGTH characters
                            answer   ≤ MAX_ANSWER_LENGTH characters
                            at least MIN_QUESTIONS pairs before saving
    """

    def __init__(self) -> None:
        """Initialise all create-quiz page widgets."""
        super().__init__()

        # ── Private 1-D arrays ────────────────────────────────────
        self.__arrQuizQuestions = []   # list[str]
        self.__arrQuizAnswers   = []   # list[str]

        # ── Widgets ───────────────────────────────────────────────
        self.lblTitle = ttk.Label(
            master=app, text="Create Quiz",
            font=font_title, style='TLabel')

        self.lblCount = ttk.Label(
            master=app, text=f"Questions added: 0  (minimum {MIN_QUESTIONS})",
            font=small_font, style='Muted.TLabel')

        self.frmCard = ttk.Frame(
            master=app, style='TFrame', width=580, height=440)

        self.entryQuizTitle = ttk.Entry(
            master=self.frmCard, width=26,
            font=font_para, style='TEntry')
        self.entryQuizTitle.insert(0, "Quiz Title")

        self.lblDivider = ttk.Label(
            master=self.frmCard, text="── Add Questions ──",
            font=small_font, style='MutedCard.TLabel')

        self.entryQuestion = ttk.Entry(
            master=self.frmCard, width=26,
            font=font_para, style='TEntry')
        self.entryQuestion.insert(0, "Question")

        self.entryAnswer = ttk.Entry(
            master=self.frmCard, width=26,
            font=font_para, style='TEntry')
        self.entryAnswer.insert(0, "Answer")

        self.btnNext = ttk.Button(
            master=self.frmCard, text="Add Question ＋",
            command=self.nextQuestion)
        self.btnFinish = ttk.Button(
            master=self.frmCard, text="Save Quiz ✓",
            command=self.finishQuiz)
        self.btnExit = ttk.Button(
            master=app, text="Discard",
            command=self.exit,
            style='Secondary.TButton')

        # Bind placeholder events (inherited from FormPage)
        for entry, placeholder in [
            (self.entryQuizTitle, "Quiz Title"),
            (self.entryQuestion,  "Question"),
            (self.entryAnswer,    "Answer"),
        ]:
            entry.bind(
                '<FocusIn>',
                lambda e, w=entry, p=placeholder:
                    self.on_entry_click(e, w, p))
            entry.bind(
                '<FocusOut>',
                lambda e, w=entry, p=placeholder:
                    self.on_focusout(e, w, p))

    # ── Public methods ─────────────────────────────────────────────

    def exit(self) -> None:
        """Confirm discard and return to the main dashboard."""
        bConfirmed: bool = messagebox.askyesno(
            "Discard Quiz",
            "Exit without saving? All questions will be lost.")
        if bConfirmed:   # selection
            self.__arrQuizQuestions.clear()
            self.__arrQuizAnswers.clear()
            self.lblCount.config(
                text=f"Questions added: 0  (minimum {MIN_QUESTIONS})")
            show_page2()

    def nextQuestion(self) -> None:
        """
        Validate the current Q&A pair and append to the 1-D arrays.

        Validation:
            • Existence check – both fields must not be empty
            • Range check     – lengths must not exceed defined limits
        """
        strQuestion: str = self.entryQuestion.get().strip()
        strAnswer:   str = self.entryAnswer.get().strip()

        # Existence checks
        if not strQuestion or strQuestion == "Question":
            messagebox.showwarning("Missing Question",
                                   "Please type a question before adding.")
            return
        if not strAnswer or strAnswer == "Answer":
            messagebox.showwarning("Missing Answer",
                                   "Please type an answer before adding.")
            return

        # Range checks
        if len(strQuestion) > MAX_QUESTION_LENGTH:   # > operator
            messagebox.showwarning("Question Too Long",
                                   f"Questions must be ≤ "
                                   f"{MAX_QUESTION_LENGTH} characters.")
            return
        if len(strAnswer) > MAX_ANSWER_LENGTH:
            messagebox.showwarning("Answer Too Long",
                                   f"Answers must be ≤ "
                                   f"{MAX_ANSWER_LENGTH} characters.")
            return

        # Append to 1-D arrays
        self.__arrQuizQuestions.append(strQuestion)
        self.__arrQuizAnswers.append(strAnswer)

        # Update counter display
        intCount: int = len(self.__arrQuizQuestions)   # int – current count
        self.lblCount.config(
            text=f"Questions added: {intCount}  (minimum {MIN_QUESTIONS})")

        # Reset entry fields to their placeholders
        self._set_placeholder(self.entryQuestion, "Question")
        self._set_placeholder(self.entryAnswer,   "Answer")

    def finishQuiz(self) -> None:
        """
        Validate the completed quiz and write it to quizzesArray.csv.

        Builds a 2-D list of [question, answer] pairs and stores it as a
        single CSV field, along with the title and owner username.

        Validation:
            • Existence check – title must not be empty
            • Range check     – at least MIN_QUESTIONS questions required
        """
        strQuizTitle: str = self.entryQuizTitle.get().strip()

        # Existence check – title
        if not strQuizTitle or strQuizTitle == "Quiz Title":
            messagebox.showwarning("Missing Title",
                                   "Please enter a title for your quiz.")
            return

        # Range check – minimum question count
        if len(self.__arrQuizQuestions) < MIN_QUESTIONS:   # < operator
            messagebox.showwarning("Not Enough Questions",
                                   f"A quiz needs at least {MIN_QUESTIONS} "
                                   f"questions. Please add more.")
            return

        # Build 2-D array of question/answer pairs
        arrQuizData = [[q, a] for q, a in
                       zip(self.__arrQuizQuestions, self.__arrQuizAnswers)]

        # Write quiz record to CSV (write to data source)
        with open(QUIZZES_FILE_PATH, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([strQuizTitle,
                             page1.current_username,
                             arrQuizData])

        # Reset state
        self.__arrQuizQuestions.clear()
        self.__arrQuizAnswers.clear()
        self._set_placeholder(self.entryQuizTitle, "Quiz Title")
        self.lblCount.config(
            text=f"Questions added: 0  (minimum {MIN_QUESTIONS})")

        messagebox.showinfo("Quiz Saved",
                            f'"{strQuizTitle}" has been saved!')
        show_page2()

    def show(self) -> None:
        """Display the create-quiz page."""
        hide_all()
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

    def hide(self) -> None:
        """Remove all create-quiz widgets from the screen."""
        for w in (self.lblTitle, self.lblCount, self.frmCard,
                  self.entryQuizTitle, self.lblDivider,
                  self.entryQuestion, self.entryAnswer,
                  self.btnNext, self.btnFinish, self.btnExit):
            w.place_forget()


# ══════════════════════════════════════════════════════════════════════
#  PAGE 6 – PLAY MODE SELECTION      playQuizPage(BasePage)
# ══════════════════════════════════════════════════════════════════════

class playQuizPage(BasePage):
    """
    Displayed after the user selects a quiz to play.
    Lets the user choose between Flashcard and Quiz (Kahoot) mode.

    Data:
        arrQuizToPlay – 2-D list of [question, answer] pairs
        strQuizTitle  – text (str) of the selected quiz
    """

    def __init__(self) -> None:
        """Initialise mode-selection widgets."""
        super().__init__()

        # ── Public quiz data (consumed by page7 and page8) ────────
        self.arrQuizToPlay = []   # list[list] – 2-D array [[q, a], ...]
        self.strQuizTitle  = ""   # str – quiz title

        # ── Widgets ───────────────────────────────────────────────
        self.lblQuizName = ttk.Label(
            master=app, text="",
            font=font_title, style='TLabel')
        self.lblSubtitle = ttk.Label(
            master=app, text="Choose how you'd like to study",
            font=small_font, style='Muted.TLabel')

        self.frmPlay = ttk.Frame(
            master=app, style='TFrame', width=520, height=320)

        self.btnFlashCard = ttk.Button(
            master=self.frmPlay, text="🃏   Flashcards",
            command=self.flashCard)
        self.lblFlashDesc = ttk.Label(
            master=self.frmPlay,
            text="Flip through cards at your own pace",
            font=small_font, style='MutedCard.TLabel')

        self.btnKahoot = ttk.Button(
            master=self.frmPlay, text="⚡   Quiz Mode",
            command=self.kahoot)
        self.lblKahootDesc = ttk.Label(
            master=self.frmPlay,
            text="Multiple-choice questions against the clock",
            font=small_font, style='MutedCard.TLabel')

        self.btnCancel = ttk.Button(
            master=self.frmPlay, text="← Back",
            command=self.cancel)

    def getQuizToPlay(self, intQuizIndex: int) -> None:
        """
        Load the quiz at the given index from the main page's 2-D array.

        Record fields accessed by index:
            [0] title   : str
            [1] username: str
            [2] data    : str (string repr of 2-D [[q, a], ...] list)

        Parameters
        ----------
        intQuizIndex : int – index in page2.quizzes
        """
        self.strQuizTitle  = page2.quizzes[intQuizIndex][0]   # text
        strRawData: str    = page2.quizzes[intQuizIndex][2]   # text
        # Convert the stored string back to a Python 2-D list
        self.arrQuizToPlay = eval(strRawData)

    def cancel(self) -> None:
        """Return to the main quiz dashboard."""
        show_page2()

    def flashCard(self) -> None:
        """Navigate to Flashcard mode."""
        show_page7()

    def kahoot(self) -> None:
        """Navigate to Quiz (Kahoot) mode."""
        show_page8()

    def show(self) -> None:
        """Display the mode selection page."""
        hide_all()
        self.lblQuizName.config(text=self.strQuizTitle)
        self.lblQuizName.place(relx=0.5, rely=0.13, anchor="center")
        self.lblSubtitle.place(relx=0.5, rely=0.22, anchor="center")
        self.frmPlay.place(relx=0.5, rely=0.56, anchor="center")
        self.btnFlashCard.place(relx=0.5, rely=0.22, anchor="center",
                                width=360)
        self.lblFlashDesc.place(relx=0.5, rely=0.38, anchor="center")
        self.btnKahoot.place(relx=0.5, rely=0.55, anchor="center",
                             width=360)
        self.lblKahootDesc.place(relx=0.5, rely=0.71, anchor="center")
        self.btnCancel.place(relx=0.5, rely=0.88, anchor="center")

    def hide(self) -> None:
        """Remove all mode-selection widgets from the screen."""
        for w in (self.lblQuizName, self.lblSubtitle, self.frmPlay,
                  self.btnFlashCard, self.lblFlashDesc,
                  self.btnKahoot, self.lblKahootDesc, self.btnCancel):
            w.place_forget()


# ══════════════════════════════════════════════════════════════════════
#  PAGE 7 – FLASHCARD MODE      flashCardPage(BasePage)
# ══════════════════════════════════════════════════════════════════════

class flashCardPage(BasePage):
    """
    Flashcard study mode.

    Displays one card at a time; the user flips it to reveal the answer
    and advances at their own pace.  Cards wrap around when the end is
    reached.

    Data: page6.arrQuizToPlay – 2-D list of [question, answer] pairs.
    """

    def __init__(self) -> None:
        """Initialise flashcard widgets."""
        super().__init__()

        # ── Private state ──────────────────────────────────────────
        self.__intClicks: int = 0   # int – flip-click counter (even = Q, odd = A)
        self.__intN:      int = 0   # int – current card index

        # ── Widgets ───────────────────────────────────────────────
        self.lblQuizTitle = ttk.Label(
            master=app, text="",
            font=font_subtitle, style='TLabel')
        self.lblProgress = ttk.Label(
            master=app, text="",
            font=small_font, style='Muted.TLabel')

        self.crdFlashCard = ttk.Frame(
            master=app, style='TFrame', width=720, height=340)
        self.lblSide = ttk.Label(
            master=self.crdFlashCard, text="QUESTION",
            font=small_bold, style='MutedCard.TLabel')
        self.lblContent = ttk.Label(
            master=self.crdFlashCard, text="",
            font=font_para, style='Card.TLabel', wraplength=660)

        self.btnFlip = ttk.Button(
            master=app, text="Flip Card ↺",
            command=self.flipCard)
        self.btnNext = ttk.Button(
            master=app, text="Next →",
            command=self.nextCard)
        self.btnFinish = ttk.Button(
            master=app, text="Finish",
            command=self.finishQuiz,
            style='Secondary.TButton')

    # ── Private helpers ────────────────────────────────────────────

    def __refreshCard(self) -> None:
        """
        Private – update the progress label and show the question side
        of the current card.
        """
        intTotal: int = len(page6.arrQuizToPlay)   # int – total cards
        # Progress: addition operator used (self.__intN + 1)
        self.lblProgress.config(
            text=f"Card {self.__intN + 1} of {intTotal}")
        self.lblSide.config(text="QUESTION")
        self.lblContent.config(
            text=page6.arrQuizToPlay[self.__intN][0])   # field [0] = question

    # ── Public methods ─────────────────────────────────────────────

    def flipCard(self) -> None:
        """Toggle the card between question (front) and answer (back)."""
        self.__intClicks += 1   # increment

        if self.__intClicks % 2 == 0:   # modulus – even → question side
            self.lblSide.config(text="QUESTION")
            self.lblContent.config(
                text=page6.arrQuizToPlay[self.__intN][0])
        else:                           # odd → answer side
            self.lblSide.config(text="ANSWER")
            self.lblContent.config(
                text=page6.arrQuizToPlay[self.__intN][1])   # field [1]

    def nextCard(self) -> None:
        """Advance to the next card; wrap back to the first when at the end."""
        intTotal: int = len(page6.arrQuizToPlay)
        self.__intN      = (self.__intN + 1) % intTotal   # modulus wrap-around
        self.__intClicks = 0
        self.__refreshCard()

    def finishQuiz(self) -> None:
        """End the flashcard session and return to the main page."""
        self.__intN      = 0
        self.__intClicks = 0
        show_page2()

    def show(self) -> None:
        """Reset state and display the flashcard page."""
        hide_all()
        self.__intN      = 0
        self.__intClicks = 0
        self.lblQuizTitle.config(text=page6.strQuizTitle)
        self.__refreshCard()

        self.lblQuizTitle.place(relx=0.5, rely=0.08, anchor="center")
        self.lblProgress.place(relx=0.5, rely=0.17, anchor="center")
        self.crdFlashCard.place(relx=0.5, rely=0.48, anchor="center")
        self.lblSide.place(relx=0.5, rely=0.16, anchor="center")
        self.lblContent.place(relx=0.5, rely=0.52, anchor="center")
        self.btnFlip.place(relx=0.33, rely=0.83, anchor="center")
        self.btnNext.place(relx=0.67, rely=0.83, anchor="center")
        self.btnFinish.place(relx=0.5, rely=0.95, anchor="center")

    def hide(self) -> None:
        """Remove all flashcard widgets from the screen."""
        for w in (self.lblQuizTitle, self.lblProgress,
                  self.crdFlashCard, self.lblSide, self.lblContent,
                  self.btnFlip, self.btnNext, self.btnFinish):
            w.place_forget()


# ══════════════════════════════════════════════════════════════════════
#  PAGE 8 – KAHOOT / QUIZ MODE      kahootPage(FormPage)
# ══════════════════════════════════════════════════════════════════════

class kahootPage(FormPage):
    """
    Multiple-choice quiz mode.

    For each question, four answer options are shown (one correct,
    three randomly sampled from other quiz answers).  Score is
    accumulated and a results screen is shown at the end.

    Data structures:
        __allAnswers   – 2-D list: for each question, 4 shuffled options
        __allQuestions – 1-D list of question strings
        __ansPositions – 1-D list of ints: correct-answer index per question

    Validation (time-per-question entry):
        • Type check  – input must be a whole number (isdigit)
        • Range check – must be between MIN_TIME_PER_Q and MAX_TIME_PER_Q
    """

    def __init__(self) -> None:
        """Initialise all Kahoot mode widgets."""
        super().__init__()

        # ── Private quiz-state variables ───────────────────────────
        self.__intN:         int = 0   # int     – current question index
        self.__intCorrect:   int = 0   # int     – correct-answer count
        self.__intIncorrect: int = 0   # int     – incorrect-answer count
        self.__allAnswers        = []  # list[list] – 2-D array of 4 options
        self.__allQuestions      = []  # list[str]  – 1-D array of questions
        self.__ansPositions      = []  # list[int]  – 1-D correct-index array

        # ── Settings screen ────────────────────────────────────────
        self.lblKahoot = ttk.Label(
            master=app, text="Quiz Mode",
            font=font_title, style='TLabel')
        self.lblSubtitle = ttk.Label(
            master=app, text="Multiple-choice against the clock",
            font=small_font, style='Muted.TLabel')

        self.frmSettings = ttk.Frame(
            master=app, style='TFrame', width=560, height=340)
        self.lblTimePerQ = ttk.Label(
            master=self.frmSettings, text="Seconds per question:",
            font=font_para, style='Card.TLabel')
        self.entryTimePerQ = ttk.Entry(
            master=self.frmSettings, width=8,
            font=font_para, style='TEntry')
        self.entryTimePerQ.insert(0, str(DEFAULT_TIME_PER_Q))
        self.btnStart = ttk.Button(
            master=self.frmSettings, text="Start Quiz ▶",
            command=self.getAnswers)

        # ── Live question display ──────────────────────────────────
        self.lblQuestion = ttk.Label(
            master=app, text="",
            font=font_subtitle, style='TLabel', wraplength=900)

        # Answer tiles: each is a coloured button with an overlaid label
        # (label carries the answer text; button colour provides visual hit area)
        self.btnAns1 = ttk.Button(master=app, text=" ",
                                   command=self.ans1Selected,
                                   style='Tile.TButton')
        self.lblAns1 = ttk.Label(master=app, text="",
                                  font=font_answer, style='TileText.TLabel',
                                  wraplength=420)

        self.btnAns2 = ttk.Button(master=app, text=" ",
                                   command=self.ans2Selected,
                                   style='Tile.TButton')
        self.lblAns2 = ttk.Label(master=app, text="",
                                  font=font_answer, style='TileText.TLabel',
                                  wraplength=420)

        self.btnAns3 = ttk.Button(master=app, text=" ",
                                   command=self.ans3Selected,
                                   style='Tile.TButton')
        self.lblAns3 = ttk.Label(master=app, text="",
                                  font=font_answer, style='TileText.TLabel',
                                  wraplength=420)

        self.btnAns4 = ttk.Button(master=app, text=" ",
                                   command=self.ans4Selected,
                                   style='Tile.TButton')
        self.lblAns4 = ttk.Label(master=app, text="",
                                  font=font_answer, style='TileText.TLabel',
                                  wraplength=420)

        # ── Results screen ─────────────────────────────────────────
        self.lblResults = ttk.Label(
            master=app, text="Results",
            font=font_title, style='TLabel')

        self.frmResults = ttk.Frame(
            master=app, style='TFrame', width=700, height=440)
        self.lblCorrectHdr   = ttk.Label(
            master=self.frmResults, text="Correct",
            font=small_bold, style='Card.TLabel')
        self.lblCorrect      = ttk.Label(
            master=self.frmResults, text="",
            font=font_huge, style='Success.TLabel')
        self.lblIncorrectHdr = ttk.Label(
            master=self.frmResults, text="Incorrect",
            font=small_bold, style='Card.TLabel')
        self.lblIncorrect    = ttk.Label(
            master=self.frmResults, text="",
            font=font_huge, style='Warning.TLabel')
        self.lblScoreHdr     = ttk.Label(
            master=self.frmResults, text="Score",
            font=small_bold, style='Card.TLabel')
        self.lblPercentage   = ttk.Label(
            master=self.frmResults, text="",
            font=font_subtitle, style='Card.TLabel')
        self.btnDone = ttk.Button(
            master=self.frmResults, text="Back to Quizzes",
            command=self.finishKahoot)

        # Bind placeholder events (inherited from FormPage)
        self.entryTimePerQ.bind(
            '<FocusIn>',
            lambda e: self.on_entry_click(
                e, self.entryTimePerQ, str(DEFAULT_TIME_PER_Q)))
        self.entryTimePerQ.bind(
            '<FocusOut>',
            lambda e: self.on_focusout(
                e, self.entryTimePerQ, str(DEFAULT_TIME_PER_Q)))

    # ── Private helpers ────────────────────────────────────────────

    def __processAnswer(self, strSelected: str) -> None:
        """
        Private – evaluate whether the selected answer is correct and
        advance to the next question.

        Parameters
        ----------
        strSelected : str – the answer text from the clicked label
        """
        # Retrieve the correct answer using the pre-stored position index
        strCorrect: str = self.__allAnswers[self.__intN][
            self.__ansPositions[self.__intN]]

        if strSelected == strCorrect:   # equality comparison
            self.__intCorrect   += 1   # increment
        else:
            self.__intIncorrect += 1   # increment

        self.__intN += 1               # advance to next question
        self.__showQuestion()

    def __showQuestion(self) -> None:
        """
        Private – render the current question and four answer tiles, or
        show the results screen when all questions are exhausted.
        """
        if self.__intN >= len(self.__allQuestions):   # ≥ comparison
            self.__showResults()
            return

        # Update question text
        self.lblQuestion.config(text=self.__allQuestions[self.__intN])

        # Retrieve 4 shuffled options for this question (2-D array access)
        arrOptions = self.__allAnswers[self.__intN]
        self.lblAns1.config(text=arrOptions[0])
        self.lblAns2.config(text=arrOptions[1])
        self.lblAns3.config(text=arrOptions[2])
        self.lblAns4.config(text=arrOptions[3])

        # Place question label at top centre
        self.lblQuestion.place(relx=0.5, rely=0.12, anchor="center")

        # Place four answer tiles in a 2×2 grid
        # Top-left
        self.btnAns1.place(relx=0.26, rely=0.45, anchor="center",
                           width=520, height=175)
        self.lblAns1.place(relx=0.26, rely=0.45, anchor="center")
        # Top-right
        self.btnAns2.place(relx=0.74, rely=0.45, anchor="center",
                           width=520, height=175)
        self.lblAns2.place(relx=0.74, rely=0.45, anchor="center")
        # Bottom-left
        self.btnAns3.place(relx=0.26, rely=0.78, anchor="center",
                           width=520, height=175)
        self.lblAns3.place(relx=0.26, rely=0.78, anchor="center")
        # Bottom-right
        self.btnAns4.place(relx=0.74, rely=0.78, anchor="center",
                           width=520, height=175)
        self.lblAns4.place(relx=0.74, rely=0.78, anchor="center")

    def __showResults(self) -> None:
        """
        Private – calculate the final score and display the results panel.

        The percentage is stored as a floating-point number (float).
        """
        hide_all()

        intTotal:      int   = len(self.__allQuestions)          # int
        # Calculate score as floating-point percentage (float data type)
        fltPercentage: float = (self.__intCorrect / intTotal) * 100.0

        self.lblResults.place(relx=0.5, rely=0.08, anchor="center")
        self.frmResults.place(relx=0.5, rely=0.56, anchor="center")

        self.lblCorrectHdr.place(relx=0.25, rely=0.16, anchor="center")
        self.lblCorrect.config(text=str(self.__intCorrect))
        self.lblCorrect.place(relx=0.25, rely=0.36, anchor="center")

        self.lblIncorrectHdr.place(relx=0.75, rely=0.16, anchor="center")
        self.lblIncorrect.config(text=str(self.__intIncorrect))
        self.lblIncorrect.place(relx=0.75, rely=0.36, anchor="center")

        self.lblScoreHdr.place(relx=0.5, rely=0.62, anchor="center")
        # Round float to 1 decimal place for display
        self.lblPercentage.config(text=f"{round(fltPercentage, 1)}%")
        self.lblPercentage.place(relx=0.5, rely=0.76, anchor="center")

        self.btnDone.place(relx=0.5, rely=0.92, anchor="center")

    # ── Public answer callbacks ────────────────────────────────────

    def ans1Selected(self) -> None:
        """Handle selection of answer tile 1."""
        self.__processAnswer(self.lblAns1.cget('text'))

    def ans2Selected(self) -> None:
        """Handle selection of answer tile 2."""
        self.__processAnswer(self.lblAns2.cget('text'))

    def ans3Selected(self) -> None:
        """Handle selection of answer tile 3."""
        self.__processAnswer(self.lblAns3.cget('text'))

    def ans4Selected(self) -> None:
        """Handle selection of answer tile 4."""
        self.__processAnswer(self.lblAns4.cget('text'))

    def getAnswers(self) -> None:
        """
        Validate settings, build randomised answer sets for every question,
        and launch the quiz.

        Validation:
            • Type check  – seconds input must be a whole number (.isdigit())
            • Range check – seconds must be between MIN_TIME_PER_Q and
                            MAX_TIME_PER_Q (inclusive)
        """
        strTimeInput: str = self.entryTimePerQ.get().strip()

        # ── Type check – must be numeric (integer) ─────────────────
        if not strTimeInput.isdigit():   # logical NOT
            messagebox.showwarning("Invalid Input",
                                   "Seconds per question must be a "
                                   "whole number (e.g. 30).")
            return
        intTimePerQ: int = int(strTimeInput)   # convert text → integer

        # ── Range check – must be within allowed bounds ────────────
        if intTimePerQ < MIN_TIME_PER_Q or intTimePerQ > MAX_TIME_PER_Q:
            messagebox.showwarning("Out of Range",
                                   f"Seconds per question must be between "
                                   f"{MIN_TIME_PER_Q} and {MAX_TIME_PER_Q}.")
            return

        # ── Reset quiz-state counters and arrays ───────────────────
        self.__intN         = 0
        self.__intCorrect   = 0
        self.__intIncorrect = 0
        self.__allAnswers   = []
        self.__allQuestions = []
        self.__ansPositions = []

        arrPossible = []   # 1-D array – distractor pool for current question

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

            self.__allAnswers.append(arrDistractors)     # row in 2-D array
            self.__allQuestions.append(strQuestion)
            self.__ansPositions.append(intAnsPos)
            arrPossible = []   # reset for next iteration

        hide_all()
        self.__showQuestion()

    def finishKahoot(self) -> None:
        """Return to the main quiz dashboard."""
        show_page2()

    def show(self) -> None:
        """Display the Kahoot settings panel."""
        hide_all()
        self.lblKahoot.place(relx=0.5, rely=0.10, anchor="center")
        self.lblSubtitle.place(relx=0.5, rely=0.19, anchor="center")
        self.frmSettings.place(relx=0.5, rely=0.54, anchor="center")
        self.lblTimePerQ.place(relx=0.5, rely=0.28, anchor="center")
        self.entryTimePerQ.place(relx=0.5, rely=0.48, anchor="center")
        self.btnStart.place(relx=0.5, rely=0.72, anchor="center")

    def hide(self) -> None:
        """Remove all Kahoot mode widgets from the screen."""
        for w in (self.lblKahoot, self.lblSubtitle, self.frmSettings,
                  self.lblTimePerQ, self.entryTimePerQ, self.btnStart,
                  self.lblQuestion,
                  self.btnAns1, self.lblAns1,
                  self.btnAns2, self.lblAns2,
                  self.btnAns3, self.lblAns3,
                  self.btnAns4, self.lblAns4,
                  self.lblResults, self.frmResults,
                  self.lblCorrectHdr, self.lblCorrect,
                  self.lblIncorrectHdr, self.lblIncorrect,
                  self.lblScoreHdr, self.lblPercentage,
                  self.btnDone):
            w.place_forget()


# ══════════════════════════════════════════════════════════════════════
#  INSTANTIATE PAGE OBJECTS
# ══════════════════════════════════════════════════════════════════════

page1 = logInPage()       # Login page          – logInPage(FormPage → BasePage)
page2 = mainPage()        # Main dashboard      – mainPage(BasePage)
page3 = newAccPage()      # Sign-Up page        – newAccPage(FormPage → BasePage)
page4 = manageAccPage()   # Manage account      – manageAccPage(BasePage)
page5 = newQuizPage()     # Create quiz         – newQuizPage(FormPage → BasePage)
page6 = playQuizPage()    # Play mode selection – playQuizPage(BasePage)
page7 = flashCardPage()   # Flashcard mode      – flashCardPage(BasePage)
page8 = kahootPage()      # Kahoot/Quiz mode    – kahootPage(FormPage → BasePage)


# ══════════════════════════════════════════════════════════════════════
#  LAUNCH APPLICATION
# ══════════════════════════════════════════════════════════════════════

show_page1()       # Start at the login screen
app.mainloop()     # Enter the Tkinter event loop
