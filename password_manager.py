import json
import os
import tkinter as tk
from tkinter import messagebox, END

VAULT_FILE = "vault.json"

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {}
    try:
        with open(VAULT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}

def save_vault(vault):
    with open(VAULT_FILE, "w", encoding="utf-8") as f:
        json.dump(vault, f, ensure_ascii=False, indent=2)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Manager (Basic)")
        self.vault = load_vault()

        # --- چپ: لیست سرویس‌ها + جستجو
        left = tk.Frame(root, padx=8, pady=8)
        left.grid(row=0, column=0, sticky="ns")
        tk.Label(left, text="🔎 جستجو:").pack(anchor="w")
        self.q = tk.Entry(left)
        self.q.pack(fill="x")
        self.q.bind("<KeyRelease>", self.filter_list)

        self.listbox = tk.Listbox(left, width=28, height=16)
        self.listbox.pack(pady=6, fill="both")
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        btns = tk.Frame(left)
        btns.pack(pady=4, fill="x")
        tk.Button(btns, text="➕ جدید/آپدیت", command=self.add_or_update).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(btns, text="🗑 حذف", command=self.delete_entry).pack(side="left", expand=True, fill="x", padx=2)

        # --- راست: فرم جزئیات
        right = tk.Frame(root, padx=8, pady=8)
        right.grid(row=0, column=1, sticky="nsew")
        root.grid_columnconfigure(1, weight=1)

        tk.Label(right, text="نام سرویس:").grid(row=0, column=0, sticky="w")
        self.e_service = tk.Entry(right)
        self.e_service.grid(row=0, column=1, sticky="ew", padx=4, pady=2)

        tk.Label(right, text="نام کاربری:").grid(row=1, column=0, sticky="w")
        self.e_username = tk.Entry(right)
        self.e_username.grid(row=1, column=1, sticky="ew", padx=4, pady=2)

        tk.Label(right, text="رمز عبور:").grid(row=2, column=0, sticky="w")
        self.e_password = tk.Entry(right, show="•")
        self.e_password.grid(row=2, column=1, sticky="ew", padx=4, pady=2)

        self.show_var = tk.BooleanVar(value=False)
        tk.Checkbutton(right, text="نمایش رمز", variable=self.show_var,
                       command=self.toggle_password).grid(row=2, column=2, padx=6)

        right.grid_columnconfigure(1, weight=1)

        tk.Button(right, text="💾 ذخیره دستی", command=self.save_now).grid(row=3, column=1, sticky="e", pady=8)

        self.refresh_list()

    # ---------- لیست ----------
    def refresh_list(self, items=None):
        self.listbox.delete(0, END)
        keys = sorted(items if items is not None else self.vault.keys(), key=str.lower)
        for k in keys:
            self.listbox.insert(END, k)

    def filter_list(self, _=None):
        text = self.q.get().strip().lower()
        if not text:
            self.refresh_list()
            return
        matches = [k for k in self.vault.keys() if text in k.lower()]
        self.refresh_list(matches)

    def on_select(self, _=None):
        if not self.listbox.curselection():
            return
        service = self.listbox.get(self.listbox.curselection()[0])
        creds = self.vault.get(service, {})
        self.e_service.delete(0, END); self.e_service.insert(0, service)
        self.e_username.delete(0, END); self.e_username.insert(0, creds.get("username",""))
        self.e_password.delete(0, END); self.e_password.insert(0, creds.get("password",""))

    # ---------- عملیات ----------
    def add_or_update(self):
        service = self.e_service.get().strip()
        username = self.e_username.get().strip()
        password = self.e_password.get().strip()

        if not service or not username or not password:
            messagebox.showwarning("خطا", "لطفاً همه فیلدها را پر کنید.")
            return

        self.vault[service] = {"username": username, "password": password}
        save_vault(self.vault)
        self.refresh_list()
        self.q.delete(0, END)
        messagebox.showinfo("موفق", f"اطلاعات «{service}» ذخیره شد.")

    def delete_entry(self):
        if self.listbox.curselection():
            service = self.listbox.get(self.listbox.curselection()[0])
        else:
            service = self.e_service.get().strip()
        if not service or service not in self.vault:
            messagebox.showwarning("توجه", "سرویسی برای حذف انتخاب/وارد نشده.")
            return
        if messagebox.askyesno("تایید حذف", f"حذف «{service}»؟"):
            del self.vault[service]
            save_vault(self.vault)
            self.refresh_list()
            self.e_service.delete(0, END)
            self.e_username.delete(0, END)
            self.e_password.delete(0, END)

    def toggle_password(self):
        self.e_password.config(show="" if self.show_var.get() else "•")

    def save_now(self):
        save_vault(self.vault)
        messagebox.showinfo("ذخیره", "فایل vault.json به‌روزرسانی شد.")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()