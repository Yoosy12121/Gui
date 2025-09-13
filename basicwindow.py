from tkinter import*

mainwindow=Tk()
mainwindow.geometry("250x250")
button1=Button(mainwindow,text="Login",background="Blue",foreground="Yellow",bd=5)
button1.pack(side="top")
closebutton=Button(mainwindow,text="Close",background="Black",foreground="Red",command=mainwindow.destroy)
closebutton.pack()

mainwindow.mainloop()
