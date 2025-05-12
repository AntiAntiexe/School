from customtkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
import pandas as pd


app = CTk()
app.title('Math Quiz!')
app.geometry("500x500")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)

def hide_all():
    """Hide all widgets in the app."""
    page1.hide()
    page2.hide() 

def show_page1():
    """Show the first page of the app."""
    page1.show()

def show_page2():
    """Show the second page of the app."""
    page2.show()

class LogInPage:
    def __init__(self):
        super().__init__()

        # Fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")
        self.font_para = customtkinter.CTkFont(family="Helvetica", size=15, weight="normal")

        self.intro = CTkLabel(master=app, text='Enter your details', font=self.font_title)

        self.studentID = CTkEntry(master=app, placeholder_text="Student ID", width=185, height=40, fg_color='#0fa4af',
                                  border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                                  font=(self.font_para, 20))
        
        self.name = CTkEntry(master=app, placeholder_text="Name", width=185, height=40, fg_color='#0fa4af',
                                  border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                                  font=(self.font_para, 20))
        
        self.submit_button = CTkButton(master=app, text="Submit", command=self.submit, fg_color="#0fa4af",
                                  border_color='#0d737a',
                                  border_width=2, hover_color='#024950', text_color="#323231", height=20, width=100,
                                  font=(self.font_para, 20))
    def show(self):
        """Show the login page."""
        hide_all()
        self.intro.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.studentID.place(relx=0.1, rely=0.15)
        self.name.place(relx=0.1, rely=0.25)
        self.submit_button.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    def hide(self):
        """Hide the login page."""
        self.intro.place_forget()
        self.studentID.place_forget()
        self.name.place_forget()
        self.submit_button.place_forget()
    
    def submit(self):
        """Handle the submit button click."""
        self.studentID_value = self.studentID.get()
        self.name_value = self.name.get()
        if self.studentID_value and self.name_value:
            msg = CTkMessagebox(title="Result", message="Details submitted successfully!",
                        icon="info")
            self.hide()
            page2.show()
        else:
            msg = CTkMessagebox(title="Error", message="Please fill in all fields", icon="error")

class QuizPage:
    def __init__(self):
        super().__init__()

        # Fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")
        self.font_para = customtkinter.CTkFont(family="Helvetica", size=15, weight="normal")

        self.title = CTkLabel(master=app, text='Math Quiz!', font=self.font_title)
        self.q1 = CTkLabel(master=app, text="Q1: Solve 3x - 7 = 11:", font=self.font_para)
        self.q1Ans = customtkinter.CTkComboBox(master=app, values=["4/3", "11/3", "-3/4", "6", "-6"])

        self.q2 = CTkLabel(master=app, text="Q2: If x/3 +1/3 = 2 then x =:", font=self.font_para)
        self.q2Ans = customtkinter.CTkComboBox(master=app, values=["1/3", "2/3", "7/3", "5", "7"])

        self.q3 = CTkLabel(master=app, text="Q3: The solution of the equation x - 8 = 3x - 16 is", font=self.font_para)
        self.q3Ans = customtkinter.CTkComboBox(master=app, values=["-8/3", "11/3", "4", "2", "-2"])

        self.submit_button = CTkButton(master=app, text="Submit", command=self.submit, fg_color="#0fa4af",
                                  border_color='#0d737a',
                                  border_width=2, hover_color='#024950', text_color="#323231", height=20, width=100,
                                  font=(self.font_para, 20))

    def show(self):
        """Show the quiz page."""
        hide_all()
        self.title.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.q1.place(relx=0.1, rely=0.2, anchor=W)
        self.q1Ans.place(relx=0.1, rely=0.25, anchor=W)
        
        self.q2.place(relx=0.1, rely=0.325, anchor=W)
        self.q2Ans.place(relx=0.1, rely=0.375, anchor=W)
        self.q3.place(relx=0.1, rely=0.45, anchor=W)
        self.q3Ans.place(relx=0.1, rely=0.5, anchor=W)
        self.submit_button.place(relx=0.1, rely=0.6, anchor=W)

        
    
    def hide(self):
        """Hide the quiz page."""
        self.title.place_forget()
        self.q1.place_forget()
        self.q1Ans.place_forget()
        self.q2.place_forget()
        self.q2Ans.place_forget()
        self.q3.place_forget()
        self.q3Ans.place_forget()
        self.submit_button.place_forget()
    
    def submit(self):
        """Handle the submit button click."""
        results = pd.read_csv('SoftwareDev10/quiz/results.csv')
         
        right = 0
        if self.q1Ans.get() == "6":
            quest1 = True
            right = right + 1
            
        else:
            quest1 = False
            
        if self.q2Ans.get() == "5":
            quest2 = True
            right = right + 1
        else:
            quest2 = False
            
        if self.q3Ans.get() == "4":
            quest3 = True
            right = right + 1
        else:
            quest3 = False

        results.loc[len(results)] = [page1.name.get(), page1.studentID.get(), right]
        results.to_csv('SoftwareDev10/quiz/results.csv', index=True)

        
            

        msg = CTkMessagebox(title="Result", message="You got " + str(right) +"/3",
                        icon="info")
        
        self.hide()
        show_page1()



page1 = LogInPage()
page2 = QuizPage()

show_page1()

app.mainloop()


    