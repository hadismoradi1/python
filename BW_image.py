
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("تبدیل عکس به سیاه و سفید")
        self.root.geometry("600x500")
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)
        self.btn_select = tk.Button(root, text="انتخاب عکس", command=self.select_image)
        self.btn_select.pack(pady=5)
        self.btn_convert = tk.Button(root, text="تبدیل به سیاه و سفید", command=self.convert_image, state=tk.DISABLED)
        self.btn_convert.pack(pady=5)
        self.btn_save = tk.Button(root, text="ذخیره تصویر", command=self.save_image, state=tk.DISABLED)
        self.btn_save.pack(pady=5)
        self.original_image = None
        self.bw_image = None
    def select_image(self):
        file_path = filedialog.askopenfilename( filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp *.gif")] )
        if file_path:
            self.original_image = Image.open(file_path)
            img_resized = self.original_image.resize((400, 300))
            self.tk_image = ImageTk.PhotoImage(img_resized)
            self.image_label.config(image=self.tk_image)
            self.btn_convert.config(state=tk.NORMAL)
    def convert_image(self):
        if self.original_image:
            self.bw_image = self.original_image.convert("L")
            img_resized = self.bw_image.resize((400, 300))
            self.tk_image_bw = ImageTk.PhotoImage(img_resized)
            self.image_label.config(image=self.tk_image_bw)
            self.btn_save.config(state=tk.NORMAL)
    def save_image(self):
        if self.bw_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
            if save_path:
                self.bw_image.save(save_path)
                messagebox.showinfo("ذخیره شد", "تصویر با موفقیت ذخیره شد!")
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="light blue")
    app = ImageConverterApp(root)
    root.mainloop()