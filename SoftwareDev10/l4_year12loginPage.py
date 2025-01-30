from customtkinter import *
import customtkinter
import pandas as pd

def hide_all():
    """ Hides all the pages """
    logInPage.hide()
    page2.hide()


def show_page1():
    logInPage.show()


def show_page2():
    mainPage.show()
    
class logInPage:

    def __init__(self):
        super().__init__()

        self.app = CTk()
        self.app.title('Money Calculator')
        self.app.geometry("500x500")
        set_appearance_mode("dark")
        self.app.grid_columnconfigure(0, weight=1)

        # Fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")

        self.font_para = customtkinter.CTkFont(family="Helvetica", size=25, weight="normal", )

        # Title
        self.label = CTkLabel(master=self.app, text="Login Screen!", font=self.font_title)
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.entry = CTkEntry(master=self.app, placeholder_text="Username", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 20))
        self.entry.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.entry = CTkEntry(master=self.app, placeholder_text="Username", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 20))
        self.entry.place(relx=0.5, rely=0.3, anchor=CENTER)
        
        self.button = CTkButton(master=self.app, text="Submit", command=show_page2, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40, width=185,
                                   font=(self.font_para, 20))
        self.button.place(relx=0.5, rely=0.4, anchor=CENTER)

        
        

        self.app.mainloop()

    def submit(self):
        grade = int(self.entry.get())
        result = self.gradeCheck(grade)

        self.result.configure(text=str(result))
        
class mainPage:
    def __init__(self):
        self.back =   CTkButton(master=self.app, text="Submit", command=show_page1, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40, width=185,
                                   font=(self.font_para, 20))
        self.back.place(relx=0.5, rely=0.4, anchor=CENTER)


logInPage()