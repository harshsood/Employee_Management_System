from tkinter import *
from tkinter import messagebox
import datetime
date = datetime.datetime.now().date()
date = str(date)
import sqlite3

con = sqlite3.connect('db1.db')
cur = con.cursor()

class form(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("700x600")
        self.title("Regularise Attendance")
        self.resizable(False, False)

        #labels and buttons

        #frames
        self.top = Frame(self, height=100, bg='White')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=600, bg='#283618')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text=" Regularisation Request ", font='TimesNewRoman 24 bold', bg='#606c38', fg='White')
        self.heading.place(x=140, y=40)

        #id
        self.label_id = Label(self.bottom, text="Employee ID", font='arial 12 bold', bg='#283618', fg='White')
        self.label_id.place(x=170, y=40)

        self.entry_id = Entry(self.bottom, width=30, bd=4)
        self.entry_id.insert(0, "Enter Employee ID")
        self.entry_id.place(x=310, y=40)

        #name
        self.label_name = Label(self.bottom, text="Name", font='arial 12 bold', bg='#283618', fg='White')
        self.label_name.place(x=170, y=80)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, "Enter Name")
        self.entry_name.place(x=310, y=80)

        #department
        self.label_dept = Label(self.bottom, text="Department", font='arial 12 bold', bg='#283618', fg='White')
        self.label_dept.place(x=170, y=120)

        self.entry_dept = Entry(self.bottom, width=30, bd=4)
        self.entry_dept.insert(0, "Enter Department")
        self.entry_dept.place(x=310, y=120)

        #Date of Application
        self.label_DOA = Label(self.bottom, text="Date of Application:  " + date, font='arial 12 bold', bg='#283618', fg='White')
        self.label_DOA.place(x=170, y=160)

        #reason
        self.label_reason = Label(self.bottom, text="Reason", font='arial 12 bold', bg='#283618', fg='White')
        self.label_reason.place(x=170, y=200)

        self.entry_reason = Entry(self.bottom, width=30, bd=4)
        self.entry_reason.insert(0, "Enter Reason")
        self.entry_reason.place(x=310, y=200)

        #Regularise Time
        self.label_time = Label(self.bottom, text="Time", font='arial 12 bold', bg='#283618', fg='White')
        self.label_time.place(x=170, y=240)

        self.entry_time = Entry(self.bottom, width=30, bd=4)
        self.entry_time.insert(0, "Enter Timings")
        self.entry_time.place(x=310, y=240)

        #button 1- Submit
        button = Button(self.bottom, text="Submit", font="arial 14 bold", bg="#1b4332", fg="White", command=self.request, bd=8, relief=GROOVE, width=14)
        button.place(x=220, y=350)
        #button 2- Cancel
        button = Button(self.bottom, text="Cancel", font="arial 14 bold", command=self.destroy, bg="#1b4332", fg="White", bd=8, relief=GROOVE, width=14)
        button.place(x=220, y=400)

    def request(self):
        emp_id = self.entry_id.get()
        name = self.entry_name.get()
        department = self.entry_dept.get()
        reason = self.entry_reason.get()
        status = "Pending"
        time = self.entry_time.get()

        if emp_id and name and department and reason and status and time != "":
            try:
                #add to database
                    query = "Insert into 'Leave' (emp_id,reason,status,time) values(?,?,?,?)"
                    cur.execute(query, (emp_id,reason,status,time))
                    con.commit()
                    messagebox.showinfo("Regularisation Form", "Request Applied")
                    self.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Fill all the fields", icon='warning')