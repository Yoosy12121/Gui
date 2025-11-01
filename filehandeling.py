from tkinter import*
from tkinter.filedialog import*

mainscreen=Tk()
mainscreen.geometry("500x250")

def savingfile():
    saveas=asksaveasfile(filetypes=[("Text Document","*.txt")])

def openingfile():
    file=askopenfile(filetypes=[("Text Document","*.txt")])
    if file is not None:
        reading=file.read()
        print(reading)
save=Button(mainscreen,text="Save",font=("arial",15),command=savingfile)
save.pack(side="top")

open=Button(mainscreen,text="Open",font=("arial",15),command=openingfile)
open.pack(side="top")


























mainscreen.mainloop()
