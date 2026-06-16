
from tkinter import *
from tkinter.ttk import *

app= Tk()

app.geometry('350x200')
app.title("Anton's app")

def changeText():
    lbl.configure(text="The button was clicked")

lbl = Tk.Label(app, text="This is an app")

lbl.grid(column=0, row=0)

btn = Button(app, text="Click Me", fg="blue", bg="grey", command=changeText())

btn.grid(column=1, row=0)

combo = Combobox(app)

combo['values']= (1, 2, 3, 4, 5, "Text")

combo.current(1) #set the selected item

combo.grid(column=2, row=0)

chk_state = BooleanVar()

chk_state.set(True) #set check state

chk = Checkbutton(app, text='Choose', var=chk_state)

chk.grid(column=3, row=0)

rad1 = Radiobutton(app,text='First', value=1)

rad2 = Radiobutton(app,text='Second', value=2)

rad3 = Radiobutton(app,text='Third', value=3)

rad1.grid(column=0, row=1)

rad2.grid(column=1, row=2)

rad3.grid(column=2, row=3)





app.mainloop()
