import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

DATA_FILE = "habits.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_habit():
    habit = simpledialog.askstring("عادت جدید :", "اسم عادت جدید وارد کن")
    if habit:
        if habit not in data:
            data[habit] = []
            save_data(data)
            update_tree()
            messagebox.showinfo(f"عادت {habit} با موفقیت افزوده شد")
        else:
            messagebox.showwarning("هشدار این عادت قبلا ثبت شده")

def log_habit():
    selected = tree.selection()
    if selected:
        habit = tree.item(selected[0])['text']
        today = datetime.today().strftime("%Y-%m-%d")
        if today not in data[habit]:
            data[habit].append(today)
            save_data(data)
            update_tree()
            messagebox.showinfo(f"عادت {habit}برای امروز ثبت شد")
        else:
            messagebox.showwarning("هشدار این عادت قبلا ثبت شده")
    else:
        messagebox.showwarning("لطفا یک عادت انتخاب کنید")

def habit_status(habit, days):
    total_days = len(days)
    streak = 0
    sorted_days = sorted(days, reverse=True)
    today = datetime.today()
    for i, day in enumerate(sorted_days):
        day_date = datetime.strptime(day, "%Y-%m-%d")
        if (today - day_date).days == i:
            streak +=1
        else:
            break
    return f"تعداد کل : {total_days}, پشت سر هم {streak} روز"

def update_tree():
    for item in tree.get_children():
        tree.delete(item)
    for habit, days in data.items():
        tree.insert('', 'end', text=habit, values=(habit_status(habit, days),))



root = tk.Tk()
root.title("یاداور عادت روزانه")
root.geometry("500x400")

data = load_data()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="اضافه کردن عادت", command=add_habit)
btn_add.pack(side=tk.LEFT, padx=5)

btn_log = tk.Button(frame_buttons, text="ثبت عادت امروز", command=log_habit)
btn_log.pack(side=tk.LEFT, padx=5)

columns = ("وضعیت",)
tree = ttk.Treeview(root, columns=columns)
tree.heading("#0", text="عادت")
tree.heading("وضعیت", text="وضعیت")
tree.pack(expand=True, fill=tk.BOTH, pady=10, padx=10)

update_tree()
root.mainloop()



