from tkinter import *
from tkinter.filedialog import *

def add_item():
    value = entryblock.get()
    if value.strip():
        listbox.insert(END, value)
  

def delete_item():
    selected = listbox.curselection()
    selected = selected[::-1]  
    for i in selected:
        listbox.delete(i)

def change_color():
    selected = listbox.curselection()
    if selected:
        mainscreen.configure(bg=listbox.get(selected[0]))


mainscreen = Tk()
mainscreen.geometry("500x400")



entryblock = Entry(mainscreen, width=30)
entryblock.pack(pady=10)


addbutton = Button(mainscreen, text="Add", width=15, command=add_item)
addbutton.pack(pady=5)

deleteButton = Button(mainscreen, text="Delete", width=15, command=delete_item)
deleteButton.pack(pady=5)

changebutton = Button(mainscreen, text="Change Color", width=20, command=change_color)
changebutton.pack(pady=10)


listbox = Listbox(mainscreen, width=40, height=10, selectmode=MULTIPLE)
colors = ["red", "green", "blue", "yellow", "pink", "orange", "purple"]
for i in colors:
    listbox.insert(END, i)
listbox.pack(pady=10)



mainscreen.mainloop()
