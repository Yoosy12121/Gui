from tkinter import*
from gtts import gTTS
import os

mainscreen=Tk()
mainscreen.geometry("400x100")

def submit():
    text=enter.get()
    speach=gTTS(text=text,lang="en")
    speach.save("Speach.wav")
    os.system("speach.wav")


title=Label(text="Welcome",font=(15))
title.pack(side="top")

enter=Entry(relief="raised",width="50")
enter.pack(side="top")

submit=Button(text="Submit",font=(15),command=submit)
submit.pack(side="top")
























mainscreen.mainloop()