import tkinter as tk
from tkinter import filedialog, messagebox


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("success", "file saved successfully!")


def exit_file():
    window.destroy()


window = tk.Tk()
window.title('notepad')
window.geometry("600x400")

text_area = tk.Text(window)
text_area.pack(expand=True, fill='both')

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

open_button = tk.Button(button_frame, text="open", command=open_file, width=10)
open_button.pack(side='left', padx=10)

save_button = tk.Button(button_frame, text="save", command=save_file, width=10)
save_button.pack(side='left', padx=10)

exit_button = tk.Button(button_frame, text="exit", command=exit_file, width=10)
exit_button.pack(side='left', padx=10)

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="open", command=open_file)
file_menu.add_command(label="save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="exit", command=exit_file)

menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

window.mainloop()
