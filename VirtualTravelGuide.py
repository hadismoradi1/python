import tkinter as tk
from tkinter import messagebox

travel_data = {
    "ایران":{
        "فارسی" : "زبان",
        "ریال": "واحد پول",
        "کباب _ قرمه سبزی _ فسنجان ": "غذا های معروف",
        "به ایران خوش آمدید": "خوشامدگویی"
    },
    "ژاپن":{
        "ژاپنی": "زبان",
        "ین": "واحد پول",
        "سوشی _ رامن _ تمپورا": "غذا های معروف",
        "به ژاپن خوش آمدید": "خوشامدگویی"
    },
    "فرانسه":{
        "فرانسوی": "زبان",
        "یورو": "واحد پول",
        "بگت _ کروسان _ پنیر": "غذا های معروف",
        "به فرانسه خوش آمدید": "خوشامدگویی"
    },
    "ترکیه":{
        "ترکی استانبولی": "زبان",
        "لیر": "واحد پول",
        "کباب - باقلوا _ دونر": "غذا های معروف",
        "به ترکیه خوش  آمدید": "خوشامدگویی"
    }
}

def search_country():
    country = entry.get().strip().lower()
    if country in travel_data:
        info = travel_data[country]
        result = f"""
        کشور : {country}
        زبان : {info['زبان']}
        واحد پول : {info['واحد پول']}
        غذا های معروف : {info['غذا های معروف']}
         {info['خوشامدگویی']}
    """
        messagebox.showinfo("اطلاعات سفر", result)
    else:
        messagebox.showwarning("خظا", "کشور مورد نظر در لیست وجود ندارد")


root = tk.Tk()
root.title("راهنمای سفر مجازی")
root.geometry("400x250")

label = tk.Label(root, text="نام کشور را وارد کنید:", font=("Tahoma", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Tahoma", 12))
entry.pack(pady=5)

search_btn = tk.Button(root, text="جستجو", command=search_country, font=("Tahoma", 12), bg="light blue")
search_btn.pack(pady=10)

root.mainloop()

