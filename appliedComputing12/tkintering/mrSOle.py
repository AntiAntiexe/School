from tkinter import *
from tkinter import messagebox

# Initialize the main window
window = Tk()
window.title("Welcome to Mr. Sole's app")
window.geometry('500x500')
window.configure(bg="#bf88c6")

# Create the label for "Contract"
l = Label(window, text="Soul Contract")
l.config(font=("Courier", 14))
l.pack(pady=10)

# Create the text widget to display the fact
T = Text(window, height=20, width=50)
T.insert(END, "Do you agree to give your eternal soul to Mr. Sole? Please note that this agreement can not be cancelled or altered in any way. Have a nice day.")
T.pack(pady=10)

# Function for the button click event
def clicked():
    messagebox.showinfo('Contract', 'Yes, I agree!')

# Create the button
btn = Button(window, text='Click me', command=clicked)
btn.config(font=("Courier New", 14))
btn.pack(side=TOP, padx=10, pady=10)

# Run the application
window.mainloop()
