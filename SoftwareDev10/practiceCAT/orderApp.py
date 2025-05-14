from customtkinter import *
import customtkinter

app = CTk()
app.title("Frank's Food")
app.geometry("500x500")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)


class FranksFoodApp:
    def __init__(self):

        SENIOR_CITIZEN_DISCOUNT = 10

        # fonts
        self.font_title = customtkinter.CTkFont(
            family="Helvetica", size=25, weight="bold"
        )

        self.font_para = customtkinter.CTkFont(
            family="Helvetica",
            size=15,
            weight="normal",
        )

        self.title = CTkLabel(master=app, text="Frank's Food", font=self.font_title)
        self.title.place(relx=0.1, rely=0.1, anchor=W)

        self.nameLbl = CTkLabel(master=app, text="Enter Name", font=self.font_para)
        self.nameLbl.place(relx=0.1, rely=0.2, anchor=W)

        self.nameEntry = CTkEntry(master=app, placeholder_text="Name", width=185, height=30,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 15))
        self.nameEntry.place(relx=0.1, rely=0.265, anchor=W)

        self.orderValueLbl = CTkLabel(master=app, text="Order Value", font=self.font_para)
        self.orderValueLbl.place(relx=0.1, rely=0.35, anchor=W)

        self.orderValueEntry = CTkEntry(master=app, placeholder_text="Order Value", width=185, height=30,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 15))
        self.orderValueEntry.place(relx=0.1, rely=0.415, anchor=W)

        self.seniorCitLbl = CTkLabel(master=app, text="Senior Citizen?", font=self.font_para)
        self.seniorCitLbl.place(relx=0.1, rely=0.5, anchor=W)

        self.radio_var = IntVar()
        self.yesRadio = CTkRadioButton(
            master=app, text="Yes", variable=self.radio_var, value=1
        )
        self.yesRadio.place(relx=0.2, rely=0.55, anchor=CENTER)
        self.noRadio = CTkRadioButton(
            master=app, text="No", variable=self.radio_var, value=2
        )
        self.noRadio.place(relx=0.4, rely=0.55, anchor=CENTER)

        self.submit = CTkButton(
            master=app,
            text="Submit",
            command=self.submit,
            fg_color="#0fa4af",
            border_color="#0d737a",
            border_width=2,
            hover_color="#024950",
            text_color="#323231",
            height=20,
            width=100,
            font=(self.font_para, 15),
        )
        self.submit.place(relx=0.1, rely=0.7, anchor=W)

        self.resultLbl = CTkLabel(master=app, text="Total Cost:", font=self.font_para)
    def calcDiscount(self, orderValue):
        if orderValue > 100 and orderValue < 150:
            orderDiscount = 10
            totalOrderValue = orderValue * (1 - orderDiscount / 100) 
            
    def submit(self):
        pass








        




FranksFoodApp()

app.mainloop()