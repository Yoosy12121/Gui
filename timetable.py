from tkinter import*
from tkinter.ttk import*

def generatetable():
    n=selectednumber.get()
    r=selectedrd.get()
    result=""
    for i in range(r+1): 
        result=result+str(n)+"x"+str(i)+"="+str(n*i)+"\n"
    print (result)
    answer.config(text=result)

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

range1=Label(mainscreen,text="Range",font=("arial",20))
range1.pack(side="top")

selectedrd=IntVar()


r10=Radiobutton(mainscreen,text="10",value=10,variable=selectedrd)
r10.pack(side="top")
r15=Radiobutton(mainscreen,text="15",value=15,variable=selectedrd)
r15.pack(side="top")
r20=Radiobutton(mainscreen,text="20",value=20,variable=selectedrd)
r20.pack(side="top")

selectedrd.set(10)

calculate=Button(mainscreen,text="Calculate",command=generatetable)
calculate.pack(side="top")


answer=Label(mainscreen,text="0")
answer.pack(side="top")







mainscreen.mainloop()
