import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("simple paint")
root.geometry("600x500")

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack(pady=20)

current_color = "black"
brush_size = 3


def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x - brush_size), (event.y - brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)


def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color


def change_brush(size):
    global brush_size
    brush_size = size


def clear_canvas():
    canvas.delete("all")


btn_frame = tk.Frame(root)
btn_frame.pack()

color_btn = tk.Button(btn_frame, text="Color", command=choose_color)
color_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_canvas)
clear_btn.grid(row=0, column=1, padx=10)

small_btn = tk.Button(btn_frame, text="Small", command=lambda:
change_brush(2))
small_btn.grid(row=0, column=2, padx=5)

medium_btn = tk.Button(btn_frame, text="Medium", command=lambda:
change_brush(5))
medium_btn.grid(row=0, column=3, padx=5)

large_btn = tk.Button(btn_frame, text="Large", command=lambda:
change_brush(10))
large_btn.grid(row=0, column=4, padx=5)

canvas.bind("<B1-Motion>", paint)
root.mainloop()
