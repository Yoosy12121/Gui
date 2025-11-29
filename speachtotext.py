from tkinter import*
from gtts import gTTS
import speech_recognition as sr
from tkinter.filedialog import*
from tkinter import messagebox

def record():
    speech=sr.Recognizer()
    with sr.Microphone() as source:
        audio=speech.listen(source)
        try:
            text=speech.recognize_google(audio)
        except:
            text=("Sorry could no recognize your voice")
    speachtotext.insert(END,text)
            
def clear():
    speachtotext.delete(1.0,END)

def save():
    saveas=asksaveasfile(filetypes=[("Text Document","*.txt")])
    if saveas is not None:
        text=speachtotext.get(1.0,END)
        print(text,file=saveas)
    else:
        messagebox.showwarning("Warning","Could not save")

mainscreen=Tk()
mainscreen.geometry("700x400")

title=Label(text="Speach to text",font=(25))
title.pack(side="top")

recordaudio=Button(text="Record audio",font=(15),command=record)
recordaudio.pack(side="left")

speachtotext=Text(height=10,width=50)
speachtotext.pack(side="left")

save=Button(text="Save to file",font=(15),command=save)
save.pack(side="left")

cleartext=Button(text="Clear text",font=(15),command=clear)
cleartext.pack(side="left")

































mainscreen.mainloop()