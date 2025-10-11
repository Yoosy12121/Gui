from tkinter import*
from time import strftime

mainscreen=Tk()


display=Label(mainscreen,text="hi",font=("arial",80),background="black",foreground="white")
display.pack(side="top",padx=10,pady=10)

display1=Label(mainscreen,text="hi",font=("arial",80),background="black",foreground="white")
display1.pack(side="top",padx=10,pady=10)

def get():
    currenttime=strftime("%H:%M:%S")
    currentday=strftime("%a %d/%b/%y")
    display1.config(text=currentday)
    display.config(text=currenttime)
    display.after(1000,get)

get()












mainscreen.mainloop()