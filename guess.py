from tkinter import *
import random


class Guess:
    def __init__(self):
        self.error = 0
        self.systemnumber = random.randint(1, 100)
        self.win = Tk()
        self.win.title('guess number')
        self.win.geometry('300x300')
        self.win.configure(bg='pink')
        self.comment = Label(self.win, text='عددی بین 1 تا 100 وارد کنید')
        self.res = Label(self.win, text='')
        self.err = Label(self.win, text='')
        self.number = Entry(self.win)

        self.comment.pack()
        self.number.pack(pady=40)
        btn = Button(self.win, text='check', command=self.check)
        btn.pack()
        self.win.mainloop()



    def check(self):

        if self.error < 3:
            print(self.systemnumber, self.number.get())
            self.error +=1
            self.err.config(text=f'{self.error} خطا')
            self.err.pack(anchor=NE)
            if self.systemnumber == int(self.number.get()):
                self.res.config(text='موفق شدی')
            elif int(self.number.get()) > self.systemnumber:
                self.res.config(text='عدد کوچکتری وارد کنید')
            else:
                self.res.config(text='عدد بزرگتری وارد کنید')
        else:
            self.res.config(text=f'متاسفانه موفق نشدی عدد {self.systemnumber}بود')
            self.number.config()
        self.res.pack()


newGuess = Guess()


