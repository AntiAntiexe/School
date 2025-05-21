from customtkinter import *
import customtkinter
import csv

app = CTk()
app.title('Choose Ice Cream')
app.geometry("500x500")
set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)


class WaverleyStars:
    def __init__(self):
        #fonts
        self.font_title = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")
        self.font_para = customtkinter.CTkFont(family="Helvetica", size=15, weight="normal")

        self.title = customtkinter.CTkLabel(master=app, text='Waverley Stars', font=self.font_title)
        self.title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.nameEntry = CTkEntry(master=app, placeholder_text="Enter your name", 
                                  font=(self.font_para))
        self.nameEntry.place(relx=0.2, rely=0.2, anchor=CENTER)

        self.dateEntry = CTkEntry(master=app, placeholder_text="Enter Date (dd/mm/yy)", 
                                  font=(self.font_para))
        self.dateEntry.place(relx=0.2, rely=0.3, anchor=CENTER)

        self.eventEntry = CTkEntry(master=app, placeholder_text="Enter Event", 
                                  font=(self.font_para))
        self.eventEntry.place(relx=0.2, rely=0.4, anchor=CENTER)

        self.hoursEntry = CTkEntry(master=app, placeholder_text="Enter Hours", font=(self.font_para))
        self.hoursEntry.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.minutesEntry = CTkEntry(master=app, placeholder_text="Enter Minutes",
                                  font=(self.font_para))
        self.minutesEntry.place(relx=0.2, rely=0.6, anchor=CENTER)
        self.secondsEntry = CTkEntry(master=app, placeholder_text="Enter Seconds",
                                  font=(self.font_para))
        self.secondsEntry.place(relx=0.2, rely=0.7, anchor=CENTER)

        self.timeConvertLbl = CTkLabel(master=app, text="Time convert", font=self.font_para)
        self.timeConvertLbl.place(relx=0.6, rely=0.175, anchor=CENTER)

        self.timeUnitDropdown = CTkOptionMenu(master=app, values=["Select", "Seconds", "Minutes", "Hours"])
        self.timeUnitDropdown.set("Select")
        self.timeUnitDropdown.place(relx=0.6, rely=0.25, anchor=CENTER)

        self.resultLbl = CTkLabel(master=app, text="Result", font=self.font_para)

        self.submitButton = CTkButton(master=app, text="Submit", command=self.submit)
        self.submitButton.place(relx=0.5, rely=0.8, anchor=CENTER)

    def save(self, name, event, date, finalTime, unit):
        finalTime = str(round(finalTime, 1)) + unit
        data = {'Name': name, 'event': event, 'date': date, 'finalTime':finalTime}

        with open('SoftwareDev10/CAT/Athlete.csv', 'w', newline='') as csvfile:
            fieldnames = ['Name', 'event', 'date', 'finalTime']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            #writer.writerow([customerName, totalOrderValue, finalOrderValue, totalOrderDiscount])
            writer.writerow(data)

    def submit(self):
        name = self.nameEntry.get()
        event = self.eventEntry.get()
        date = self.dateEntry.get()
        hours = float(self.hoursEntry.get())
        minutes = float(self.minutesEntry.get())
        seconds = float(self.secondsEntry.get())
        timeUnit = self.timeUnitDropdown.get()

        if timeUnit == "Seconds":
            totalTime = (hours * 3600) + (minutes * 60) + seconds
            self.resultLbl.configure(text=f"{name} has completed {event} \n on {date} in {round(totalTime, 1)} seconds")
        elif timeUnit == "Minutes":
            totalTime = (hours *60) + minutes + (seconds / 60)
            self.resultLbl.configure(text=f"{name} has completed {event} \n on {date} in {round(totalTime, 1)} minutes")
        elif timeUnit == "Hours":
            totalTime = hours + (minutes / 60) + (seconds / 3600)
            self.resultLbl.configure(text=f"{name} has completed {event} \n on {date} in {round(totalTime, 1)} hours")
        else:
            self.resultLbl.configure(text="Please select a time unit")
        self.resultLbl.place(relx=0.6, rely=0.4, anchor=CENTER)

        self.save(name, event, date, totalTime, timeUnit)
    

WaverleyStars()
app.mainloop()