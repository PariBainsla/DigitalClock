from tkinter import Tk 
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")

clock = Label(master, font=("Calibri",90),bg="grey",fg="white")
clock.pack()

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

get_time()

master.mainloop()