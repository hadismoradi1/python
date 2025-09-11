import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from collections import Counter
import re

def open_file():
    filepath = filedialog.askopenfilename(
        title = "انتخاب فایل متنی",
        filetypes = [("txt files", "*.txt")]
    )
    if not filepath:
        return

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        words = re.findall(r'\b\w+\b', text.lower())
        if not words:
            messagebox.showinfo("اطلاعات هیچ کلمه ای پیدا نشد")
            return

        counter = Counter(words)
        most_common = counter.most_common()

        result_box.delete(1.0, tk.END)
        for word, count in most_common:
            result_box.insert(tk.END, f"{word}: {count}\n")

        plt.figure(figsize=(8, 5))
        plt.bar([w for w, c in most_common], [c for w, c in most_common])
        plt.title("Top 10 words frequency")
        plt.xlabel("Words")
        plt.ylabel("Count")
        plt.show()

    except Exception as e:
        messagebox.showerror("خطا",str(e))

root = tk.Tk()
root.title("تحلیل متن و کلمات پرتکرار")

btn = tk.Button(root, text="باز کردن فایل",command=open_file)
btn.pack(pady=10)

result_box = tk.Text(root, height=15, width=50)
result_box.pack(pady=5)

root.mainloop()