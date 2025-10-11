from tkinter import*
from tkinter.ttk import*

mainscreen=Tk()
mainscreen.geometry("500x600")

heading=Label(mainscreen,text="Multiplication table",font=("arial",25))
heading.pack(side="top")

numberlabel=Label(mainscreen,text="Number",font=("arial",20))
numberlabel.pack(side="top")

selectednumber=IntVar()

numbercombo=Combobox(mainscreen,textvariable=selectednumber)
numbercombo.pack(side="top")
numbercombo["values"]=tuple(range(1,13))
selectednumber.set(1)

range=Label(mainscreen,text="Range",font=("arial",20))
range.pack(side="top")











mainscreen.mainloop()