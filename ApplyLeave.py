from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import datetime
date = datetime.datetime.now().date()
date = str(date)
import sqlite3

con = sqlite3.connect('db1.db')
cur = con.cursor()

class Submit_Leave(Toplevel):
    def __init__(self, emp_id):
        Toplevel.__init__(self)

        self.geometry("700x600")
        self.title("Leave Application")
        self.resizable(False, False)

        self.login = emp_id

        #labels and buttons

        #frames
        self.top = Frame(self, height=100, bg='White')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=600, bg='#006d77')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text=" Application Form ", font='TimesNewRoman 24 bold', bg='#0077b6', fg='White')
        self.heading.place(x=230, y=40)


        query = cur.execute("SELECT emp_id, name, department FROM Employee WHERE emp_id = ? ",(self.login,))
        data = query.fetchone()

        #id
        self.label_id = Label(self.bottom, text="Employee ID", font='arial 12 bold', bg='#006d77', fg='White')
        self.label_id.place(x=60, y=40)

        self.entry_id = Entry(self.bottom, width=30, bd=4)
        self.entry_id.insert(0, data[0])
        self.entry_id.place(x=210, y=40)

        #name
        self.label_name = Label(self.bottom, text="Name", font='arial 12 bold', bg='#006d77', fg='White')
        self.label_name.place(x=60, y=80)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, data[1])
        self.entry_name.place(x=210, y=80)

        #department
        self.label_dept = Label(self.bottom, text="Department", font='arial 12 bold', bg='#006d77', fg='White')
        self.label_dept.place(x=60, y=120)

        self.entry_dept = Entry(self.bottom, width=30, bd=4)
        self.entry_dept.insert(0, data[2])
        self.entry_dept.place(x=210, y=120)

        #Date of Application
        self.label_DOA = Label(self.bottom, text="Date of Application:  " + date, font='arial 12 bold', bg='#006d77', fg='White')
        self.label_DOA.place(x=60, y=160)

        #date1
        self.label_date1 = Label(self.bottom, text="Date1(Start)", font='arial 12 bold', bg='#006d77', fg='White')
        self.label_date1.place(x=60, y=200)

        self.entry_date1 = Entry(self.bottom, width=30, bd=4)
        self.entry_date1.insert(0, "Enter Date")
        self.entry_date1.place(x=210, y=200)

        #date2
        self.label_date2 = Label(self.bottom, text="Date2(End)", font='arial 12 bold', bg='#006d77', fg='White')
        self.label_date2.place(x=60, y=240)

        self.entry_date2 = Entry(self.bottom, width=30, bd=4)
        self.entry_date2.insert(0, "Enter Date")
        self.entry_date2.place(x=210, y=240)

        # Duration of Leave
        self.label_duration = Label(self.bottom, text="Duration of Leave", font='arial 12 bold', bg='#006d77', fg='White')
        self.label_duration.place(x=60, y=280)

        self.entry_duration = Entry(self.bottom, width=30, bd=4)
        self.entry_duration.insert(0, "Enter Duration")
        self.entry_duration.place(x=210, y=280)

        #Type of Leave
        self.label_type = Label(self.bottom, text="Type of Leave", font='arial 12 bold', bg='#006d77', fg='White')
        self.label_type.place(x=60, y=320)

        #Combobox creation
        n = tk.StringVar()
        self.entry_type = ttk.Combobox(self.bottom, width=27, textvariable=n)

        #Adding combobox drop down list
        self.entry_type['values'] = ('Casual Leave', 'Medical Leave', 'Maternity Leave', 'Paternity Leave', 'Compensatory Leave', 'Bereavement Leave')
        self.entry_type.place(x=210, y=320)
        self.entry_type.current()

        #button 1- Submit
        button = Button(self.bottom, text="Submit", font="arial 12 bold", bg="#0077b6", fg="White", command=self.leave)
        button.place(x=300, y=400)
        #button 2- Cancel
        button = Button(self.bottom, text="Cancel", font="arial 12 bold", command=self.destroy, bg="#0077b6", fg="White")
        button.place(x=390, y=400)

    def leave(self):
        emp_id = self.entry_id.get()
        name = self.entry_name.get()
        dept = self.entry_dept.get()
        date1 = self.entry_date1.get()
        date2 = self.entry_date2.get()
        duration = self.entry_duration.get()
        type = self.entry_type.get()
        status = "Pending"

        if emp_id and name and dept and date1 and date2 and duration and type and status != "":
            try:
                #add to database
                    query = "Insert into 'Leave' (emp_id,date1,date2,duration,type,status) values(?,?,?,?,?,?)"
                    cur.execute(query, (emp_id,date1,date2,duration,type,status))
                    con.commit()
                    messagebox.showinfo("Application Form", "Leave Successfully Applied")
                    self.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Fill all the fields", icon='warning')