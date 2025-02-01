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
        

        self.check = CTkLabel(master=app, text="Incorrect username or password!", font=(self.font_para, 20))
        

        self.username = CTkEntry(master=app, placeholder_text="Username", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 20))
        
        self.password = CTkEntry(master=app, placeholder_text="Password", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 20))
        
        
        self.button = CTkButton(master=app, text="Submit", command=self.submit, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=20, width=100,
                                   font=(self.font_para, 20))
        
        self.newAccBut = CTkButton(master=app, text="Create new account", command=self.createNewAcc, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=10, width=50,
                                   font=(self.font_para, 20))
          
    def show(self):
        hide_all()
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.username.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.password.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.newAccBut.place(relx=0.8, rely=0.95, anchor=CENTER)
        

    def hide(self):
        self.label.place_forget()
        self.username.place_forget()
        self.password.place_forget()
        self.button.place_forget()
        self.check.place_forget()
        self.newAccBut.place_forget()

    def createNewAcc(self):
        pass

    def submit(self):
        df = pd.read_csv('SoftwareDev10/l4_year12LoginPageFolder/accounts.csv')
        user = self.username.get()
        password = self.password.get()

        data = df[df['username']== user].astype(str)
        print(password, type(password))
        print(data['password'].tolist())

        print('\n ------------\n')
        print(df['username'].tolist())

        if user in df['username'].tolist() and password in data['password'].tolist():
            print(f'hello {user}.')
            show_page2()
        else:
            self.check.place(relx=0.5, rely=0.5, anchor=CENTER)
            print('Incorrect username or password.')


        print(df[df['username']== user])

        
        
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