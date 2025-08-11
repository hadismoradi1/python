import tkinter as tk
import time
import locale

try:
    locale.setlocale(locale.LC_TIME, "fa_IR")
except:
    pass


def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A,%d,%B,%Y")
    label_time.config(text=current_time)
    label_date.config(text=current_date)
    label_time.after(1000, update_time)


root = tk.Tk()
root.title("ساعت و تاریخ دیجیتال")
root.geometry("400x200")
root.configure(bg="black")

label_time = tk.Label(root, font=("Arial", 50), fg="cyan", bg="black")
label_time.pack(pady=10)
label_date = tk.Label(root, font=("Arial", 20), fg="white", bg="black")
label_date.pack()

update_time()
root.mainloop()
