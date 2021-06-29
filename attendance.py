from tkinter import *
from AttendanceStatus import Attendance_Status
import sqlite3
#we can code without using self in bottom cases
con = sqlite3.connect('db1.db')
cur = con.cursor()

class attendance(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("500x300+550+250")
        self.title('View Attendance')
        self.resizable(False,False)

        #frame
        self.frame = Frame(self, height=300, bg='#ccdbfd')
        self.frame.pack(fill=X)

        #label and button

        #id
        self.label_id = Label(self.frame, text="Employee ID ", font='arial 16 bold', fg='#e71d36', bg='#ccdbfd')
        self.label_id.place(x=20, y=40)

        self.entry_id = Entry(self.frame, width=30, bd=4)
        self.entry_id.insert(0, "Enter Employee ID")
        self.entry_id.place(x=150, y=40)

        #password
        self.label_password = Label(self.frame, text="Password ", font='arial 16 bold', fg='#e71d36', bg='#ccdbfd')
        self.label_password.place(x=40, y=80)

        self.entry_password = Entry(self.frame, width=30, bd=4)
        self.entry_password.insert(0, "Enter Password")
        self.entry_password.config(show="*")
        self.entry_password.place(x=150, y=80)

        #button
        button = Button(self.frame, text="OK", font="arial 12 bold", command=self.attendancestatus)
        button.place(x=215, y=200)

    def attendancestatus(self):
        window = Attendance_Status()
