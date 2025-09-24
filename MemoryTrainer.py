import tkinter as tk
import random
from tkinter import messagebox

# ------------------ تنظیمات ------------------
FLASH_DELAY = 500     # میلی‌ثانیه: زمان چشمک زدن یک دکمه
PAUSE_BETWEEN = 250   # میلی‌ثانیه: فاصله بین نمایش‌های پشت سر هم
# ----------------------------------------------


class MemoryTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("MemoryTrainer 🧠")
        self.root.resizable(False, False)

        # حالت بازی
        self.sequence = []       # دنباله‌ی تولیدشده
        self.user_input = []     # ورودی کاربر
        self.level = 0
        self.is_playing = False  # آیا برنامه در حال پخش دنباله است؟
        self.buttons = {}
        self.colors = [("green", "#2ecc71"), ("red", "#e74c3c"),
                       ("yellow", "#f1c40f"), ("blue", "#3498db")]

        # بالای پنجره: عنوان و نشانگر مرحله
        top_frame = tk.Frame(root)
        top_frame.pack(padx=10, pady=(10, 0))
        tk.Label(top_frame, text="MemoryTrainer", font=("Arial", 18, "bold")).pack()
        self.level_label = tk.Label(top_frame, text="مرحله: 0", font=("Arial", 12))
        self.level_label.pack()

        # وسط: 2x2 دکمه رنگی
        grid_frame = tk.Frame(root)
        grid_frame.pack(padx=10, pady=10)

        # ساخت دکمه‌ها
        # موقعیت‌ها: (0,0)=green, (0,1)=red, (1,0)=yellow, (1,1)=blue
        positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for (name, hexcol), pos in zip(self.colors, positions):
            btn = tk.Button(grid_frame,
                            bg=hexcol,
                            activebackground=hexcol,
                            width=12, height=6,
                            command=lambda n=name: self.on_user_click(n))
            btn.grid(row=pos[0], column=pos[1], padx=6, pady=6)
            self.buttons[name] = btn

        # پایین: کنترل‌ها
        control_frame = tk.Frame(root)
        control_frame.pack(padx=10, pady=(0, 10), fill="x")

        self.start_btn = tk.Button(control_frame, text="شروع بازی", command=self.start_game, bg="#27ae60", fg="white")
        self.start_btn.pack(side="left", padx=6)

        self.strict_var = tk.BooleanVar(value=False)
        self.strict_check = tk.Checkbutton(control_frame, text="حالت سخت (با اشتباه پایان)", variable=self.strict_var)
        self.strict_check.pack(side="left", padx=6)

        self.restart_btn = tk.Button(control_frame, text="ریست", command=self.reset_game)
        self.restart_btn.pack(side="right", padx=6)

        # نمایش پیشرفت کوتاه
        self.status_label = tk.Label(root, text="آماده‌ای؟ روی «شروع بازی» بزن!", font=("Arial", 10), fg="gray")
        self.status_label.pack(pady=(0, 8))

    # --------------- منطق بازی ---------------
    def start_game(self):
        if self.is_playing:
            return
        self.reset_game(state_only=True)
        self.add_step()
        self.play_sequence()

    def reset_game(self, state_only=False):
        """حالت بازی رو ریست کن. اگر state_only=True فقط مقادیر بدون پاک کردن UI"""
        self.sequence = []
        self.user_input = []
        self.level = 0
        self.level_label.config(text=f"مرحله: {self.level}")
        self.status_label.config(text="بازی ریست شد.")
        if not state_only:
            self.is_playing = False

    def add_step(self):
        """یک رنگ تصادفی به دنباله اضافه می‌کند و سطح را افزایش می‌دهد."""
        color_name = random.choice([c[0] for c in self.colors])
        self.sequence.append(color_name)
        self.level += 1
        self.level_label.config(text=f"مرحله: {self.level}")

    def play_sequence(self):
        """شروع به پخش دنباله می‌کند (چشمک زدن دکمه‌ها)."""
        if not self.sequence:
            return
        self.is_playing = True
        self.user_input = []
        self.status_label.config(text="در حال نمایش دنباله—دقت کن و بعد تکرار کن.")
        self._play_index = 0
        self.root.after(PAUSE_BETWEEN, self._flash_next)

    def _flash_next(self):
        if self._play_index >= len(self.sequence):
            # اتمام پخش
            self.is_playing = False
            self.status_label.config(text="حالا نوبت توست! دنباله را تکرار کن.")
            return
        color = self.sequence[self._play_index]
        self._flash_button(color, FLASH_DELAY)
        self._play_index += 1
        # زمان‌بندی برای نمایش بعدی بعد از PAUSE_BETWEEN + FLASH_DELAY
        self.root.after(FLASH_DELAY + PAUSE_BETWEEN, self._flash_next)

    def _flash_button(self, color_name, duration):
        """ظاهر دکمه را برای مدت کوتاهی تغییر می‌دهد تا چشمک بزند."""
        btn = self.buttons[color_name]
        orig = btn.cget("bg")
        # نورانی‌تر کردن (می‌تونیم از سفید به عنوان هایلایت استفاده کنیم)
        btn.config(bg="white")
        self.root.update()
        self.root.after(duration, lambda: btn.config(bg=orig))

    def on_user_click(self, color_name):
        """وقتی کاربر کلیک می‌کند، این اجرا می‌شود."""
        if self.is_playing:
            # اگر برنامه هنوز دنباله را پخش می‌کند، کلیک را قبول نکن
            return
        # چشمک کوچک برای بازخورد
        self._flash_button(color_name, 120)

        self.user_input.append(color_name)
        idx = len(self.user_input) - 1
        # بررسی در همان لحظه
        if self.user_input[idx] != self.sequence[idx]:
            # اشتباه شد
            self.status_label.config(text="اشتباه! 😕")
            if self.strict_var.get():
                messagebox.showinfo("پایان بازی", f"اشتباه کردی. سطحی که رسیدی: {self.level}")
                self.reset_game()
            else:
                # در حالت عادی، دوباره پخش می‌کنیم اجازه امتحان دوباره
                self.status_label.config(text="اشتباه شد، دوباره امتحان کن—دنباله نمایش داده می‌شود.")
                self.root.after(800, self.play_sequence)
            return

        # اگر تا اینجا همه درست بود
        if len(self.user_input) == len(self.sequence):
            # مرحله با موفقیت سپری شد
            self.status_label.config(text="آفرین! مرحله بعدی آماده است 🎉")
            # کمی تاخیر و سپس مرحله بعد
            self.root.after(800, lambda: (self.add_step(), self.play_sequence()))

    # --------------- پایان کلاس ---------------


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryTrainer(root)
    root.mainloop()