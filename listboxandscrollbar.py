from tkinter import*

mainscreen=Tk()
mainscreen.geometry("200x200")

scroll=Scrollbar(mainscreen)
scroll.pack(side="right",fill=Y)

numberlist=Listbox(mainscreen,yscrollcommand=scroll.set)
numberlist.pack(side="top",)

for i in range(20):
    numberlist.insert(END,i)

scroll.config(command=numberlist.yview)











mainscreen.mainloop()