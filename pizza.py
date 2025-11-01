from tkinter import*
from tkinter.ttk import*

mainscreen=Tk()
mainscreen.geometry("500x200")
names=["cat","dog","fish"]
choice=StringVar()
option=OptionMenu(mainscreen,choice,names)
option.pack(side="left")





























mainscreen.mainloop()
