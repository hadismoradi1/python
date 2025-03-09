from tkinter import *


def mySum():
    result = int(txt1.get()) + int(txt2.get())
    lbl_result.config(text=result)

def myMinus():
    result = int(txt1.get()) - int(txt2.get())
    lbl_result.config(text=result)

def myMultiplication():
    result = int(txt1.get()) * int(txt2.get())
    lbl_result.config(text=result)

def myDivision():
    result = int(txt1.get()) / int(txt2.get())
    lbl_result.config(text=result)



win = Tk()
win.title('calculator')
win.geometry('300x300')



lbl1 = Label(win ,text='First Number')
lbl1.place(x=10,y=10)

txt1 = Entry(win)
txt1.place(x=110,y=10)

lbl2 = Label(win ,text='Second Number')
lbl2.place(x=10,y=50)

txt2 = Entry(win)
txt2.place(x=110,y=50)


btn_sum = Button(win , text="+" , command=mySum)
btn_sum.place(x=40,y=100)

btn_minus = Button(win , text="-" , command=myMinus)
btn_minus.place(x=60,y=100)

btn_multiplication = Button(win , text="*" , command=myMultiplication)
btn_multiplication.place(x=80,y=100)

btn_division = Button(win , text="/" , command=myDivision)
btn_division.place(x=100,y=100)

lbl_result = Label(win ,text='')
lbl_result.place(x=10,y=100)

win.mainloop()
