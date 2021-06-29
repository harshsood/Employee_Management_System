from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
#we can code without using self in bottom cases
con = sqlite3.connect('db1.db')
cur = con.cursor()

class attendance(Toplevel):
    def __init__(self,emp_id):
        Toplevel.__init__(self)

        self.geometry("500x300+550+250")
        self.title('Mark Attendance')
        self.resizable(False,False)

        self.login = emp_id

        #frame
        self.frame = Frame(self, height=300, bg='#ccdbfd')
        self.frame.pack(fill=X)

        #label and button
        # id
        self.label_id = Label(self.frame, text="Employee ID ", font='arial 16 bold', fg='#e71d36', bg='#ccdbfd')
        self.label_id.place(x=40, y=40)

        self.entry_id = Entry(self.frame, width=30, bd=4)
        self.entry_id.insert(0, "Enter Employee ID")
        self.entry_id.place(x=180, y=40)

        #button
        button = Button(self.frame, text="Next", font="arial 12 bold", command=self.mark)
        button.place(x=215, y=200)
        button.bind("<Return>", self.mark)

    def mark(self, event=' '):

        self.emp_id = self.entry_id.get()

        window = tk.Tk()
        window.title('Mark Attendance')
        window.geometry('500x250')

        #label text for title
        ttk.Label(window, text="Present/Absent", font=("Times New Roman", 15)).grid(row=0, column=1)

        #label
        ttk.Label(window, text="Select the Option :", font=("Times New Roman", 10)).grid(column=0, row=5, padx=10, pady=25)

        #Combobox creation
        n = tk.StringVar()
        mark = ttk.Combobox(window, width=27, textvariable=n)

        #Adding combobox drop down list
        mark['values'] = ('Present', 'Absent')
        mark.grid(column=1, row=5)
        mark.current()

        # button
        button = Button(window, text="OK", font="arial 12 bold", command=self.marking)
        button.place(x=215, y=200)
        button.bind("<Return>", self.marking)
        window.mainloop()

    def marking(self):
        emp_id = self.emp_id

        attendance = ["Present", "Absent"]
        fieldValues = ["emp_id"]

        if emp_id != "":
           try:
                # add to database
                query = f"UPDATE Employee SET attendance = '{attendance[0]}' WHERE emp_id = {self.login}"
                print(type(query))
                cur.execute(query)
                con.commit()
                if attendance == "Absent":
                    print(0)
                    cur.execute("SELECT Employee FROM attendance WHERE emp_id=?", (fieldValues[0],))
                    row = cur.fetchall()
                    col = row

                messagebox.showinfo("Success", "Attendance Marked")
                self.destroy()
           except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Wrong Record", icon='warning')
