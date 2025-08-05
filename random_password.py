from tkinter import *
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("طول رمزعبور", "هشدار.حداقل باید 4 باشد")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("لطفا", "خطا.یک عدد صحیحی وارد کنید")


win = Tk()
win.configure(bg = "gray")
win.title("تولیدکننده رمزعبور")
win.geometry("400x200")
win.resizable(False, False)

lbl = Label(win, text="طول رمزعبور:")
lbl.pack(pady=5)
length_entry = Entry(win, justify="center")
length_entry.pack()
btn = Button(win, text="تولید رمزعبور", command=generate_password)
btn.pack(pady=10)
lbl1 = Label(win, text="رمز عبور تولید شده:")
lbl1.pack()
result_entry = Entry(win, justify="center", width=40)
result_entry.pack(pady=5)

win.mainloop()
