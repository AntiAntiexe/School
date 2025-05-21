from customtkinter import *
import customtkinter

app = CTk()
app.title('Choose Ice Cream')
app.geometry("500x500")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)


class IceCream:
    def __init__(self):
        self.entry = CTkEntry(master=app, placeholder_text="i value")
        self.entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.lbl = CTkLabel(master=app, text="i")

        self.submit_button = CTkButton(master=app, text="Submit", command=self.submit)
        self.submit_button.place(relx=0.5, rely=0.6, anchor=CENTER) 
    def submit(self):
        i = int(self.entry.get())
        while i<9:
            print(i)
            i += 1
        self.lbl.configure(text=i)
        self.lbl.place(relx=0.5, rely=0.7, anchor=CENTER)

IceCream()
app.mainloop()
        
