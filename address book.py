from tkinter import*

mainscreen=Tk()
mainscreen.geometry("500x400")

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

editbutton=Button(frame4,text="Edit")
editbutton.grid(row=0,column=0)

deletebutton=Button(frame4,text="Delete")
deletebutton.grid(row=0,column=1)

updatebutton=Button(frame4,text="Update/Add")
updatebutton.grid(row=0,column=2,columnspan=2)

savebutton=Button(frame4,text="Save",width=20)
savebutton.grid(row=1,column=0,columnspan=2)






















mainscreen.mainloop()