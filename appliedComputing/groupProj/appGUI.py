import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from runTfLite import Classifier 
from usdaFood import NutrientData
import numpy as np
from runMainModel import FruitClassifier

'''
The App class initialises the variables required for the tkinter GUI.
This includes methods and objects for:
    colours
    UI elements
    fruit classifier
'''

class App:
    def __init__(self, root, frm):


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


        self.frm = frm
        self.root.title("NutriVision")
        self.root.geometry("800x600")
        self.root.configure(bg=self.colours['bg_dark'])

        self.predicter = Classifier('fruitModel.tflite')
        
        self.fruitClassifier = FruitClassifier()

        style = ttk.Style(self.root)
        style.theme_use('classic')
        
        #frame = ttk.Frame(self.root, height=300, width=300, )
        #frame.place(x=400, y=300, anchor='center')
        
        s = ttk.Style()
        s.configure('Danger.TFrame', background=self.colours['border'], borderwidth=5)
        
        frame = ttk.Frame(self.root, height=300, width=400, style='Danger.TFrame')
        frame.place(x=550, y=300, anchor='center')

        font_main = ('Manrope', 100, 'bold')
        label = ttk.Label(self.root, text='NutriVision', font=font_main, foreground=self.colours['text'], background=self.colours['bg_dark'])
        label.place(x=10, y=50, anchor='w')
        font_main = ('Manrope', 20, 'bold')
        selectFileButton = tk.Button(self.root, text='Select Image', font= font_main, command=self.select_image, background=self.colours['text'], foreground=self.colours['bg_dark'], highlightbackground=self.colours['bg_dark'], height=2, width=10)
        selectFileButton.place(x=10, y=175, anchor='w')

        #classifyButton = tk.Button(self.root, text='Classify Image', command=self.runClassifier, background=self.colours['text'], foreground=self.colours['bg_dark'], highlightbackground=self.colours['bg_dark'])
        #classifyButton.place(x=10, y=150, anchor='w')

        self.nutrientsInfo = ttk.Label(frame, text='', font=('Manrope', 12), foreground=self.colours['text'], background=self.colours['border'])
        self.nutrientsInfo.place(x=175, y=150, anchor='center')

    '''
    Applys an existance check to the filename to see whether a file was selected and then runs it through the fruitClassifier runClassifier command.
    Then assigns the returned values to two variables.
    '''
    def runClassifier(self):
        if self.filename:
            #self.predicter.classify(self.filename)
            #self.fruitClassifier.runClassifier(self.filename)
            #self.fruitName = self.fruitClassifier.fruitName
            
            self.acc, self.fruitName = self.fruitClassifier.runClassifier(self.filename)
    '''
    Creates the object for the fooddata central API and then requests the data for the classified fruit.
    '''

    def getNutrientData(self):
        nutrientData = NutrientData()
        self.nurtrients = nutrientData.getNutrientData(self.fruitName)

        print(f"Nutrient data for {self.fruitName}: {self.nurtrients}")

    '''
    Uses tks askopenfilename to let the iser to pick a photo they wish to classifiy then it applys an existence check and runs the previous functions.
    '''
    def select_image(self):
        self.filename = askopenfilename()

        if self.filename:
            # Here you can add the logic to process the selected image
            print(f"Selected file: {self.filename}")
            #tk.messagebox.showinfo("File Selected", f"You selected: {self.filename}")
            
            #panel.pl(side = "bottom", fill = "both", expand = "yes")
            #panel.place(x=100, y=400, anchor='center')
            
            canvas = Canvas(self.root, width = 300, height = 300)
            canvas.place(x=400, y=300, anchor='center')
            img = ImageTk.PhotoImage(Image.open(self.filename))
            canvas.create_image(20,20, anchor='center', image=img)
            
            self.runClassifier()
            self.getNutrientData()
            self.nutrientsInfo.config(text=f"Nutrient data for {self.fruitName}: {self.nurtrients}")
        else:
            print("No file selected")
            tk.messagebox.showinfo("No Selection", "No file was selected. Please try again.")

        

        

        
    
    

    



app = tk.Tk()
frm = ttk.Frame(app, padding=10)
frm.grid()
app_instance = App(app, frm)
app.mainloop()
