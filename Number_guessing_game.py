import tkinter as tk
import ttkbootstrap as ttk
from random import randrange

def range_submit():
    from_range = from_var.get()
    to_range = to_var.get()
    if from_range > to_range:
        error_var.set("First number must be smaller than the second!!!")
    elif from_range == to_range:
        error_var.set("Numbers must be different!!!")
    else:
        random_number = randrange(from_range, to_range)
        number_var.set(random_number)
        print(random_number)

def guess_number():
    guessed_number = guessing_entry_var.get()
    guessing_number = number_var.get()
    guesses = number_of_guesses.get()
    if guessed_number > guessing_number:
        guessing_label_var.set("Number you are guessing is too big!!! Try again")
        number_of_guesses += 1
    elif guessed_number < guessing_number:
        guessing_label_var.set("Number you are guessing is too small!!! Try again")
        number_of_guesses += 1
    else:
        guessing_label_var.set(f"You guessed the number!!! The number was {guessing_number}. You guess in {guesses} tries!")
        number_of_guesses.set(0)

#window
window = ttk.Window(themename='journal')
window.title("Guessing game")
window.geometry('500x500')

#Start Frame (Pick range)
frame1 = ttk.Frame(master=window)
start_label = ttk.Label(master=frame1, text="Select a range", font='Calibri 24 italic')
from_var = tk.IntVar()
from_range_entry = ttk.Entry(master=frame1, textvariable=from_var)
to_var = tk.IntVar()
to_range_entry = ttk.Entry(master=frame1, textvariable=to_var)
range_submit_button = ttk.Button(master=frame1, text="Submit", command=range_submit)
error_var = tk.StringVar()
error_label = ttk.Label(master=frame1, textvariable=error_var)

frame1.pack()
start_label.pack()
from_range_entry.pack(side="left", padx=5)
to_range_entry.pack(side="left", padx=5)
range_submit_button.pack()

#Guessing Frame (Pick a number)
frame2 = ttk.Frame(master=window)
number_var = tk.IntVar()
number_of_guesses = tk.IntVar()
number_of_guesses.set(0)
guessing_label = ttk.Label(master=frame2, text="Try to guess a number!!!", font='Calibri 24 italic')
guessing_entry_var = tk.IntVar()
guessing_entry = ttk.Entry(master=frame2, textvariable=guessing_entry_var)
guessing_button = ttk.Button(master=frame2, text="Guess!!!", command=guess_number)
guessing_label_var = tk.StringVar()
guessing_label_finish = ttk.Label(master=frame2, textvariable=guessing_label_var)

frame2.pack()
guessing_label.pack()
guessing_entry.pack()
guessing_button.pack()
guessing_label_finish.pack()

#run
window.mainloop()