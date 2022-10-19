import f1api as f1
from tkinter import *
from tkinter import ttk


def set_result():
    dname=v1.get()
    syear=Season.get()
    Result1.config(text= f1.driver_points(dname,syear))

def getDriver():
    #To take te driver name
    v1.set("Select a Name")
    syear=Season.get()
    #dlist=f1.driver_names(syear)
    driverName = OptionMenu(frame,v1,*f1.driver_names(syear))
    driverName.grid(column=1,row=1)
    return v1

#Root Window
window=Tk()
window.geometry("400x200")

#Main Frame
frame=ttk.Frame(window,padding=10)
frame.grid()

#Labels
l1=Label(frame, text="Name")
l1.grid(column=0, row=1)
l2=Label(frame, text="Result")
l2.grid(column=0, row=2)
l3=Label(frame, text="Season")
l3.grid(column=0, row=0)

#Label to Display Result
Result1=Label(frame)
Result1.grid(column=1,row=2)

#To Get season year
Season=Entry(frame)
Season.grid(column=1,row=0)

#stores option menu value
v1=StringVar(frame)

#buttons
ttk.Button(frame, text="Quit", command=window.destroy).grid(column=2, row=3)
ttk.Button(frame, text="Get", command=set_result).grid(column=1, row=3)
ttk.Button(frame, text="Get names", command=getDriver).grid(column=0, row=3)

window.mainloop()








