import tkinter as tk

from tkinterweb import HtmlFrame # import the HtmlFrame widget


root = tk.Tk() # create the Tkinter window


### The important part: create the html widget and attach it to the window

yourhtmlframe = HtmlFrame(root) # create the HtmlFrame widget
yourhtmlframe.load_website("google.com")

yourhtmlframe.pack(fill="both", expand=True) # attach the HtmlFrame widget to the window


root.mainloop()


