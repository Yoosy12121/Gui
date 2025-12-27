from tkinter import*
from tkinter import messagebox

mainscreen=Tk()
mainscreen.geometry("500x400")

addressbook={}
def add():
    name=nameentry.get()
    address=addressentry.get()
    mobile=mobileentry.get()
    email=emailentry.get()
    birthday=birthdayentry.get()
    if name == "" :
        messagebox.showinfo("Info","Please insert a name.")
    else:
        if name not in addressbook:
            namelistbox.insert(END,name)
        addressbook[name]=(address,mobile,email,birthday)
        clearall()
        print(addressbook)

def clearall():
    nameentry.delete(0,END)
    addressentry.delete(0,END)
    mobileentry.delete(0,END)
    emailentry.delete(0,END)
    birthdayentry.delete(0,END)



def edit():
    clearall()
    indexselection=namelistbox.curselection()
    if indexselection:
        selected=namelistbox.get(indexselection)
        details=addressbook[selected]
        nameentry.insert(0,selected)
        addressentry.insert(0,details[0])
        mobileentry.insert(0,details[1])
        emailentry.insert(0,details[2])
        birthdayentry.insert(0,details[3])
    else:
        messagebox.showinfo("Info","Please select a name.")



frame1=Frame(mainscreen)
frame1.pack(side="top",pady=2)

title=Label(master=frame1,text="Addres book")
title.grid(row=0,column=0,padx=10,)

openbutton=Button(master=frame1,text="Open")
openbutton.grid(row=0,column=1,padx=10,)

frame2=Frame(mainscreen)
frame2.pack(side="left")

namelistbox=Listbox(frame2,height=13,width=25)
namelistbox.grid(row=0,column=0)

frame3=Frame(mainscreen)
frame3.pack(side="right")

namelabel=Label(frame3,text="Name")
namelabel.grid(row=0,column=0)

nameentry=Entry(frame3)
nameentry.grid(row=0,column=1,pady=10,padx=5)

addresslabel=Label(frame3,text="Address")
addresslabel.grid(row=1,column=0,pady=10,padx=5)

addressentry=Entry(frame3)
addressentry.grid(row=1,column=1,pady=10,padx=5)


mobilelabel=Label(frame3,text="Mobile")
mobilelabel.grid(row=2,column=0,pady=10,padx=5)

mobileentry=Entry(frame3)
mobileentry.grid(row=2,column=1,pady=10,padx=5)


emaillabel=Label(frame3,text="Email")
emaillabel.grid(row=3,column=0,pady=10,padx=5)

emailentry=Entry(frame3)
emailentry.grid(row=3,column=1,pady=10,padx=5)


birthdaylabel=Label(frame3,text="Birthday")
birthdaylabel.grid(row=4,column=0,pady=10,padx=5)

birthdayentry=Entry(frame3)
birthdayentry.grid(row=4,column=1,pady=10,padx=5)

frame4=Frame(mainscreen)
frame4.pack(side="bottom")

editbutton=Button(frame4,text="Edit",command=edit)
editbutton.grid(row=0,column=0)

deletebutton=Button(frame4,text="Delete")
deletebutton.grid(row=0,column=1)

updatebutton=Button(frame4,text="Update/Add",command=add)
updatebutton.grid(row=0,column=2,columnspan=2)

savebutton=Button(frame4,text="Save",width=20)
savebutton.grid(row=1,column=0,columnspan=2)






















mainscreen.mainloop()