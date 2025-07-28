from tkinter import *
import mysql.connector


def search():
    mdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='phone'
    )

    con = mdb.cursor()
    name = name_entry.get()
    number = number_entry.get()
    lbl_number.config(text=number)
    lbl_name.config(text=name)
    myval = (name, number)
    sql_statement = 'select * from list where name=%s AND number=%s'
    con.execute(sql_statement, myval)
    r = con.fetchall()
    print(r)


def insert():
    mdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='phone'
    )

    con = mdb.cursor()
    number = number_entry.get()
    name = name_entry.get()
    image = image_entry.get()

    lbl_number.config(text=number)
    lbl_name.config(text=name)
    lbl_image.config(text=image)
    myval = (number, name, image)
    sql_statement = 'insert into list(number,name,image) value (%s,%s,%s)'
    con.execute(sql_statement, myval)
    mdb.commit()
    print('مخاطب با موفقیت اضافه شد')


def delete():
    mdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='phone'
    )

    con = mdb.cursor()
    number = number_entry.get()
    lbl_number.config(text=number)
    sql_statement = 'delete from list where number=%s'
    myval = (number,)
    con.execute(sql_statement, myval)
    mdb.commit()
    print('مخاطب حذف شد')

def update():
    mdb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='phone'
    )

    con = mdb.cursor()

    number = number_entry.get()
    name = name_entry.get()
    image = image_entry.get()

    lbl_number.config(text=number)
    lbl_name.config(text=name)
    lbl_image.config(text=image)
    sql_statement = 'update list set name=%s,image=%s where number=%s'
    myval = (name, image, number)
    con.execute(sql_statement, myval)
    mdb.commit()
    print('اطلاعات اپدیت شد')
    mdb.close()


win = Tk()
win.geometry("350x350")
win.title('phone_list')
win.configure(bg='pink')

number_entry = Entry(win)
number_entry.place(x=70, y=70)

name_entry = Entry(win)
name_entry.place(x=70, y=120)

image_entry = Entry(win)
image_entry.place(x=70, y=170)

number = Label(win, text="number", )
number.place(x=20, y=70)

name = Label(win, text="name", )
name.place(x=20, y=120)

image = Label(win, text="image", )
image.place(x=20, y=170)

lbl_number = Label(win, text="", )
lbl_number.place(x=210, y=70)

lbl_name = Label(win, text="", )
lbl_name.place(x=210, y=120)

lbl_image = Label(win, text="", )
lbl_image.place(x=210, y=170)

search_btn = Button(win, text="search", command=search)
search_btn.place(x=50, y=250)

insert_btn = Button(win, text="insert", command=insert)
insert_btn.place(x=110, y=250)

update_btn = Button(win, text="update", command=update)
update_btn.place(x=160, y=250)

delete_btn = Button(win, text="delete", command=delete)
delete_btn.place(x=220, y=250)

win.mainloop()
