import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

# ساخت پنجره
root = tk.Tk()
root.title("🎶 Music Player with Playlist")
root.geometry("500x300")
root.configure(bg="black")

# راه‌اندازی pygame
pygame.mixer.init()

playlist = []   # لیست موزیک‌ها
current_index = 0

# انتخاب چند موزیک
def load_music():
    global playlist
    files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    if files:
        for file in files:
            playlist.append(file)
            playlist_box.insert(tk.END, file.split("/")[-1])

# پخش موزیک
def play_music():
    global current_index
    if playlist:
        current_index = playlist_box.curselection()[0]
        song = playlist[current_index]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        song_label.config(text=song.split("/")[-1])
    else:
        messagebox.showwarning("Warning", "No songs in playlist!")

# توقف موقت
def pause_music():
    pygame.mixer.music.pause()

# ادامه دادن
def unpause_music():
    pygame.mixer.music.unpause()

# توقف کامل
def stop_music():
    pygame.mixer.music.stop()

# آهنگ بعدی
def next_music():
    global current_index
    if playlist:
        current_index = (current_index + 1) % len(playlist)
        song = playlist[current_index]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        song_label.config(text=song.split("/")[-1])

# آهنگ قبلی
def prev_music():
    global current_index
    if playlist:
        current_index = (current_index - 1) % len(playlist)
        song = playlist[current_index]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        song_label.config(text=song.split("/")[-1])

# لیبل نمایش آهنگ
song_label = tk.Label(root, text="No song loaded", font=("Arial", 12), bg="black", fg="white")
song_label.pack(pady=5)

# لیست پلی‌لیست
playlist_box = tk.Listbox(root, width=50, height=8)
playlist_box.pack(pady=10)

# دکمه‌ها
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack()

tk.Button(btn_frame, text="📂 Load", command=load_music).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="▶️ Play", command=play_music).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="⏸ Pause", command=pause_music).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="⏯ Unpause", command=unpause_music).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="⏹ Stop", command=stop_music).grid(row=0, column=4, padx=5)

tk.Button(btn_frame, text="⏮ Prev", command=prev_music).grid(row=1, column=1, pady=10)
tk.Button(btn_frame, text="⏭ Next", command=next_music).grid(row=1, column=3, pady=10)

root.mainloop()