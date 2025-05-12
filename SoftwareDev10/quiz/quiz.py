from customtkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
import pandas as pd


app = CTk()
app.title('Math Quiz!')
app.geometry("500x700")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)

class quiz:
    def __init__(self):

        # Fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")

        self.font_para = customtkinter.CTkFont(family="Helvetica", size=15, weight="normal", )

        self.intro = CTkLabel(master=app, text='Enter your details', font=self.font_title)
        self.intro.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.studentID = CTkEntry(master=app, placeholder_text="Student ID", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 20))
        self.studentID.place(relx=0.1, rely=0.15)

        self.name = CTkEntry(master=app, placeholder_text="Name", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 20))
        self.name.place(relx=0.1, rely=0.25)

        self.title = CTkLabel(master=app, text='Math Quiz!', font=self.font_title)

        self.title.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.q1 = CTkLabel(master=app, text="Q1: Solve 3x - 7 = 11:", font=self.font_para)
        self.q1Ans = customtkinter.CTkComboBox(master=app, values=["4/3", "11/3", "-3/4", "6", "-6"])

        self.q1.place(relx=0.1, rely=0.5, anchor=W)
        self.q1Ans.place(relx=0.1, rely=0.55, anchor=W)

        self.q2 = CTkLabel(master=app, text="Q2: If x/3 +1/3 = 2 then x =:", font=self.font_para)
        self.q2Ans = customtkinter.CTkComboBox(master=app, values=["1/3", "2/3", "7/3", "5", "7"])

        self.q2.place(relx=0.1, rely=0.625, anchor=W)
        self.q2Ans.place(relx=0.1, rely=0.675, anchor=W)

        self.q3 = CTkLabel(master=app, text="Q3: The solution of the equation x - 8 = 3x - 16 is", font=self.font_para)
        self.q3Ans = customtkinter.CTkComboBox(master=app, values=["-8/3", "11/3", "4", "2", "-2"])

        self.q3.place(relx=0.1, rely=0.75, anchor=W)
        self.q3Ans.place(relx=0.1, rely=0.8, anchor=W)

        self.button = CTkButton(master=app, text="Submit", command=self.submit, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=20, width=100,
                                   font=(self.font_para, 20))
        
        self.button.place(relx=0.1, rely=0.9, anchor=W)

    def submit(self):
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

        results.loc[len(results)] = [self.name.get(), self.studentID.get(), right]
        results.to_csv('SoftwareDev10/quiz/results.csv', index=True)


            

        msg = CTkMessagebox(title="Result", message="You got " + str(right) +"/3",
                        icon="info")
        
        






        


quiz()

app.mainloop()