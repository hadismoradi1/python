from tkinter import *
import requests

API_KEY ="b1a7f524721f1b215037974a9bbc1830"


def get_weather():
    city = city_entry.get()
    url = (f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fa")

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            result_lbl.config(text="شهر پیدا نشد")
            return
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        result = f"""وضعیت city:
        دمای هوا:{temp}
        اسمان:{description}
        رطوبت:{humidity}
        باد:{wind} m/s"""

        result_lbl.config(text=result)
    except:

        result_lbl.config(text="خطا در دریافت اطلاعات")


win = Tk()
win.geometry('400x400')
win.configure(bg='light green')
win.title('وضعیت اب و هوا')
lbl = Label(win, text="نام شهر را وارد کنید")
lbl.place(x=150, y=50)
city_entry = Entry(win)
city_entry.place(x=150, y=100)
show_btn = Button(win, text='نمایش وضعیت', command=get_weather)
show_btn.place(x=150, y=150)
result_lbl = Label(win, text="", justify="right")
result_lbl.place(x=150, y=200)

win.mainloop()
