'''
Simple GUI program to calculate the cost of a window quote based on user input.
The program uses the customtkinter library to create a user-friendly interface.
The program calculates the area of the window, applies a cost based on the type of glass selected,
and applies a discount if the user has a valid concession card.
The program also saves the quote details to a CSV file for record-keeping.
'''

from customtkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox 
import csv

# Set up the framework for the application
app = CTk()
app.title("Jimmy's Windows")
app.geometry("500x500")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)

'''
Create the class app which contains all the methods and variables for the program.
It contains the following methods:
    - __init__: Initializes the GUI components and layout.
    - calcWindowArea: Calculates the area of the window based on height and width.
    - calcCost: Calculates the cost of the window based on the area and type of glass.
    - apply_concession_discount: Applies a discount if the user has a valid concession card.
    - save: Saves the quote details to a CSV file.
    - generateQuote: Generates the quote based on user input and displays the result.
'''
class JimmyApp:
    def __init__(self):
        # Define constants
        self.CONCESSION_DISCOUNT = 0.15

        # Fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")
        self.font_para = customtkinter.CTkFont(family="Helvetica", size=15, weight="normal")

        # Title label and placement
        title = customtkinter.CTkLabel(master=app, text="Jimmy's Windows", font=self.font_title)
        title.place(relx=0.3, rely=0.1, anchor=CENTER)

        # Lable for the input fields
        windowHeightLbl = CTkLabel(master=app, text="Please enter \nwindow height (in cm)", font=self.font_para)
        windowHeightLbl.place(relx=0.2, rely=0.2, anchor=CENTER)
        windowWidthLbl = CTkLabel(master=app, text="Please enter \nwindow width (in cm)", font=self.font_para)
        windowWidthLbl.place(relx=0.2, rely=0.3, anchor=CENTER)

        # Inputs fields for the height and width of the window
        self.windowHeightEntry = CTkEntry(master=app, font=(self.font_para))
        self.windowHeightEntry.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.windowWidthEntry = CTkEntry(master=app, font=(self.font_para))
        self.windowWidthEntry.place(relx=0.5, rely=0.3, anchor=CENTER)

        # Glass type label and dropdown
        glassTypeLbl = CTkLabel(master=app, text="Select \nglass type", font=self.font_para)
        glassTypeLbl.place(relx=0.2, rely=0.4, anchor=CENTER)
        self.glassTypeDropdown = CTkOptionMenu(master=app, values=["Clear", "Frosted", "Tinted"])
        self.glassTypeDropdown.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Concession card label and radio buttons
        self.radioVar = IntVar()
        concessionCardLbl = CTkLabel(master=app, text="Valid concession card?", font=self.font_para)
        concessionCardLbl.place(relx=0.2, rely=0.5, anchor=CENTER)
        yesRadio = CTkRadioButton(master=app, text="Yes", variable=self.radioVar, value=1)
        yesRadio.place(relx=0.5, rely=0.5, anchor=CENTER)
        noRadio = CTkRadioButton(master=app, text="No", variable=self.radioVar, value=0)
        noRadio.place(relx=0.625, rely=0.5, anchor=CENTER)

        # Button to generate the quote
        genQuoteButton = CTkButton(master=app, text="Generate Quote*", command=self.generateQuote)
        genQuoteButton.place(relx=0.2, rely=0.7, anchor=CENTER)

        # Terms and conditions label to inform the user about the $100 call out fee
        tandCLbl = CTkLabel(master=app, text="*Please note that a $100 call out fee is applied to all quotes.", font=(self.font_para))
        tandCLbl.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        # Result label to display the total cost
        self.resultLbl = CTkLabel(master=app, text="Total cost: $0", font=self.font_para)
        self.resultLbl.place(relx=0.6, rely=0.7, anchor=CENTER)

    def calcWindowArea(self, height, width):
        return width * height
    
    def calcCost(self, area, glassType):
        basePrices = {
            "clear": 126.60,
            "tinted": 140.50,
            "frosted": 150.40
        }

        costPer30cm = basePrices[glassType]

        cost = (area / 30) * costPer30cm

        return cost
    
    def apply_concession_discount(self, concessionDiscount, cost, has_concession):
        if has_concession == 1:
            cost = cost * (1 - concessionDiscount)
        elif has_concession == 0:
            cost = cost
         
        return cost
    
    def save(self, width, height, glassType, has_concession, quote_price):
        # Column names for the CSV file
        field_names = ['width', 'height', 'glassType', 'has_concession', 'quote_price']

        # Data to be saved in the CSV file
        dict = {'width': width, 'height': height, 'glassType': glassType, 'has_concession':has_concession, 'quote_price': quote_price}

        # Open the CSV file in append mode and write the data
        with open('appliedComputing/sac/quotes.csv', 'a', newline='') as f_objects:
            dictWriter_object = csv.DictWriter(f_objects, fieldnames=field_names)

            dictWriter_object.writerow(dict)
            f_objects.close()

        
    def generateQuote(self):
        height = float(self.windowHeightEntry.get())
        width = float(self.windowWidthEntry.get())
        glassType = self.glassTypeDropdown.get().lower()
        has_concession = self.radioVar.get()

        area = self.calcWindowArea(height, width)

        cost = self.calcCost(area, glassType)
        cost = self.apply_concession_discount(self.CONCESSION_DISCOUNT, cost, has_concession)
        cost = round(cost + 100, 2)

        self.resultLbl.forget()
        self.resultLbl = CTkLabel(master=app, text=f"Total cost: ${cost}", font=self.font_para)
        self.resultLbl.place(relx=0.6, rely=0.7, anchor=CENTER)

        self.save(width, height, glassType, has_concession, cost)

        msg = CTkMessagebox(title="Saved", message="Quote saved to quotes.csv", icon="check")

        


JimmyApp()

app.mainloop()