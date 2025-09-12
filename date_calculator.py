import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

from word_analyzer import result_box


def calculate_difference():
    try:
        date1 = datetime.strptime(entry_date1.get(), "%Y-%m-%d")
        date2 = datetime.strptime(entry_date2.get(), "%Y-%m-%d")
        diff = abs((date2 - date1).days)
        result_label.config(text=f"اختلاف تاریخ ها : {diff} روز")
    except ValueError:
        messagebox.showerror("خطا", "لطفا تاریخ ها را به صورت YYYY-MM-DD وارد کنید")

def add_days():
    try:
        base_date = datetime.strptime(entry_base_date.get(), "%Y-%m-%d")
        days = int(entry_days.get())
        new_date = base_date + timedelta(days=days)
        result_label.config(text=f"تاریخ جدید : {new_date.strftime('%Y-%m-%d')}")
    except ValueError:
        messagebox.showerror("خظا", "فرمت تاریخ یا روز اشتباه است")


root = tk.Tk()
root.title("ماشین حساب تاریخ")
root.configure(bg="orange")
root.geometry("300x300")

tk.Label(root, text="تاریخ اول:(YYYY-MM-DD)").pack()
entry_date1 = tk.Entry(root)
entry_date1.pack()
tk.Label(root, text="تاریخ دوم:(YYYY-MM-DD)").pack()
entry_date2 = tk.Entry(root)
entry_date2.pack()

tk.Button(root, text="محاسبه اختلاف", command=calculate_difference).pack(pady=5)

tk.Label(root, text="تاریخ پایه:(YYYY-MM-DD)").pack()
entry_base_date = tk.Entry(root)
entry_base_date.pack()

tk.Label(root, text="تعداد روز").pack()
entry_days = tk.Entry(root)
entry_days.pack()

tk.Button(root, text="افزودن روز", command=add_days).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()