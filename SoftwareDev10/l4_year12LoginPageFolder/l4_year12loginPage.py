from customtkinter import *
import customtkinter
import pandas as pd

app = CTk()
app.title('My App')
app.geometry("500x500")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)

def hide_all():
    """ Hides all the pages """
    page1.hide()
    page2.hide()


def show_page1():
    page1.show()


def show_page2():
    page2.show()
    
class logInPage:

    def __init__(self):
        super().__init__()

        

        # Fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")

        self.font_para = customtkinter.CTkFont(family="Helvetica", size=25, weight="normal", )

        # Title
        self.label = CTkLabel(master=app, text="Login Screen!", font=self.font_title)
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.username = CTkEntry(master=app, placeholder_text="Username", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 20))
        
        self.password = CTkEntry(master=app, placeholder_text="Password", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 20))
        
        
        self.button = CTkButton(master=app, text="Submit", command=show_page2, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40, width=185,
                                   font=(self.font_para, 20))
          
    def show(self):
        hide_all()
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.username.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.password.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.4, anchor=CENTER)

    def hide(self):
        self.label.place_forget()
        self.username.place_forget()
        self.password.place_forget()
        self.button.place_forget()

    def submit(self):
        grade = int(self.username.get())
        result = self.gradeCheck(grade)

        self.result.configure(text=str(result))
        
class mainPage:
    def __init__(self):
        self.back =   CTkButton(master=app, text="back", command=show_page1, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40, width=185)
        
    def show(self):
        hide_all()
        self.back.place(relx=0.5, rely=0.4, anchor=CENTER)
        

    def hide(self):
        self.back.place_forget()



page1 = logInPage()

page2 = mainPage()


show_page1()


app.mainloop()