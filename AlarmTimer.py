import tkinter as tk

seconds = 0
running = False

def start_timer():
    global seconds, running
    try:
        seconds = int(entry.get())
        running = True
        countdown()
    except:
        label.config(text="⛔ لطفاً عدد درست وارد کن!")

def countdown():
    global seconds, running
    if running and seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        label.config(text=timer)
        seconds -= 1
        root.after(1000, countdown)
    elif seconds < 0:
        label.config(text="⏰ Time's Up!")

def pause_timer():
    global running
    running = False

def resume_timer():
    global running
    if not running and seconds > 0:
        running = True
        countdown()

def reset_timer():
    global running, seconds
    running = False
    seconds = 0
    label.config(text="00:00")
    entry.delete(0, tk.END)

# پنجره اصلی
root = tk.Tk()
root.title("⏳ تایمر پیشرفته")
root.configure(bg="black")

label = tk.Label(root, text="00:00", font=("Arial", 36), fg="red", bg="black")
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16), bg="gray")
entry.pack(pady=10)

frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

start_btn = tk.Button(frame, text="Start", font=("Arial", 12), bg="gray", command=start_timer)
start_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(frame, text="Pause", font=("Arial", 12), bg="gray", command=pause_timer)
pause_btn.grid(row=0, column=1, padx=5)

resume_btn = tk.Button(frame, text="Resume", font=("Arial", 12), bg="gray", command=resume_timer)
resume_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(frame, text="Reset", font=("Arial", 12), bg="gray", command=reset_timer)
reset_btn.grid(row=0, column=3, padx=5)

root.mainloop()