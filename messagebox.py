from tkinter import*
from tkinter import messagebox


mainscreen=Tk()
mainscreen.geometry("200x200")

#heading
heading=Label(text="Message window",font=("arial",20))
heading.pack(side="top")

messagebox.showinfo("Info","Hello")

messagebox.showwarning("Warning","Hi")

messagebox.showerror("Error","Hola")

answer=messagebox.askquestion("question","Do you like cats")

print(answer)

print(messagebox.askokcancel("cancel","Would you like to proceed"))

print(messagebox.askyesno("yes or no","Are dogs better than cats"))

print(messagebox.askretrycancel("Retry or cancel","You got 10 out of 20 in your test"))







mainscreen.mainloop()

