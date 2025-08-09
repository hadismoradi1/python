import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

gender = input("صدای مرد یا زن؟(m/f)").lower()
engine.setProperty('voice', voices[0].id
if gender=='m' else voices[1].id)

text = input("متن خود را وارد کنید:")

engine.say(text)
engine.runAndWait()

if input('ذخیره به mp3? (y/n)').lower()=='y':
    engine.save_to_file(text, "output.mp3")
    engine.runAndWait()
    print("output.mp3 ذخیره شد")