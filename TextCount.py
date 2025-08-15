from collections import Counter

text = input("/nیک متن وارد کنید :")

clean_text = text.lower().strip()

words = clean_text.split()
word_count = len(words)

letter_count = len([ch for ch in clean_text if ch.isalpha()])

sentence_count = clean_text.count('.') + clean_text.count('!') + clean_text.count('?')

most_common_words = Counter(words).most_common(5)

print("/n امار متن")
print(f"تعداد کلمات:{word_count}")
print(f"تعداد حروف:{letter_count}")
print(f"تعداد جملات:{sentence_count}")
print("5 کلمه پرتکرار")
for word, freq in most_common_words:
    print(f":  {word}:  {freq} بار")