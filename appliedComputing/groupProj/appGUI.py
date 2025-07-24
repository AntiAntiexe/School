import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from runTfLite import Classifier 


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

        style = ttk.Style(self.root)
        style.theme_use('classic')

        font_main = ('Helvetica', 50, 'bold')
        label = ttk.Label(self.root, text='NutriVision', font=font_main, foreground=self.colours['text'], background=self.colours['bg_dark'])
        label.place(x=10, y=30, anchor='w')

        selectFileButton = tk.Button(self.root, text='Select Image', command=self.select_image, background=self.colours['text'], foreground=self.colours['bg_dark'], highlightbackground=self.colours['bg_dark'])
        selectFileButton.place(x=10, y=100, anchor='w')

        classifyButton = tk.Button(self.root, text='Classify Image', command=self.runClassifier, background=self.colours['text'], foreground=self.colours['bg_dark'], highlightbackground=self.colours['bg_dark'])
        classifyButton.place(x=10, y=150, anchor='w')


    def select_image(self):
        self.filename = askopenfilename()

        if self.filename:
            # Here you can add the logic to process the selected image
            print(f"Selected file: {self.filename}")
            tk.messagebox.showinfo("File Selected", f"You selected: {self.filename}")
        else:
            print("No file selected")
            tk.messagebox.showinfo("No Selection", "No file was selected. Please try again.")

        
    
    def runClassifier(self):
        if self.filename:
            self.predicter.classify(self.filename)

    def getNutrientData(self):
        # This method can be used to fetch nutrient data if needed
        pass

app = tk.Tk()
frm = ttk.Frame(app, padding=10)
frm.grid()
app_instance = App(app, frm)
app.mainloop()