import tkinter as tk
from tkinter import messagebox


# الگوریتم بک‌ترکینگ برای حل سودوکو
def is_valid(board, row, col, num):
    # بررسی سطر
    for i in range(9):
        if board[row][i] == num:
            return False

    # بررسی ستون
    for i in range(9):
        if board[i][col] == num:
            return False

    # بررسی مربع 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# گرفتن مقادیر از GUI
def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val.isdigit() else 0)
        board.append(row)
    return board


def fill_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            if board[i][j] != 0:
                entries[i][j].insert(0, str(board[i][j]))


def solve_sudoku():
    board = get_board()
    if solve(board):
        fill_board(board)
        messagebox.showinfo("نتیجه", "سودوکو حل شد ✅")
    else:
        messagebox.showerror("خطا", "راه حلی وجود نداره ❌")


# رابط گرافیکیsss
root = tk.Tk()
root.title("بازی سودوکو")

entries = [[None for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        e = tk.Entry(root, width=3, font=("Arial", 18), justify="center")
        e.grid(row=i, column=j, padx=2, pady=2)
        entries[i][j] = e

solve_button = tk.Button(root, text="حل کن", command=solve_sudoku)
solve_button.grid(row=9, column=0, columnspan=9, pady=10)

root.mainloop()