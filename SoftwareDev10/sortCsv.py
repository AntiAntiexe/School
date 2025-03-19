import customtkinter
from customtkinter import *
import pandas as pd
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from customtkinter import  CTk, CTkButton 


class App:

    def __init__(self) -> None:
        super().__init__()

        self.app = CTk()
        self.app.title('Sort CSV')
        self.app.geometry('800x800')

        set_appearance_mode("dark")

        self.my_font = customtkinter.CTkFont(family="sans serif", size=75, weight="bold", )

        self.my_font2 = customtkinter.CTkFont(family="sans serif", size=25, weight="normal", )

        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(0, weight=0)
        

        self.label = CTkLabel(master=self.app, text="CSV Sorter", font=self.my_font)
        self.label.grid(column=0, row=0, padx=20, pady=20)

        self.btn_submit = CTkButton(master=self.app, text="Submit", command=self.select_file, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40,
                                   font=(self.my_font2, 25))
        self.btn_submit.grid(column=0, row=1, padx=20, pady=20)

        self.textbox = customtkinter.CTkTextbox(master=self.app, width=400, corner_radius=0)
        self.textbox.grid(row=2, column=0, padx=20, pady=20)
        self.textbox.insert("0.0", "Some example text!\n" * 50)

        


        self.app.mainloop()

    def filedialog(self):
        file = filedialog.askdirectory()

        print(file)
    
    
    
    def sort(self):
        df = pd.read_csv(self.filename)

        sorted_df = df.sort_values(by=["number"], ascending=True)
        sorted_df.to_csv('homes_sorted.csv', index=False)

        self.textbox.insert("0.0", sorted_df)
        print(sorted_df)
    
    def select_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=self.filename
        )

        self.sort()

        print(self.filename)


App()
