from tkinter import *

root = Tk()
root.title("Scrollable Frame")
root.geometry("300x300")

canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
scrollable_frame = Frame(canvas)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

for i in range(30):
    Label(scrollable_frame, text=f"Item {i+1}", width=20).pack(pady=5)

root.mainloop()