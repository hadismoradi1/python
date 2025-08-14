import tkinter as tk
import random

quotes= [
    "هیچوقت برای شروع دیر نیست⭐",
    "باور داشته باش که میتونی و در نیمه راهی⭐",
    "هر روز یک قدم کوچک هم پیشرفت است⭐",
    "امروز بهترین فرصت برای شروع است⭐",
    "شکست مقدمه پیروزی است⭐",
    "خودت را باور کن⭐",
    "خودت رو باور کن⭐",
]
colors = ["red", "blue", "green", "purple", "orange" , "pink", "cyan", "brown"]

def show_quotes():
    quote = random.choice(quotes)
    color = random.choice(colors)
    label_quote.config(text=quote, fg=color, bg="black")
    root.after(3000, show_quotes)

root = tk.Tk()
root.title("جملات انگیزشی اتوماتیک")
root.geometry("500x300")
root.configure(bg="black")

label_quote = tk.Label(root, text="", font=("Arial", 16), wraplength=400)
label_quote.pack(pady=100)

show_quotes()
root.mainloop()