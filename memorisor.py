from tkinter import*
from tkinter.filedialog import*

def adding():
    text=entryblock.get()
    if len(text.strip())>0:
        list.insert(END,text)

def remove():
    index=list.curselection()
    print(index)
    index=index[ : :-1]
    if index:
        for i in index:
            list.delete(i)

def save():
    saveas=asksaveasfile(filetypes=[("Text Document","*.txt")])
    if saveas is not None:
        for item in list.get(0,END):
            print(item,file=saveas)
        list.delete(0,END)

def enter():
    file=askopenfile()
    if file is not None:
        content=file.readlines()
        for item in content:
            list.insert(END,item)
mainscreen=Tk()
mainscreen.geometry("500x250")

savebutton=Button(mainscreen,text="Save",font=("arial",15),command=save)
savebutton.pack(side="top")

entryblock=Entry(mainscreen,text="",)
entryblock.pack(side="top")

addbutton=Button(mainscreen,text="Add",command=adding)
addbutton.pack(side="top")

scrollwheel=Scrollbar(mainscreen)
scrollwheel.pack(side="right",fill=Y)

list=Listbox(mainscreen,yscrollcommand=scrollwheel.set,selectmode=MULTIPLE)
for i in range (10):
    list.insert(END,str(i)+"hi")
list.pack(side="top")

openbutton=Button(mainscreen,text="Open",command=enter)
openbutton.place(x=80,y=100)

deleteButton=Button(mainscreen,text="Delete",command=remove)
deleteButton.place(x=420,y=90)

























mainscreen.mainloop()