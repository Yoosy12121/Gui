from tkinter import *
import random
from tkinter import messagebox


mainscreen = Tk()
mainscreen.geometry("400x400")
mainscreen.title("Guess the Number Game")


heading = Label(mainscreen, text="Welcome", font=("Arial", 20, "bold"))
heading.pack(side="top", pady=10)

entername = Label(mainscreen, text="Enter your name please.", font=("Arial", 14))
entername.pack(side="top", pady=5)

box = Entry(mainscreen, font=("Arial", 14))
box.pack(side="top", pady=5)


number = random.randint(1, 20)


def start_game():
    name = box.get()
    

    messagebox.showinfo("Welcome", f"Hi {name}! I am thinking of a number between 1 and 20. Can you guess it?")
    

    heading.destroy()
    entername.destroy()
    box.destroy()
    enterbutton.destroy()
    

    guess_label = Label(mainscreen, text="Enter your guess:", font=("Arial", 14))
    guess_label.pack(pady=10)
    
    guess_entry = Entry(mainscreen, font=("Arial", 14))
    guess_entry.pack(pady=5)
    
    # Function to check the guess
    def check_guess():
        guess = int(guess_entry.get())
        if guess < number:
            messagebox.showinfo("Result", "Your guess is too low!")
        elif guess > number:
            messagebox.showinfo("Result", "Your guess is too high!")
        else:
            messagebox.showinfo("Congratulations!", f" You guessed it right, {name}! The number was {number}.")
            mainscreen.destroy()
    # Guess button
    guess_button = Button(mainscreen, text="Guess", font=("Arial", 14, "bold"), relief="raised", command=check_guess)
    guess_button.pack(pady=10)

# Enter button (calls the function)
enterbutton = Button(mainscreen, text="Enter", font=("Arial", 14, "bold"), relief="raised", command=start_game)
enterbutton.pack(side="top", pady=10)

# Run the window
mainscreen.mainloop()
