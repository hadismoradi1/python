import tkinter as tk
from tkinter import messagebox

students = {}

def add_student():
    name = entry_name.get()
    grade = entry_grade.get()

    if name == "" or grade == "" :
        messagebox.showwarning("خطا", "نام و نمره را وارد کنید")
        return

    try:
        grade = float(grade)
        students[name] = grade
        listbox.insert(tk.END, f"{name}:{grade}")
        entry_name.delete(0, tk.END)
        entry_grade.delete(0, tk.END)
    except:
        messagebox.showerror("خطا", "نمره باید عدد باشد")

def show_average():
    if not students:
        messagebox.showinfo("میانگین هیچ دانش اموزی ثبت نشده")
    else:
        avg = sum(students.values()) / len(students)
        messagebox.showinfo("میانگین نمرات", f"{avg:.2f}")

def show_best_worst():
    if not students:
        messagebox.showinfo("میانگین هیچ دانش اموزی ثبت نشده")
    else:
        best = max(students, key=students.get)
        worst = min(students, key=students.get)
        messagebox.showinfo("نتیجه", f"بیشترین نمره: {best}  {students[best]}\n"
        f"کمترین نمره: {worst}   {students[worst]}")

root = tk.Tk()
root.title("مدیریت نمرات دانش اموزان")

tk.Label(root, text="نام دانش امور:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="نمره").pack()
entry_grade = tk.Entry(root)
entry_grade.pack()

tk.Button(root, text="اضافه کردن", command=add_student).pack(pady=5)
tk.Button(root, text="میانگین نمرات", command=show_average).pack(pady=5)
tk.Button(root, text="بیشترین/کمترین نمره", command=show_best_worst).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

root.mainloop()