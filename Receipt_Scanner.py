import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import re

def open_receipt():
    filepath = filedialog.askopenfilename(title="انتخاب تصویر رسید", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    if filepath:
        try:
            img = Image.open(filepath)
            text = pytesseract.image_to_string(img, lang="eng")
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text.strip())
            numbers = re.findall(r"\d+(?:\.\d+)?", text)
            numbers = list(map(float, numbers)) if numbers else []

            total = sum(numbers)
            total_label.config(text=f"جمع کل:{total}")

        except Exception as e:
            messagebox.showerror("خطا", str(e))

root = tk.Tk()
root.title("اسکنر رسید")

btn = tk.Button(root, text="باز کردن رسید", command=open_receipt)
btn.pack(pady=10)

tk.Label(root, text="متن رسید").pack()
text_box = tk.Text(root, height=15, width=50)
text_box.pack(pady=5)

total_label = tk.Label(root, text="جمع کل: 0", font=("Arial", 14, "bold"))
total_label.pack(pady=10)

root.mainloop()
