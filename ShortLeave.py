from tkinter import *
from tkinter import messagebox
import datetime
date = datetime.datetime.now().date()
date = str(date)
import sqlite3

con = sqlite3.connect('db1.db')
cur = con.cursor()

class Short_Leave(Toplevel):
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
        self.heading = Label(self.top, text=" Apply Short Leave ", font='TimesNewRoman 24 bold', bg='#0077b6', fg='White')
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

        #reason
        self.label_reason = Label(self.bottom, text="Reason", font='arial 12 bold', bg='#006d77', fg='White')
        self.label_reason.place(x=60, y=200)

        self.entry_reason = Entry(self.bottom, width=30, bd=4)
        self.entry_reason.insert(0, "Enter Reason")
        self.entry_reason.place(x=210, y=200)

        #Duration of Leave
        self.label_DOL = Label(self.bottom, text="Duration of Leave", font='arial 12 bold', bg='#006d77', fg='White')
        self.label_DOL.place(x=60, y=240)

        self.entry_DOL = Entry(self.bottom, width=30, bd=4)
        self.entry_DOL.insert(0, "Enter Duration")
        self.entry_DOL.place(x=210, y=240)

        #button 1- Submit
        button = Button(self.bottom, text="Submit", font="arial 12 bold", bg="#0077b6", fg="White", command=self.leave)
        button.place(x=300, y=400)
        #button 2- Cancel
        button = Button(self.bottom, text="Cancel", font="arial 12 bold", command=self.destroy, bg="#0077b6", fg="White")
        button.place(x=390, y=400)

    def leave(self):
        emp_id = self.entry_id.get()
        name = self.entry_name.get()
        department = self.entry_dept.get()
        reason = self.entry_reason.get()
        status = "Pending"

        if emp_id and name and department and reason and status != "":
            try:
                #add to database
                    query = "Insert into 'Leave' (emp_id,reason,status) values(?,?,?)"
                    cur.execute(query, (emp_id,reason,status))
                    con.commit()
                    messagebox.showinfo("Application Form", "Leave Successfully Applied")
                    self.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Fill all the fields", icon='warning')