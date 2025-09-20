from tkinter import*
import calendar

def showcaledar():
    calendarwindow=Tk()
    calendarwindow.geometry("800x550")
    year=int(yearbox.get())
    content=calendar.calendar(year)
    caltext=Text(calendarwindow,height=500)
    caltext.pack(side="top",padx=10,pady=10)
    caltext.insert(END,content)
    calendarwindow.mainloop()


mainscreen=Tk()
mainscreen.geometry("400x400")

calendar1=Label(mainscreen,text="Calendar",font=("bold",25),background="Black",foreground="white",relief="raised",borderwidth=3,underline=0,)
calendar1.pack(side="top")

enteryearbutton=Button(mainscreen,text="Enter year",font=10,relief="raised",borderwidth=3)
enteryearbutton.pack(side="top")

yearbox=Entry(mainscreen,relief="raised",borderwidth=3,font=10)
yearbox.pack(side="top")

showbutton=Button(mainscreen,text="Show calendar",font=10,command=showcaledar)
showbutton.pack(side="top")

closebutton=Button(mainscreen,text="Close",foreground="white",background="Black",command=mainscreen.destroy)
closebutton.pack(side="top")

mainscreen.mainloop()