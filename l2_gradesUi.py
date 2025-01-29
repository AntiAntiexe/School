from customtkinter import *
import customtkinter


class App:

    def __init__(self):
        super().__init__()

        self.app = CTk()
        self.app.title('Money Calculator')
        self.app.geometry("500x500")
        set_appearance_mode("dark")
        self.app.grid_columnconfigure(0, weight=1)

        # Fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")

        self.font_para = customtkinter.CTkFont(family="Helvetica", size=25, weight="normal", )

        # Title
        self.label = CTkLabel(master=self.app, text="Grade Checker!", font=self.font_title)
        self.label.place(relx=0.25, rely=0.1, anchor=CENTER)

        self.entry = CTkEntry(master=self.app, placeholder_text="Input grade", width=185, height=40,fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.font_para, 20))
        self.entry.place(relx=0.25, rely=0.2, anchor=CENTER)
        
        self.button = CTkButton(master=self.app, text="Reset", command=self.addCheck, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40, width=185,
                                   font=(self.font_para, 20))
        self.button.place(relx=0.25, rely=0.3, anchor=CENTER)

        self.result = CTkLabel(master=self.app, text="result", font=self.font_para)
        self.result.place(relx=0.25, rely=0.4, anchor=CENTER)
        

        self.app.mainloop()

    def gradeCheck(self, grade):
        if grade >= 90:
            return 'A'
        elif 80 <= grade <=89:
            return 'B'    
        elif 60 <= grade <=79:
            return 'C'   
        elif 40 <= grade <=59:
            return 'D'
        else:
            return 'F'
    def addCheck(self):
        grade = int(self.entry.get())
        result = self.gradeCheck(grade)

        self.result.configure(text=str(result))
        
        


App()