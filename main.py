from tkinter import *
from Registration import Registration
from admin import admin
from employee import employee
from tkinter import messagebox
from CalculateSalary import CalculateSalary
from Regularise import form
from ApproveRequest import Approve_Request
import sqlite3

con = sqlite3.connect('db1.db')
cur = con.cursor()

class System(object):
    def __init__(self,master):
        self.master = master

        #frame
        f1 = Frame(master, width=1360, height=100, bd=8, bg="#4f772d")
        f1.place(x=110, y=0)

        lbl_information = Label(f1, font=('arial', 45, 'bold'), text="EMPLOYEE MANAGEMENT SYSTEM", relief=GROOVE, bd=10, bg="#4f772d", fg="White")
        lbl_information.grid(row=0, column=0)

        f2 = Frame(master, width=1360, height=50, bd=8, bg="#4f772d")
        f2.place(x=0, y=110)

        self.Button1 = Button(f2, text="Employee", command=self.employee, font=("arial", 14, "bold"), bg='#90a955', fg='White')
        self.Button1.place(x=1080, y=0)

        self.Button2 = Button(f2, text="   Admin   ", command=self.admin, font=("arial", 14, "bold"), bg='#90a955', fg='White')
        self.Button2.place(x=960, y=0)

        self.Button3 = Button(f2, text="Register", command=self.Registration, font=("arial", 14, "bold"), bg='#90a955', fg='White')
        self.Button3.place(x=100, y=0)

        self.Button4 = Button(f2, text="Home", font=("arial", 14, "bold"), bg='#90a955', fg='White', command=master.destroy)
        self.Button4.place(x=20, y=0)

        f3 = Frame(master, width=1200, height=450, bd=8, bg="#31572c")
        f3.place(x=60, y=220)

        label1 = Label(f3, font=('arial', 20, 'bold'), text="Welcome Admin!!",  bg="#31572c", fg="White")
        label1.place(x=40, y=30)

        self.top_image2 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\1742-490x288.png")
        self.top_image2_label2 = Label(f3, image=self.top_image2)
        self.top_image2_label2.place(x=80, y=80)

        label2 = Label(f3, font=('arial', 20, 'bold', 'underline'), text="Features", bg="#31572c", fg="White")
        label2.place(x=700, y=30)

        self.Button2 = Button(f3, text="Manage Leaves", command=self.ManageLeaves, width=20, relief=GROOVE, bd=10, font=("arial", 14, "bold"), bg='#4f772d', fg='White')
        self.Button2.place(x=750, y=120)

        self.Button3 = Button(f3, text="Manage Salary", command=self.ManageSalary, width=20, relief=GROOVE, bd=10, font=("arial", 14, "bold"), bg='#4f772d', fg='White')
        self.Button3.place(x=750, y=180)

        self.Button4 = Button(f3, text="Attendance", command=self.attendancelist, width=20, relief=GROOVE, bd=10, font=("arial", 14, "bold"), bg='#4f772d', fg='White')
        self.Button4.place(x=750, y=240)

        self.Button5 = Button(f3, text="Regularize Attendance", command=self.Regularise, width=20, relief=GROOVE, bd=10, font=("arial", 14, "bold"), bg='#4f772d', fg='White')
        self.Button5.place(x=750, y=300)

    def Registration(self):
        window = Registration()

    def ManageLeaves(self):
        root = Tk()
        root.title("Manage Leaves")
        root.geometry("500x300+550+250")
        root.resizable(False,False)
        root.configure(bg="#ecf39e")

        label = Label(root, text="""Select the category you belong to:""", bg="#ecf39e", fg="#ef233c", font=('arial', 18, 'bold'))
        label.place(x=0, y=20)

        #buttons
        self.Button1 = Button(root, text="Employee", command=self.employee, font=("arial", 14, "bold"), bg='#0077b6', fg='White')
        self.Button1.place(x=50, y=100)

        self.Button2 = Button(root, text="   Admin   ", command=self.admin, font=("arial", 14, "bold"), bg='#0077b6', fg='White')
        self.Button2.place(x=50, y=200)
        root.mainloop()

    def Regularise(self):
        root = Tk()
        root.title("Regularise Attendance")
        root.geometry("500x300+550+250")
        root.resizable(False,False)
        root.configure(bg="#ecf39e")

        label = Label(root, text="""Select the category you belong to:""", bg="#ecf39e", fg="#ef233c", font=('arial', 18, 'bold'))
        label.place(x=0, y=20)

        #buttons
        self.Button1 = Button(root, text="Employee", command=self.regularise, font=("arial", 14, "bold"), bg='#0077b6', fg='White')
        self.Button1.place(x=50, y=100)

        self.Button2 = Button(root, text="   Admin   ", command=self.regulariserequest, font=("arial", 14, "bold"), bg='#0077b6', fg='White')
        self.Button2.place(x=50, y=200)
        root.mainloop()

    def ManageSalary(self):
        root = Tk()
        root.geometry("500x300+550+250")
        root.title('Admin Login')
        root.resizable(False, False)

        #frame
        self.frame = Frame(root, height=300, bg='#ecf39e')
        self.frame.pack(fill=X)

        #label and button

        #name
        self.label_id = Label(self.frame, text="Username ", font='arial 16 bold', fg='#e71d36', bg='#ecf39e')
        self.label_id.place(x=40, y=40)

        self.entry_id = Entry(self.frame, width=30, bd=4)
        self.entry_id.insert(0, "Enter Username")
        self.entry_id.place(x=150, y=40)

        #password
        self.label_password = Label(self.frame, text="Password ", font='arial 16 bold', fg='#e71d36', bg='#ecf39e')
        self.label_password.place(x=40, y=80)

        self.entry_password = Entry(self.frame, width=30, bd=4)
        self.entry_password.insert(0, "Enter Password")
        self.entry_password.config(show="*")
        self.entry_password.place(x=150, y=80)

        #button
        button = Button(self.frame, text="OK", font="arial 12 bold", command=self.submit)
        button.place(x=215, y=200)
        button.bind("<Return>", self.submit)

    def submit(self, event=' '):
        name = self.entry_id.get()
        password = self.entry_password.get()
        if password == 'admin123' and name == 'admin':
            window = CalculateSalary()
        else:
            messagebox.showinfo("Info", "wrong password")

    def admin(self):
        window = admin()

    def employee(self):
        window = employee()

    def regularise(self):
        window = form()

    def regulariserequest(self):
        window = Approve_Request()

    def attendancelist(self):
        root = Tk()
        root.title("Attendance Record")
        root.geometry('700x500')
        root.resizable(False, False)
        root.configure(bg="#283618")

        #frames
        self.top = Frame(root, height=100, bg='White')
        self.top.pack(fill=X)

        self.bottom = Frame(root, height=400, bg='#283618')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text="Attendance Record List", font='TimesNewRoman 24 bold', bg='#606c38', fg='White')
        self.heading.place(x=150, y=40)

        #bottom frame
        rows = []
        cur.execute('SELECT emp_id,name,designation,attendance FROM Employee where attendance=="Present"')

        column_names = [description[0] for description in cur.description]

        data = [tuple(column_names)] + cur.fetchall()

        for i in range(30):

            cols = []
            for j in range(4):
                e = Entry(self.bottom, relief=GROOVE)
                e.grid(row=i, column=j, sticky=NSEW)
                e.insert(INSERT, '\n')
                e.insert(INSERT, data[i][j])
                cols.append(e)
            rows.append(cols)

def main():
    root = Tk()
    sys = System(root)
    root.title("Employee Management System")
    root.geometry("1360x900+0+0")
    root.configure(bg='#ecf39e')
    root.resizable(False,False)
    root.mainloop()

if __name__ == '__main__':
    main()