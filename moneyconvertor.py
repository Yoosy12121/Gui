from tkinter import*

def convertor():
        pounds = float(convertorbox.get())  # get the number from entry
        dollars = pounds * 1.26  # example conversion rate
        target.config(text="Target currency amount $ " + str(dollars))

mainscreen=Tk()
mainscreen.geometry("600x300")

#top frame
topframe=Frame(mainscreen)
topframe.pack()
title=Label(topframe,text="£ to $",font=("Bold",25))
title.pack(side="top",padx=10,pady=10)

#middle frame
middleframe=Frame(mainscreen)
middleframe.pack()
source=Label(middleframe,text="source currency amount £",font=(10))
source.pack(side="left",padx=10,pady=10)
target=Label(middleframe,text="Target currency amount $",font=(10))
target.pack(side="left",padx=10,pady=10)
convertorbox=Entry(middleframe)
convertorbox.pack(side="right")

#bottom frame
bottomframe=Frame(mainscreen)
bottomframe.pack()
convert=Button(bottomframe,text="convert",font="20",background="green",command=convertor)
convert.pack(side="bottom")































mainscreen.mainloop()