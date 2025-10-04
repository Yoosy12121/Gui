from tkinter import *
import random
from tkinter import messagebox

options=["rock","paper","scissors"]

pscore=0
cscore=0

def game(playerinput):
    global pscore,cscore
    computerinput=random.choice(options)
    playerselected.config(text=f"You selected:{playerinput}")
    computerselected.config(text=f"The computer selected:{computerinput}")
    if playerinput==computerinput:
        messagebox.showinfo("Tie","You and the computer tied")
    elif (playerinput== options[0] and computerinput==options[2]) or (playerinput==options[1] and computerinput== options[0]) or (playerinput==options[2]and computerinput==options[1]):
        messagebox.showinfo("Win","You won")
        pscore=pscore+1
        
    else:
        messagebox.showinfo("lost","You lost against the computer")
        cscore=cscore+1
    computerscore.config(text=f"The computer's score is:{cscore}")
    playerscore.config(text=f"Your score is:{pscore}")

    

mainscreen=Tk()
mainscreen.geometry("600x300")

#top frame
topframe=Frame(mainscreen)
topframe.pack()
heading=Label(topframe,text="Rock paper sissors",font=("arial",25))
heading.pack()

#middle frame
middleframe=Frame(mainscreen)
middleframe.pack()

option=Label(middleframe,text="Your options are ",font=("arial",20))
option.pack(side="left")

rock=Button(middleframe,text="Rock",font=("Bold",16),background="pink",command=lambda:game(options[0]))
rock.pack(side="left",padx=10,pady=10)

paper=Button(middleframe,text="Paper",font=("Bold",16),background="orange",command=lambda:game(options[1]))
paper.pack(side="left",padx=10,pady=10)

scissors=Button(middleframe,text="Scissors",font=("Bold",16),background="blue",command=lambda:game(options[2]))
scissors.pack(side="left",padx=10,pady=10)

#Bottom frame
bottomframe=Frame(mainscreen)
bottomframe.pack()

score=Label(bottomframe,text="Score:",font=("arial",20))
score.pack(side="left",padx=10,pady=10)

playerselected=Label(bottomframe,text="You selected:",font=("Bold",10))
playerselected.pack(side="bottom",padx=10,pady=10)

playerscore=Label(bottomframe,text="Your score is: ",font=("Bold",10))
playerscore.pack(side="bottom",padx=10,pady=10)

computerselected=Label(bottomframe,text="The computer selected:",font=("Bold",10))
computerselected.pack(side="bottom",padx=10,pady=10)

computerscore=Label(bottomframe,text="The computer's score is:",font=("Bold",10))
computerscore.pack(side="bottom",padx=10,pady=10)















mainscreen.mainloop()