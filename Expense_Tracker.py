import tkinter as tk

expenses = []


def add_expense():
    try:
        amount = float(entry.get())
        expenses.append(amount)
        total = sum(expenses)
        result_label.config(text=f"مجموع هزینه ها :{total} تومان ")
        entry.delete(0, tk.END)
    except:
        result_label.config(text="لطفا فقط عدد وارد کنید!")


def reset_expenses():
    expenses.clear()
    result_label.config(text="مجموع هزینه ها : 0 تومان")


root = tk.Tk()
root.title("ماشین حساب هزینه ها")
root.configure(bg="dark blue")

label = tk.Label(root, text="مبلغ هزینه را وارد کنید", font=("Arial",14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="افزودن هزینه", font=("Arial", 12), command=add_expense)
add_btn.pack(pady=5)

reset_btn = tk.Button(root, text="ریست همه هزینه ها", font=("Arial", 12), command=reset_expenses)
reset_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()