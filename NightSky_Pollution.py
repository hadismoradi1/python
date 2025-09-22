import cv2
import numpy as np
from tkinter import Tk, filedialog, Label, Button, messagebox
from PIL import Image, ImageTk

def analyze_sky(image_path):
    # خواندن تصویر
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # تار کردن برای حذف نویز
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    # تشخیص نقاط روشن (ستاره‌ها)
    _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

    # پیدا کردن کانتورهای نقاط روشن
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    stars_count = len(contours)

    # میانگین روشنایی
    brightness = np.mean(img)

    # تحلیل ساده
    if stars_count > 100 and brightness < 50:
        status = "آسمان تاریک و عالی ⭐"
    elif 50 < stars_count < 100 and brightness < 100:
        status = "آسمان نیمه آلوده 🌌"
    else:
        status = "آلودگی نوری زیاد 😢"

    return stars_count, int(brightness), status

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return

    stars, brightness, status = analyze_sky(file_path)

    # نمایش نتایج
    messagebox.showinfo("نتیجه تحلیل",
                        f"تعداد ستاره‌ها: {stars}\n"
                        f"میانگین روشنایی: {brightness}\n"
                        f"وضعیت: {status}")

    # نمایش تصویر انتخابی در GUI
    img = Image.open(file_path)
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    panel.config(image=img_tk)
    panel.image = img_tk

# ساخت پنجره اصلی
root = Tk()
root.title("🌌 NightSky Pollution Detector")

Label(root, text="انتخاب عکس آسمان شب برای تحلیل آلودگی نوری", font=("Arial", 12)).pack(pady=10)

Button(root, text="انتخاب تصویر", command=select_image, font=("Arial", 12), bg="blue", fg="white").pack(pady=5)

panel = Label(root)
panel.pack(pady=10)

root.mainloop()