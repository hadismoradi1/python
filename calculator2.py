import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text=="=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END,"خطا")
    elif text=="C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("ماشین حساب")
root.geometry("300x400")
root.configure(bg="black")
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(root, bg="black")
    frame.pack()
    for btn in row:
        b = tk. Button(frame, text=btn, font="Arial 15", width=5, height=2)
        b.pack(side=tk.LEFT, padx=5,pady=5)
        b.bind("<Button-1>", click)
root.mainloop()