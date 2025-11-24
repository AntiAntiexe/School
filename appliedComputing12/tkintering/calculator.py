from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Two Number Calculator")
window.geometry("600x200")

firstNum = IntVar()
secondNum = IntVar()



lbl = Label(window, text="Enter Number One")

lbl.grid(column=0, row=0, pady=10, padx=10, columnspan=1, sticky="W")

lbl2 = Label(window, text="Enter Number Two")

lbl2.grid(column=0, row=1, pady=10, padx=10, columnspan=1, sticky="W")

entry1 = Entry(window, textvariable=firstNum).grid(row=0, column=1, sticky="W")

entry2 = Entry(window, textvariable=secondNum).grid(row=1, column=1, sticky="W")

def add():
    sums = firstNum.get() + secondNum.get()
    Answer.config(text="Your numbers added together are: " + str(sums))

def subtract():
    diff = firstNum.get() - secondNum.get()
    Answer.config(text="Your numbers subtracted are: " + str(diff))

def multiply():
    product = firstNum.get() * secondNum.get()
    Answer.config(text="Your numbers multiplied together are: " + str(product))

def divide():
    quotient = firstNum.get() / secondNum.get()
    Answer.config(text="Your numbers divided together are: " + str(quotient))

btnAdd = Button(window, text="Add", command=add).grid(column=0, row =2, sticky="W", columnspan=1)
btnSub = Button(window, text="Subtract", command=subtract).grid(column=1, row =2, sticky="W")
btnMulti = Button(window, text="Multiply", command=multiply).grid(column=2, row =2, sticky="W")
btnDiv = Button(window, text="Divide", command=divide).grid(column=3, row =2, sticky="W", columnspan=1)


Answer = Label(window)
Answer.grid(row=4, column=0, pady=10, padx=10, columnspan=3, sticky="W")


window.mainloop()