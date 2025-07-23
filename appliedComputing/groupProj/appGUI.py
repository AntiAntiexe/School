from logging import root
import tkinter as tk
from tkinter import ttk

from matplotlib import style

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

        style = ttk.Style(self.root)
        style.theme_use('classic')

        font_main = ('Helvetica', 50, 'bold')
        label = tk.Label(self.root, text='NutriVision', font=font_main, foreground=self.colours['text'], background=self.colours['bg_dark'])
        label.grid(column=0, row=0, padx=100, pady=0, sticky='w')

        button = tk.Button(self.root, text='Select Image', command=self.select_image, background=self.colours['text'], foreground=self.colours['bg_dark'], highlightbackground=self.colours['bg_dark'])
        button.grid(column=0, row=1, padx=10, pady=10, sticky='w')


    def select_image(self):
        pass

app = tk.Tk()
frm = ttk.Frame(app, padding=10)
frm.grid()
app_instance = App(app, frm)
app.mainloop()