from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Tic Tac Toe")
frm = ttk.Frame(root, padding=10, borderwidth=10, border=10)
frm.grid()
style = ttk.Style()
style.configure('TFrame', background='lightgray')


user_numbers = []
computer_numbers = []
numbers_list = list(range(1, 10))
selected = 0


def game():
    global selected
    selected_button = root.focus_get()
    selected = str(selected_button).split("n")[1]
    selected_button["text"] = "X"
    selected_button["state"] = DISABLED
    if selected == "":
        selected = 1

    else:
        selected = int(selected)

    if selected in numbers_list:
        numbers_list.remove(selected)
        user_numbers.append(selected)
        if check_winner(user_numbers):
            style.configure('TFrame', background='green')
            disable_buttons()

        else:
            computer_move()


def computer_move():
    global numbers_list

    if len(numbers_list) > 0:
        computer = random.choice(numbers_list)
        numbers_list.remove(computer)
        computer_numbers.append(computer)
        buttons[computer - 1]["text"] = "O"
        buttons[computer - 1]["state"] = DISABLED
        if check_winner(computer_numbers):
            style.configure('TFrame', background='red')
            disable_buttons()


def check_winner(numbers):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for comb in winning_combinations:
        if all(num in numbers for num in comb):
            return True
    return False


def disable_buttons():
    for button in buttons:
        button["state"] = DISABLED


def restart_game():
    global user_numbers, computer_numbers, numbers_list
    style.configure('TFrame', background='lightgray')
    for button in buttons:
        button["state"] = NORMAL
        button["text"] = ""
        user_numbers = []
        computer_numbers = []
        numbers_list = list(range(1, 10))


buttons = []
for col in range(3):
    for row in range(3):
        button = ttk.Button(frm, padding=30, width=5, text="", command=game)
        button.grid(column=col, row=row)
        buttons.append(button)
ttk.Button(frm, padding=15, width=5, text="Restart", command=restart_game).grid(column=1, row=3)

root.mainloop()
