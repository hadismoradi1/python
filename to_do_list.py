from tkinter import *
import mysql.connector


def search():
    mdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='do_list'
    )
    con = mdb.cursor()
    sql_statement = 'select * from list'
    con.execute(sql_statement,)
    r = con.fetchall()
    print(r)


def add():
    mdb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="do_list"
    )
    con = mdb.cursor()
    lists = list_entry.get()
    sql_statement = 'insert into list(list_name) value (%s)'
    myvalue = (lists,)
    con.execute(sql_statement, myvalue)
    mdb.commit()
    print(f'{lists} به لیست اضافه شد')


win = Tk()
win.configure(bg='light blue')
win.geometry("400x300")
win.title("do list")

lbl_list = Label(win, text="enter your list to do")
lbl_list.place(x=150, y=50)

list_entry = Entry(win)
list_entry.place(x=140, y=100)

list_btn = Button(win, text="add list", command=add)
list_btn.place(x=130, y=150)

show_btn = Button(win, text="show list", command=search)
show_btn.place(x=230, y=150)

win.mainloop()