import mysql.connector
from tkinter import *


def search():
    mdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='shop_db1'
    )

    con = mdb.cursor()
    name = name_entry.get()
    lbl_search.config(text=name)

    sql_statement = 'select * from user where name=%s'
    con.execute(sql_statement, (name,))
    r = con.fetchall()

    print(r)




win = Tk()
win.geometry("300x300")
win.title('search')
name_entry = Entry(win)
name_entry.place(x=70, y=100)

lbl_search = Label(win, text="",)
lbl_search.place(x=100, y=170)

search_btn = Button(win, text="search", command=search)
search_btn.place(x=200, y=100)


win.mainloop()




