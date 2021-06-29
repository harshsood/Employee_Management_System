from tkinter import *
from tkinter import messagebox
import random
import sqlite3

con = sqlite3.connect('db1.db')
cur = con.cursor()

class Registration(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Registration Form")
        self.geometry("1360x900+0+0")
        self.configure(bg="#8d99ae")
        self.resizable(False, False)

        # labels and buttons
        # frames
        frame = Frame(self, width=600, height=600, bg='#2b2d42')
        frame.place(x=350, y=80)

        # top frame design
        self.heading = Label(frame, text="Registration Form", font='TimesNewRoman 20 bold', bg='#2b2d42', fg='White')
        self.heading.place(x=160, y=20)

        # id
        self.label_id = Label(frame, text="Employee ID", font='arial 12 bold', bg='#2b2d42', fg='White')
        self.label_id.place(x=130, y=80)

        self.entry_id = Entry(frame, width=30, bd=4)
        self.entry_id.insert(0, random.randint(1, 1000))
        self.entry_id.place(x=270, y=80)

        # name
        self.label_name = Label(frame, text="Name", font='arial 12 bold', bg='#2b2d42', fg='White')
        self.label_name.place(x=130, y=120)

        self.entry_name = Entry(frame, width=30, bd=4)
        self.entry_name.insert(0, "Enter Name")
        self.entry_name.place(x=270, y=120)

        # contact number
        self.label_phone = Label(frame, text="Contact Number", font='arial 12 bold', bg='#2b2d42', fg='White')
        self.label_phone.place(x=130, y=160)

        self.entry_phone = Entry(frame, width=30, bd=4)
        self.entry_phone.insert(0, "Enter Contact Number")
        self.entry_phone.place(x=270, y=160)

        # password
        self.label_password = Label(frame, text="Password", font='arial 12 bold', bg='#2b2d42', fg='White')
        self.label_password.place(x=130, y=200)

        self.entry_password = Entry(frame, width=30, bd=4)
        self.entry_password.insert(0, "Enter Password")
        self.entry_password.config(show="*")
        self.entry_password.place(x=270, y=200)

        # designation
        self.label_desg = Label(frame, text="Designation", font='arial 12 bold', bg='#2b2d42', fg='White')
        self.label_desg.place(x=130, y=240)

        self.entry_desg = Entry(frame, width=30, bd=4)
        self.entry_desg.insert(0, "Enter Designation")
        self.entry_desg.place(x=270, y=240)

        # department
        self.label_dept = Label(frame, text="Department", font='arial 12 bold', bg='#2b2d42', fg='White')
        self.label_dept.place(x=130, y=280)

        self.entry_dept = Entry(frame, width=30, bd=4)
        self.entry_dept.insert(0, "Enter Department")
        self.entry_dept.place(x=270, y=280)

        # Date of Joining
        self.label_DOJ = Label(frame, text="Date of Joining", font='arial 12 bold', bg='#2b2d42', fg='White')
        self.label_DOJ.place(x=130, y=320)

        self.entry_DOJ = Entry(frame, width=30, bd=4)
        self.entry_DOJ.insert(0, "Enter DOJ")
        self.entry_DOJ.place(x=270, y=320)

        # button 1- Register
        button = Button(frame, text="OK", font="arial 12 bold", bg="#06d6a0", fg="White", bd=10, width=14, relief=GROOVE, command=self.add_people)
        button.place(x=200, y=400)

        # button 2- Cancel
        button = Button(frame, text="Cancel", font="arial 12 bold", bg="#06d6a0", fg="White", bd=10, width=14, relief=GROOVE, command=self.destroy)
        button.place(x=200, y=450)

    def add_people(self):
        emp_id = self.entry_id.get()
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        password = self.entry_password.get()
        designation = self.entry_desg.get()
        department = self.entry_dept.get()
        doj = self.entry_DOJ.get()

        if emp_id and name and phone and password and designation and department and doj != "":
            try:
                # add to database
                query = "Insert into 'Employee' (emp_id,name,phone,password,designation,department,doj) values(?,?,?,?,?,?,?)"
                cur.execute(query, (emp_id, name, phone, password, designation, department, doj))
                con.commit()
                messagebox.showinfo("Success", "Registered Successfully")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "fill all the fields", icon='warning')