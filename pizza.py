from tkinter import*
from tkinter.ttk import*

mainscreen=Tk()
mainscreen.geometry("500x200")

heading=Label(mainscreen,text="Welcome to Pizza Hut",font=("arial",15))
heading.place(x=150,y=0)

pizzaselection=Label(mainscreen,text="Select your pizza",font=("arial",10))
pizzaselection.place(x=70, y=50)
pizzas=["Margherita"," Pepperoni","Hawaiian"]
choice=StringVar()
option=OptionMenu(mainscreen,choice,pizzas)
option.place(x=190,y=49)

enterquantity=Label(mainscreen,text="Enter quantity",font=("arial",10))
enterquantity.place(x=71,y=80)

numberofpizzas=Combobox(mainscreen,text="0")
numberofpizzas.place(x=180,y=80)
numberofpizzas["values"]=tuple(range(1,1000))

orderbutton=Button(mainscreen,text="Order")
orderbutton.place(x=220,y=120)

chosenrd=IntVar()


rs = Radiobutton(mainscreen, text="S",value="S",variable=chosenrd)
rs.place(x=450, y=50)

rm = Radiobutton(mainscreen, text="M",value="M",variable=chosenrd)
rm.place(x=450, y=80)

rl = Radiobutton(mainscreen, text="L",value="l",variable=chosenrd)
rl.place(x=450, y=110)

chosenrd.set(S)

































mainscreen.mainloop()
