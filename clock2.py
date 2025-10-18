from tkinter import *
from time import strftime
import random  

mainscreen = Tk()
mainscreen.title("Color Changing Clock")

display = Label(mainscreen, text="hi", font=("arial", 80), background="black", foreground="white")
display.pack(side="top", padx=10, pady=10)


colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "cyan"]

def get():
    currenttime = strftime("%H:%M:%S")
    display.config(text=currenttime)

    newcolour = random.choice(colours)
    display.config(background=newcolour)

    if newcolour in ["yellow", "white", "pink", "cyan"]:
        display.config(foreground="black")
    else:
        display.config(foreground="white")

    display.after(1000, get)

get()
mainscreen.mainloop()
