import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic Tac Toe ❌⭕ (vs Computer)")

current_player = "X"
buttons = [[None]*3 for _ in range(3)]

def check_winner():
    # سطرها و ستون‌ها
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    # قطرها
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and current_player == "X":
        buttons[row][col]["text"] = "X"
        if check_winner():
            messagebox.showinfo("Game Over", "🎉 Player X wins!")
            reset_game()
            return
        elif is_draw():
            messagebox.showinfo("Game Over", "😅 It's a draw!")
            reset_game()
            return
        current_player = "O"
        root.after(500, computer_move)

def computer_move():
    global current_player
    empty_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]["text"] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        buttons[row][col]["text"] = "O"
        if check_winner():
            messagebox.showinfo("Game Over", "🤖 Computer (O) wins!")
            reset_game()
            return
        elif is_draw():
            messagebox.showinfo("Game Over", "😅 It's a draw!")
            reset_game()
            return
    current_player = "X"

def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""

# ساخت دکمه‌ها
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, bg="black", fg="orange",
                        command=lambda r=i, c=j: click(r, c))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

reset_btn = tk.Button(root, text="Restart 🔄", font=("Arial", 14), bg="black", fg="orange", command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()