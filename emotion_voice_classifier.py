from sys import prefix

import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from SoundMatch import features

dataset = {
    "happy1.wav" : "happy",
    "angry1.wav": "angry",
    "sad1.wav": "sad"
}
X_train = []
y_train = []

for file, label in dataset.items():
    y, sr = librosa.load(file)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    features = np.mean(mfccs.T, axis=0)
    X_train.append(features)
    y_train.append(label)
print("ویژگی ها برای دیتاست ساخته شد")

model = RandomForestClassifier()
model.fit(X_train, y_train)
print("مدل آموزش داده شد")

test_file = "test.wav"
y, sr = librosa.load(test_file)
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
features = np.mean(mfccs.T, axis=0)

prediction = model.predict([features])
print("احساس پیشبینی شده:", prediction[0])