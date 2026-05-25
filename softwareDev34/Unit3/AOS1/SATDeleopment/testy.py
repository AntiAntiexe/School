import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

# 'bg' is the unfocused color, 'activebackground' is the hovered/active color
btn = tk.Button(
    root, 
    text="Click Me", 
    bg="green", 
    activebackground="blue",
    fg="white"
)
btn.pack(pady=20)

root.mainloop()
