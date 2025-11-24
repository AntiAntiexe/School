from customtkinter import *
import customtkinter
import csv

app = CTk()
app.title("Password")
app.geometry("800x400")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)


class CoffeeApp:
    def __init__(self):

        # fonts
        self.font_title = customtkinter.CTkFont(
            family="Helvetica", size=25, weight="bold"
        )

        self.font_para = customtkinter.CTkFont(
            family="Helvetica",
            size=15,
            weight="normal",
        )

        # Define the prices for each coffee size
        self.SMALL_PRICE = 4.80
        self.MEDIUM_PRICE = 5.50
        self.LARGE_PRICE = 6.50
        # Define the discount rate for concession card holders
        self.CONCESSION_DISCOUNT_RATE = 0.25
        # Define the discount for every 4 coffees
        self.COFFEE_DISCOUNT = 3.0
        # Define the file name for sales data
        self.SALES_FILE_NAME = "sales.txt"
        # Complete this function (10 marks)

        # Title
        self.title = CTkLabel(master=app, text="Coffee App", font=self.font_title)
        self.title.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Small coffee label and combo box
        self.smallLbl = CTkLabel(master=app, text="Small Coffee", font=self.font_para)
        self.smallLbl.place(relx=0.2, rely=0.2, anchor=CENTER)
        self.smallCombo = CTkComboBox(
            master=app, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.smallCombo.place(relx=0.4, rely=0.2, anchor=CENTER)

        # Medium coffee label and combo box
        self.mediumLbl = CTkLabel(master=app, text="Medium Coffee", font=self.font_para)
        self.mediumLbl.place(relx=0.2, rely=0.3, anchor=CENTER)
        self.mediumCombo = CTkComboBox(
            master=app, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.mediumCombo.place(relx=0.4, rely=0.3, anchor=CENTER)

        # Large coffee lebel and combo box
        self.largeLbl = CTkLabel(master=app, text="Large Coffee", font=self.font_para)
        self.largeLbl.place(relx=0.2, rely=0.4, anchor=CENTER)
        self.largeCombo = CTkComboBox(
            master=app, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        )
        self.largeCombo.place(relx=0.4, rely=0.4, anchor=CENTER)

        # Concession lebel and radio buttons
        self.radio_var = IntVar()
        self.concLbl = CTkLabel(master=app, text="Concession", font=self.font_para)
        self.concLbl.place(relx=0.8, rely=0.2, anchor=CENTER)
        self.yesRadio = CTkRadioButton(
            master=app, text="Yes", variable=self.radio_var, value=1
        )
        self.yesRadio.place(relx=0.775, rely=0.3, anchor=CENTER)
        self.noRadio = CTkRadioButton(
            master=app, text="No", variable=self.radio_var, value=2
        )
        self.noRadio.place(relx=0.875, rely=0.3, anchor=CENTER)

        # Submit
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
            font=(self.font_para, 20),
        )
        self.submit.place(relx=0.8, rely=0.8, anchor=CENTER)

        # Total cost label and result
        self.totalCostLbl = CTkLabel(master=app, text="Total Cost", font=self.font_para)
        self.totalCostLbl.place(relx=0.2, rely=0.8, anchor=CENTER)

        self.resultLbl = CTkLabel(master=app, text="Total Cost", font=self.font_para)

    def apply_concession_discount(self, total_cost):
        has_concession_card = StringVar()
        if self.radio_var.get() == 1:
            has_concession_card = "yes"
        elif self.radio_var.get() == 2:
            has_concession_card = "no"

        if has_concession_card == "yes":
            total_cost = total_cost * (1 - self.CONCESSION_DISCOUNT_RATE)
        elif has_concession_card == "no":
            total_cost = total_cost

        return total_cost, has_concession_card

    def get_order(self):
        num_coffees = (
            int(self.smallCombo.get())
            + int(self.mediumCombo.get())
            + int(self.largeCombo.get())
        )

        small_price = int(self.smallCombo.get()) * self.SMALL_PRICE
        medium_price = int(self.mediumCombo.get()) * self.MEDIUM_PRICE
        large_price = int(self.largeCombo.get()) * self.LARGE_PRICE

        total_cost = small_price + medium_price + large_price

        return total_cost, num_coffees

    def apply_coffee_discount(self, total_cost, num_coffees):
        if num_coffees % 4 == 0:
            num_discounts = num_coffees // 4
            total_cost -= num_discounts * self.COFFEE_DISCOUNT

        return total_cost

    def submit(self):
        total_cost, num_coffees = self.get_order()

        total_cost, has_concession_card = self.apply_concession_discount(total_cost)

        total_cost = self.apply_coffee_discount(total_cost, num_coffees)

        self.resultLbl.configure(text=f"${total_cost:.2f}")
        self.resultLbl.place(relx=0.4, rely=0.8, anchor=CENTER)


CoffeeApp()

app.mainloop()
