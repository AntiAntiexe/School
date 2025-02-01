from customtkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
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
    page3.hide()


def show_page1():
    page1.show()


def show_page2():
    page2.show()

def show_page3():
    page3.show()

class logInPage:

    def __init__(self):
        super().__init__()
        self.df = pd.read_csv('SoftwareDev10/l4_year12LoginPageFolder/accounts.csv')

        

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
        
        self.newAccBut = CTkButton(master=app, text="Create new account", command=self.goToNewAcc, fg_color="#0fa4af",
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

    def goToNewAcc(self):
        show_page3()
        

    def submit(self):
        
        self.user = self.username.get()
        self.password = self.passwordEntry.get()

        data = self.df[self.df['username']== self.user].astype(str)
        print(self.password, type(self.password))
        print(data['password'].tolist())

        print('\n ------------\n')
        print(self.df['username'].tolist())

        if self.user in self.df['username'].tolist() and self.password in data['password'].tolist():
            print(f'hello {self.user}.')
            show_page2()
        else:
            self.check.place(relx=0.5, rely=0.5, anchor=CENTER)
            print('Incorrect username or password.')


        print(self.df[self.df['username']== self.user])
 
class mainPage:
    def __init__(self):
        self.back =   CTkButton(master=app, text="back", command=show_page1, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40, width=185,
                                   font=(page1.font_para, 20))
        
        self.manageAccBut = CTkButton(master=app, text="Manage Account", command=self.managePage, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=10, width=50,
                                   font=(page1.font_para, 20))
    def managePage(self):
        page4.show()
        
    def show(self):
        hide_all()
        self.back.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.manageAccBut.place(relx=0.8, rely=0.95, anchor=CENTER)
        

    def hide(self):
        self.back.place_forget()
        self.manageAccBut.place_forget()

class manageAccPage:
    def __init__(self):
        self.delete =   CTkButton(master=app, text="Delete Account", command=self.deleteAcc, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40, width=185,
                                   font=(page1.font_para, 20))
        
        self.done = CTkButton(master=app, text="Done", command=show_page2, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=10, width=50,
                                   font=(page1.font_para, 20))
    def deleteAcc(self):
        msg = CTkMessagebox(title="Delete", message="Are you sure you want to delete your account? This action is not reversable.",
                        icon="warning", option_1="No", option_2="Yes")
        response = msg.get()
    
        if response=="Yes":
            page1.df = page1.df[page1.df.username != page1.user]
            page1.df.to_csv('SoftwareDev10/l4_year12LoginPageFolder/accounts.csv', index=False)
            print(page1.df)

            show_page1()

        else:
            print("Click 'Yes' to exit!")
        
        
    def show(self):
        hide_all()
        self.delete.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.done.place(relx=0.8, rely=0.95, anchor=CENTER)
        

    def hide(self):
        self.delete.place_forget()
        self.done.place_forget()

class newAccPage:
    def __init__(self):
        self.newAccLabel = CTkLabel(master=app, text="Create a New Account", font=page1.font_title)
        

        self.checkNewAcc = CTkLabel(master=app, text="Incorrect username or password!", font=(page1.font_para, 20))
        

        self.newUsername = CTkEntry(master=app, placeholder_text="Username", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(page1.font_para, 20))
        
        self.newPassword = CTkEntry(master=app, placeholder_text="Password", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(page1.font_para, 20))
        
        self.done = CTkButton(master=app, text="Submit", command=self.createNewAcc, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40, width=185)
    
    def createNewAcc(self):
        newUser = self.newUsername.get()
        newPass = self.newPassword.get()

        if newUser in page1.df['username'].tolist():
            print('Username not available')
            self.checkNewAcc.configure(text='Username not available')
            self.checkNewAcc.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            if newPass.isascii():
                if len(newPass) >= 8:
                    page1.df.loc[len(page1.df)] = [newUser, newPass]  
                    page1.show()
                    page1.df.to_csv('SoftwareDev10/l4_year12LoginPageFolder/accounts.csv', index=True)
                    print('New account created')
                    print(page1.df)
                else:
                    self.checkNewAcc.configure(text='Password must contain at least 8 characters')
                    self.checkNewAcc.place(relx=0.5, rely=0.5, anchor=CENTER)

            else:
                self.checkNewAcc.configure(text='Please enter a password')
                self.checkNewAcc.place(relx=0.5, rely=0.5, anchor=CENTER)

                     
    def show(self):
        hide_all()
        self.newAccLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.newUsername.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.newPassword.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.done.place(relx=0.5, rely=0.4, anchor=CENTER)
        

    def hide(self):
        self.newAccLabel.place_forget()
        self.newUsername.place_forget()
        self.newPassword.place_forget()
        self.checkNewAcc.place_forget()
        self.done.place_forget()



page1 = logInPage()

page2 = mainPage()

page3 = newAccPage()

page4 = manageAccPage()


show_page1()


app.mainloop()
