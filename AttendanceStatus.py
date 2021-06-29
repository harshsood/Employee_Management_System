from tkinter import *
import datetime
date = datetime.datetime.now().date()
date = str(date)
import sqlite3
#we can code without using self in bottom cases
con = sqlite3.connect('db1.db')
cur = con.cursor()

class Attendance_Status(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("500x300+550+250")
        self.title('Attendance Status')
        self.resizable(False,False)

        self.login = 101

        #frame
        self.frame = Frame(self, height=300, bg='#ccdbfd')
        self.frame.pack(fill=X)

        #label and button

        query = cur.execute("SELECT attendance FROM Employee WHERE emp_id = ? ",(self.login,))
        data = query.fetchone()

        #date
        self.label_date = Label(self.frame, text="Date      " + date, font='arial 16 bold', fg='#e71d36', bg='#ccdbfd')
        self.label_date.place(x=40, y=40)

        #password
        self.label_record = Label(self.frame, text="Record", font='arial 16 bold', fg='#e71d36', bg='#ccdbfd')
        self.label_record.place(x=40, y=80)

        self.entry_record = Entry(self.frame, width=30, bd=4)
        self.entry_record.insert(0, data[0])
        self.entry_record.place(x=150, y=80)



