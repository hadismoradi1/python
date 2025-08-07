import tkinter
import tkinter as tk
from tkinter import ttk

def convert_length():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        units ={
            'متر(meter)':1,
            'کیلومتر(kilometer)':1000,
            'مایل(mile)':1609.34,
            'فوت(foot)':0.3048,
            'اینچ(inch)':0.0254
        }
        value_in_meters = value * units[from_unit]
        result = value_in_meters / units[to_unit]
        label_result.config(text=f"نتیجه: {round(result,4)} {to_unit}")
    except:
        label_result.config(text="لطفا عدد و واحد معتبر وارد کنید")


win = tk.Tk()
win.title("تبدیل واحد طول")
win.configure(bg="red")
win.geometry("400x300")

tk.Label(win, text="تبدیل واحد طول", font=("Arial",16)).pack(pady=5)
tk.Label(win, text="مقدار").pack()
entry_value = tk.Entry(win)
entry_value.pack(pady=5)

tk.Label(win, text="از واحد:").pack()
combo_from = ttk.Combobox(win, values=['متر(meter)','کیلومتر(kilometer)','مایل(mile)','فوت(foot)','اینچ(inch)'])
combo_from.pack(pady=5)
combo_from.current(0)

tk.Label(win, text="به واحد:").pack()
combo_to = ttk.Combobox(win, values=['متر(meter)','کیلومتر(kilometer)','مایل(mile)','فوت(foot)','اینچ(inch)'])
combo_to.pack(pady=5)
combo_to.current(0)

tk.Button(win, text="تبدیل", command=convert_length).pack(pady=10)

label_result = tk.Label(win, text="نتیجه", font=("Arial",12))
label_result.pack(pady=10)

win.mainloop()

