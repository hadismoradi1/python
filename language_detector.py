from langdetect import detect, detect_langs

print("Language Detector")
print("برای خروج 'exit' بنویسید")

while True:
    text = input("متن را وارد کنید: ")
    if text.lower() == "exit":
        break
    try:
        lang = detect(text)
        langs = detect_langs(text)
        print(f"زبان اصلی : {lang}")
        print(f"زبان فرعی : {langs}")
    except:
        print("متن خیلی کوتاه یا نامشخص بود \n")