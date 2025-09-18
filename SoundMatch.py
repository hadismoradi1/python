import librosa
import numpy as np
import sounddevice as sd
import scipy.spatial.distance as dist
import os
from tkinter import Tk, filedialog

def recoed_audio(filename="recorded.wav", duration=5, sr=22050):
    print("در حال ضبط صدا...")
    audio = sd.rec(int(duration * sr), samplerate=sr, channels=1)
    sd.wait()
    librosa.output.write_wav(filename, audio.flatten(), sr)
    print("ضبط تمام شد و ذخیره شد", filename)
    return filename

def choose_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="یک فایل صوتی انتخاب کن",
        filetypes=[("Audio Files", "*.wav *.mp3")]
    )
    return file_path

def extract_features(file_path):
    y, sr = librosa.load(file_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    return np.mean(mfcc, axis=1)

database = {
    "song1.wav": "آهنگ شماره 1",
    "song2.wav": "آهنگ شماره 2",
    "song3.wav": "آهنگ شماره 3",
}

db_features = {}
for file, name in database.items():
    if os.path.exists(file):
        db_features[name] = extract_features(file)

print("1. ضبط صدا")
print("2. انتخاب فایل صوتی")
choice = input("کدومو میخوای (1 یا 2)")

if choice == "1":
    test_file = recoed_audio(duration=5)
elif choice == "2":
    test_file = choose_file()
else:
    print("انتخاب نامعتبر!")
    exit()

test_features = extract_features(test_file)
results = {}
for name, features in db_features.items():
    distance = dist.euclidean(test_features, features)
    results[name] = distance

closest_match = min(results, key=results.get)
print("نزدیک ترین اهنگ:", closest_match)
