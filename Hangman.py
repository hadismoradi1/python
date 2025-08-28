import tkinter as tk
import random

# لیست کلمات
words = ["سیب", "موز", "پرتقال", "هندوانه", "انگور"]
chosen_word = random.choice(words)
word_length = len(chosen_word)

# وضعیت حدس‌ها
display = ["_"] * word_length
attempts = 6
guessed_letters = []

# تابع برای حدس حرف
def guess_letter():
    global attempts
    letter = entry.get()
    entry.delete(0, tk.END)

    if letter in guessed_letters:
        message_label.config(text="این حرف رو قبلاً حدس زدی!")
        return

    guessed_letters.append(letter)

    if letter in chosen_word:
        for i, l in enumerate(chosen_word):
            if l == letter:
                display[i] = letter
        message_label.config(text="حرف درست! 🎉")
    else:
        attempts -= 1
        message_label.config(text=f"حرف اشتباه! {attempts} شانس باقی مانده.")

    word_label.config(text=" ".join(display))

    if "_" not in display:
        message_label.config(text="آفرین! کلمه درست حدس زده شد 😃")
        entry.config(state="disabled")
        guess_btn.config(state="disabled")
    elif attempts == 0:
        message_label.config(text=f"متاسفم! شانس‌ها تمام شد. کلمه درست بود: {chosen_word}")
        entry.config(state="disabled")
        guess_btn.config(state="disabled")

# ساخت پنجره اصلی
root = tk.Tk()
root.title("بازی Hangman")

# نمایش کلمه
word_label = tk.Label(root, text=" ".join(display), font=("Arial", 24))
word_label.pack(pady=20)

# پیام‌ها
message_label = tk.Label(root, text=f"تو {attempts} شانس داری!", font=("Arial", 14))
message_label.pack(pady=10)

# ورود حرف
entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

# دکمه حدس
guess_btn = tk.Button(root, text="حدس بزن", command=guess_letter)
guess_btn.pack(pady=10)

root.mainloop()