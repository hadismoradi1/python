def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


print("تبدیل گر دما")
print("1.فارنهایت -> سلسیوس")
print("2.سلسیوس -> فارنهایت")

choice = input("انتخاب شما 1 یا 2 ؟")
if choice == "1":
    c = float(input("دمای سلسیوس را وارد کنید"))
    f = celsius_to_fahrenheit(c)
    print(f"{c}C برابر است با {f:.2f}F")
elif choice == "2":
    f = float(input("دمای فارنهایت را وارد کنید"))
    c = fahrenheit_to_celsius(f)
    print(f"{f}F برابر است با {c:.2f}C")
else:
    print("گزینه نامعتبر است")
