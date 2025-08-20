import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from usdaFood import NutrientData
import numpy as np
from runMainModel import FruitClassifier
from PIL import ImageTk, Image


'''
The App class initialises the variables required for the tkinter GUI.
This includes methods and objects for:
    colours
    UI elements
    fruit classifier
'''
class App:
    def __init__(self, root):


        self.root = root

        self.colours = {
            'bg_dark': '#00060A',
            'bg': '#000E14',
            'bg_light': '#05181F',
            'text': '#D6F3FF',
            'text_muted': '#88BACD',
            'highlight': '#3B6B7D',
            'border': '#1C4E5E',
            'border_muted': '#00303D',
            'primary': '#61BEE0',
            'secondary': '#E79D7E',
            'danger': '#C1928A',
            'warning': '#A7A176',
            'success': '#7DAA92',
            'info': '#879FC4',
        }

        self.root.title("NutriVision")
        self.root.geometry("800x600")
        self.root.configure(bg=self.colours['bg_dark'])
  
        self.fruitClassifier = FruitClassifier()

        style = ttk.Style(self.root)
        style.theme_use('classic')
        
        s = ttk.Style()
        s.configure('Danger.TFrame', background=self.colours['border'], borderwidth=5)
        
        frame = ttk.Frame(self.root, height=400, width=400, style='Danger.TFrame')
        frame.place(x=550, y=350, anchor='center')

        font_main = ('Manrope', 100, 'bold')
        label = ttk.Label(self.root, text='NutriVision', font=font_main, foreground=self.colours['text'], background=self.colours['bg_dark'])
        label.place(x=10, y=50, anchor='w')
        font_main = ('Manrope', 20, 'bold')
        selectFileButton = tk.Button(self.root, text='Select Image', font= font_main, command=self.select_image, background=self.colours['text'], foreground=self.colours['bg_dark'], highlightbackground=self.colours['bg_dark'], height=2, width=10)
        selectFileButton.place(x=10, y=175, anchor='w')

        self.nutrientsInfo = ttk.Label(frame, text='', font=('Manrope', 35), foreground=self.colours['text'], background=self.colours['border'])
        self.nutrientsInfo.place(x=210, y=190, anchor='center')
        
        

    '''
    Applys an existance check to the filename to see whether a file was selected and then runs it through the fruitClassifier runClassifier command.
    Then assigns the returned values to two variables.
    '''
    def runClassifier(self):
        if self.filename:
            self.acc, self.fruitName = self.fruitClassifier.runClassifier(self.filename)
            
    '''
    Creates the object for the fooddata central API and then requests the data for the classified fruit.
    '''
    def getNutrientData(self):
        nutrientData = NutrientData()
        self.energy, self.carb, self.sugar, self.protein, self.fat = nutrientData.getNutrientData(self.fruitName)

        print(f"Nutrient data for {self.fruitName}: {self.energy}, {self.carb}, {self.sugar}, {self.protein}, {self.fat}")

    '''
    Uses tks askopenfilename to let the iser to pick a photo they wish to classifiy then it applys an existence check and runs the previous functions.
    '''
    def select_image(self):
        self.filename = askopenfilename()

        if self.filename:
            # Here you can add the logic to process the selected image
            print(f"Selected file: {self.filename}")
            
            
            img = Image.open(self.filename).resize((300, 300))
            self.img = ImageTk.PhotoImage(img)

            my_label = Label(self.root, image=self.img)
            my_label.place(x=10, y=400, anchor='w')
            
              
            self.runClassifier()
            self.getNutrientData()
            self.nutrientsInfo.config(text=f"Nutrient data for {self.fruitName}: \nEnergy: {round(self.energy[0], 2)}kcal \nCarbohydrates: {round(self.carb[0], 2)}g \nSugars: {round(self.sugar[0], 2)}g \nProtein: {round(self.protein[0], 2)}g \nTotal Fat: {round(self.fat[0], 2)}g \n\nPer 100g", anchor='center')

        else:
            print("No file selected")
            tk.messagebox.showinfo("No Selection", "No file was selected. Please try again.")


# Create the main application window
app = Tk()
app_instance = App(app)
app.mainloop()
