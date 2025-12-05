#create window
from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Search")
window.geometry('350x200')

import csv

data=[]
with open("softwareDev34/Unit3/AOS1/numbers.csv")as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        data.append(row)

arr = [x[0]for x in data]# this is column one
#colTwo = [x[1]for x in data]# this is column two
#print(colOne)# print and check whether you get the correct output
print(arr)
arr.sort(key=int)
print(arr)

def binarySearch():
    low = 0
    high = len(arr)-1
    boolFound = False
    
    while not boolFound  and low<=high:
        mid=(high+low)//2# // floor division
        print(mid)
        if  int(arr[mid]) == int(e1.get()):
            boolFound = True
            
        elif int(arr[mid]) >int(e1.get()):
            high =mid-1 

        else:
           low=mid+1

    if boolFound:
        lblmessage.config(text="found")
    else:
        lblmessage.config(text="not found")

#label message
lblmessage = ttk.Label(window, text =" ")
lblmessage.pack()

 #Create input
e1 = ttk.Entry(window)
e1.pack()

#create button
btnSearch = ttk.Button(window, text="binarySearch")
btnSearch.pack()
btnSearch.config(command=binarySearch)

mainloop()

#Suggested modification
#display a message instead of the label
#"'number' found at 'index'" as the message/label