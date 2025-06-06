import customtkinter
from customtkinter import customtkinter

from customtkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox 
import csv

# Set up the framework for the application
app = CTk()
app.title("NUMBER GUESSING GAME")
app.geometry("500x500")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)

def hide_all():
    """ Hides all the pages """
    page1.hide()
    page2.hide()
    page3.hide()
    page4.hide()


def show_page1():
    page1.show()


def show_page2():
    page2.show()

def show_page3():
    page3.show()

def show_page4():
    page4.show()

class Page1:
    def __init__(self):
        # fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")
        self.font_para = customtkinter.CTkFont(family="Helvetica", size=15, weight="normal")

        self.

class Page2:
    def __init__(self):
        # fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")
        self.font_para = customtkinter.CTkFont(family="Helvetica", size=15, weight="normal")

        self.title = customtkinter.CTkLabel(master=app, text='Page 2', font=self.font_title)
        self.title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.label = customtkinter.CTkLabel(master=app, text='This is Page 2', font=self.font_para)
        self.label.place(relx=0.5, rely=0.3, anchor=CENTER)

page1 = Page1()
page2 = Page2()
