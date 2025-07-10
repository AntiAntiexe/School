from customtkinter import *
import customtkinter

app = CTk()
app.title('Choose Ice Cream')
app.geometry("500x500")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)


class IceCream:
    def __init__(self):

        # Fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")

        self.font_para = customtkinter.CTkFont(family="Helvetica", size=25, weight="normal", )

        title = customtkinter.CTkLabel(master=app, text='Ice Cream Picker', font=self.font_title)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        subHead1 = customtkinter.CTkLabel(master=app, text='Choose your flavor:', font=self.font_para)
        subHead1.place(relx=0.1, rely=0.2, anchor=W)

        vanilla = customtkinter.CTkCheckBox(master=app, text="Vanilla", onvalue="on", offvalue="off")
        chocolate = customtkinter.CTkCheckBox(master=app, text="Chocolate", onvalue="on", offvalue="off")
        strawberry = customtkinter.CTkCheckBox(master=app, text="Strawberry", onvalue="on", offvalue="off")
        mango = customtkinter.CTkCheckBox(master=app, text="Mango", onvalue="on", offvalue="off")

        vanilla.place(relx=0.1, rely=0.3, anchor=W)
        chocolate.place(relx=0.1, rely=0.35, anchor=W)
        strawberry.place(relx=0.1, rely=0.4, anchor=W)
        mango.place(relx=0.1, rely=0.45, anchor=W)

        subHead2 = customtkinter.CTkLabel(master=app, text='Choose your cone:', font=self.font_para)
        subHead2.place(relx=0.1, rely=0.55, anchor=W)
        
        self.waff = IntVar()
        self.sugar = IntVar()
        waffle = customtkinter.CTkRadioButton(master=app, text="Waffle Cone", variable=self.waff, value=1)
        sugar = customtkinter.CTkRadioButton(master=app, text="Sugar Cone", variable=self.sugar, value=1)

        combobox = customtkinter.CTkComboBox(master=app,
                                     values=["Waffle Cone", "Sugar Cone"])

        combobox.set("Waffle Cone")
        combobox.place(relx=0.1, rely=0.625, anchor=W)

        app.mainloop()

IceCream()

        