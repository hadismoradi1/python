import tkinter as tk
import random

choices = ["سنگ", "کاغذ", "قیچی"]

def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""
    if user_choice == computer_choice:
        result = "برابر شد! 😐"
    elif (user_choice == "سنگ" and computer_choice == "قیچی") or \
         (user_choice == "کاغذ" and computer_choice == "سنگ") or \
         (user_choice == "قیچی" and computer_choice == "کاغذ"):
        result = "شما بردید! 🎉"
    else:
        result = "کامپیوتر برد! 🤖"

    lbl_result.config(text=f"شما: {user_choice} | کامپیوتر: {computer_choice}\n{result}")

root = tk.Tk()
root.title("بازی سنگ، کاغذ، قیچی")
root.geometry("350x300")
root.configure(bg="black")
lbl_title = tk.Label(root, text="سنگ، کاغذ، قیچی", font=("Arial", 20), bg="cyan")
lbl_title.pack(pady=10)

frame_buttons = tk.Frame(root, bg="black")
frame_buttons.pack()

btn_rock = tk.Button(frame_buttons, text="✊ سنگ", font=("Arial", 14), bg="cyan", command=lambda: play("سنگ"))
btn_paper = tk.Button(frame_buttons, text="🖐 کاغذ", font=("Arial", 14), bg="cyan", command=lambda: play("کاغذ"))
btn_scissors = tk.Button(frame_buttons, text="✂️ قیچی", font=("Arial", 14), bg="cyan", command=lambda: play("قیچی"))

btn_rock.grid(row=0, column=0, padx=5, pady=5)
btn_paper.grid(row=0, column=1, padx=5, pady=5)
btn_scissors.grid(row=0, column=2, padx=5, pady=5)

lbl_result = tk.Label(root, text="", font=("Arial", 14), fg="black", bg="cyan")
lbl_result.pack(pady=20)

root.mainloop()