import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.randint(0, 2)

    user_label.config(text=f"You chose: {choices[user_choice]}")
    comp_label.config(text=f"Computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=result)

# Window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Labels
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title.pack(pady=10)

user_label = tk.Label(root, text="")
user_label.pack()

comp_label = tk.Label(root, text="")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Rock", width=10, command=lambda: play(0)).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: play(1)).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors", width=10, command=lambda: play(2)).grid(row=0, column=2, padx=5)

root.mainloop()