import cv2
import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera App")
        self.video = cv2.VideoCapture(0)

        self.canvas = Label(root)

        self.canvas.pack()

        self.btn_capture = Button(root, text="گرفتن عکس", command=self.capture)
        self.btn_capture.pack(pady=10)
        self.btn_exit = Button(root, text="خروج", command=self.quit_app)
        self.btn_exit.pack(pady=5)

        self.update_frame()

    def update_frame(self):
        ret, frame = self.video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.imgtk = imgtk

            self.canvas.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def capture(self):
        ret, frame = self.video.read()
        if ret:
            filename = "photo.jpg"
            cv2.imwrite(filename, frame)
            print(f"عکس ذخیره شد : {filename}")

    def quit_app(self):
        self.video.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()
