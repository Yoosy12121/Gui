from tkinter import*
import tkinter.font as font
def convertor():
    kg=float(measurementbox.get())
    grams = kg * 1000
    pounds = kg * 2.20
    ounces = kg * 35.27

    gram.config(text=str(grams) + " g")
    pound.config(text=str(pounds) + " lb")
    ounce.config(text=str(ounces) + " oz")
   


mainscreen=Tk()
mainscreen.geometry("400x200")


textstyle=font.Font(family="Arial",size=10,weight="bold")

#heading
heading=Label(text="Weight convertor",font=("arial",24))
heading.pack(side="top")

#topframe
topframe=Frame(mainscreen)
topframe.pack(padx=10,pady=10)

heading=Label(topframe,text="Enter the weight in kg.",relief="raised")
heading.pack(side="left")

measurementbox=Entry(topframe,relief="raised")
measurementbox.pack(side="left",padx=5,pady=5)

convertbutton=Button(topframe,text="Convert",relief="raised",command=convertor)
convertbutton.pack(side="left",padx=5,pady=5)

#bottomframe
bottomframe=Frame(mainscreen)
bottomframe.pack(padx=10,pady=10)

gramlabel=Label(bottomframe,text="Grams",relief="raised",font=textstyle)
gramlabel.grid(row=0,column=0,padx=25,pady=5)

poundlabel=Label(bottomframe,text="Pounds",relief="raised",font=textstyle)
poundlabel.grid(row=0,column=1,padx=25,pady=5)

ouncelabel=Label(bottomframe,text="Ounces",relief="raised",font=textstyle)
ouncelabel.grid(row=0,column=2,padx=25,pady=5)

gram=Label(bottomframe,text="Gram",relief="raised")
gram.grid(row=1,column=0,padx=25,pady=5)

pound=Label(bottomframe,text="Pounds",relief="raised")
pound.grid(row=1,column=1,padx=25,pady=5)

ounce=Label(bottomframe,text="Ounces",relief="raised")
ounce.grid(row=1,column=2,padx=25,pady=5)



mainscreen.mainloop()