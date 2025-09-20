from tkinter import*

mainscreen=Tk()
mainscreen.geometry("400x400")
mainscreen.config(background="Red")

topframe=Frame(mainscreen,background="blue")
topframe.pack(padx=10,pady=10)

heading=Label(topframe,text="Chocolate ")
heading.grid(row=0,column=0,columnspan=3)

question1=Button(topframe,text="Milk Chocolate")
question1.grid(row=1,column=0,pady=10,padx=10)

question2=Button(topframe,text="Dark chocolate")
question2.grid(row=1,column=1,pady=10,padx=10)

question3=Button(topframe,text="White chocolate")
question3.grid(row=1,column=2,pady=10,padx=10)

bottomframe=Frame(mainscreen,background="yellow")
bottomframe.pack(side="bottom",padx=10,pady=10)

heading=Label(bottomframe,text="Icecream")
heading.grid(row=1,column=0)

question4=Button(bottomframe,text="Chocolate icecream")
question4.grid(row=2,column=0,pady=10)

question5=Button(bottomframe,text="Vanila icecream")
question5.grid(row=3,column=0,pady=10)

question6=Button(bottomframe,text="Caramel icecream")
question6.grid(row=4,column=0,pady=10)




mainscreen.mainloop()