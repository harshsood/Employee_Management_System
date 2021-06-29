from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
#we can code without using self in bottom cases
con = sqlite3.connect('db1.db')
cur = con.cursor()

class Approve_Leave(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        # exampleID is the id of the Employee who is requesting the leave
        self.exampleID = 101

        self.geometry("500x300+550+250")
        self.title('Approve Leave')
        self.resizable(False,False)

        #frame
        self.frame = Frame(self, height=300, bg='#ccdbfd')
        self.frame.pack(fill=X)

        #label and button

        #leave id
        self.label_leave_id = Label(self.frame, text="Leave ID", font='arial 16 bold', fg='#e71d36', bg='#ccdbfd')
        self.label_leave_id.place(x=40, y=40)

        self.entry_leave_id = Entry(self.frame, width=30, bd=4)
        self.entry_leave_id.insert(0, "Enter Leave ID")
        self.entry_leave_id.place(x=150, y=40)

        #button
        button = Button(self.frame, text="Next", font="arial 12 bold", command=self.approval)
        button.place(x=215, y=200)
        button.bind("<Return>", self.approval)

    def approval(self, event=' '):

        self.leave_id = self.entry_leave_id.get()

        window = tk.Tk()
        window.title('Leave Approval')
        window.geometry('500x250')

        #label text for title
        ttk.Label(window, text="Approve/Deny", font=("Times New Roman", 15)).grid(row=0, column=1)

        #label
        ttk.Label(window, text="Select the Option :", font=("Times New Roman", 10)).grid(column=0, row=5, padx=10, pady=25)

        #Combobox creation
        n = tk.StringVar()
        optionchoosen = ttk.Combobox(window, width=27, textvariable=n)

        #Adding combobox drop down list
        optionchoosen['values'] = ('Approve', 'Deny')
        optionchoosen.grid(column=1, row=5)
        optionchoosen.current()

        #button
        button = Button(window, text="OK", font="arial 12 bold", command=self.appt)
        button.place(x=215, y=200)
        button.bind("<Return>", self.appt)
        window.mainloop()

    def appt(self):
        leave_id = self.leave_id
        status = ["Approve", "Deny"]
        fieldValues = ["leave_id"]

        if leave_id != "":
           try:
                #add to database
                query = f"UPDATE Leave SET status = '{status[0]}' WHERE leave_id = {leave_id}"
                print(type(query))
                cur.execute(query)
                con.commit()
                if status == "Pending":
                    print(0)
                    cur.execute("SELECT type FROM Leave WHERE leave_id=?", (fieldValues[0],))
                    row = cur.fetchall()
                    col = row

                    for row in con.execute("SELECT emp_id,duration FROM Leave WHERE leave_id=?", (fieldValues[0],)):
                        print(2)
                        self.exampleId = row[0]

                    for row in con.execute("SELECT duration FROM Leave WHERE leave_id=?", (fieldValues[0],)):
                        print(2)
                        self.exampleDays = row[0]

                    for row in con.execute("SELECT medical_leave FROM Leave WHERE emp_id=?", (self.exampleId,)):
                        self.balance = row[0]
                        print(self.balance)

                    for row in con.execute("SELECT casual_leave FROM Leave WHERE emp_id=?", (self.exampleId,)):
                        balance1 = row[0]
                        print(balance1)

                    if (col[0] == ('medicalleave',)):
                        print(3)
                        con.execute("UPDATE Leave SET medical_leave =? WHERE emp_id= ?", ((self.balance - self.exampleDays), (self.exampleId)))

                    if (col[0] == ('casualleave',)):
                        print(3)
                        con.execute("UPDATE Leave SET casual_leave =? WHERE emp_id= ?", ((self.balance - self.exampleDays), (self.exampleId)))

                messagebox.showinfo("Success", "Leave approved and updated")
                self.destroy()
           except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Wrong Record", icon='warning')
