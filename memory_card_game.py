import tkinter as tk
import random
from functools import partial
from tkinter import messagebox

# ساخت پنجره اصلی
root = tk.Tk()
root.title("Memory Card Game")

# لیست کارت‌ها (هر کارت دوبار برای جفت شدن)
cards = ['🍎','🍌','🍇','🍉','🍒','🥝','🍍','🥭'] * 2
random.shuffle(cards)

# متغیرها برای مدیریت بازی
buttons = []
first_choice = None
second_choice = None
matched_pairs = 0

# تابع بررسی انتخاب کارت
def check_card(index):
    global first_choice, second_choice, matched_pairs

    button = buttons[index]
    button.config(text=cards[index], state="disabled")

    if first_choice is None:
        first_choice = index
    else:
        second_choice = index
        root.after(1000, check_match)

def check_match():
    global first_choice, second_choice, matched_pairs

    if cards[first_choice] == cards[second_choice]:
        matched_pairs += 1
    else:
        buttons[first_choice].config(text="", state="normal")
        buttons[second_choice].config(text="", state="normal")

    first_choice = None
    second_choice = None

    if matched_pairs == len(cards)//2:
        messagebox.showinfo("تبریک!", "تمام جفت‌ها پیدا شدند!")

# ساخت دکمه‌ها برای کارت‌ها
for i in range(len(cards)):
    button = tk.Button(root, text="", width=6, height=3, font=("Arial", 20),
                       command=partial(check_card, i))
    button.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(button)

root.mainloop()