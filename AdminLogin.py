from tkinter import *
from ApproveLeave import Approve_Leave
from ApproveRequest import Approve_Request
from attendance import attendance
import sqlite3

con = sqlite3.connect('db1.db')
cur = con.cursor()

class AdminLogin(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("1360x900")
        self.title("Admin Login")
        self.resizable(False, False)

        #frames
        self.top = Frame(self, height=100, bg='White')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=800, bg='#33658a')
        self.bottom.pack(fill=X)

        #top frame design
        lbl_information = Label(self.top, font=('arial', 45, 'bold'), text="ADMIN LOGIN", relief=GROOVE, bd=10, bg="#0077b6", fg="White")
        lbl_information.place(x=420, y=0)

        #button 1 = All Employee Information
        self.Button1 = Button(self.bottom, text=" All Employee Information ", command=self.AllEmployeeInformation, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button1.place(x=50, y=190)

        #image1
        self.image1_icon1 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\all_employee_information.png")
        self.label1_icon1 = Label(self.bottom, image=self.image1_icon1)
        self.label1_icon1.place(x=70, y=30)

        #button 2 = Leave Approval List
        self.Button2 = Button(self.bottom, text="      Leave Approval List     ", command=self.leavelist, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button2.place(x=420, y=190)

        #image2
        self.image2_icon2 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\leave_list.png")
        self.label2_icon2 = Label(self.bottom, image=self.image2_icon2)
        self.label2_icon2.place(x=450, y=30)

        #button 3 = Approve Leave
        self.Button3 = Button(self.bottom, text="         Approve Leave         ", command=self.approve, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button3.place(x=770, y=190)

        #image3
        self.image3_icon3 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\approve_leave.png")
        self.label3_icon3 = Label(self.bottom, image=self.image3_icon3)
        self.label3_icon3.place(x=790, y=30)

        #button 4 = View Attendance
        self.Button4 = Button(self.bottom, text="          View Attendance          ", command=self.attendance, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button4.place(x=1120, y=190)

        #image4
        self.image4_icon4 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\attendance.png")
        self.label4_icon4 = Label(self.bottom, image=self.image4_icon4)
        self.label4_icon4.place(x=1130, y=30)

        #button 5 = Regularise Attendance
        self.Button5 = Button(self.bottom, text="Regularise Attendance", command=self.regulariserequest, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button5.place(x=620, y=460)

        #image5
        self.image5_icon5 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\regularise.png")
        self.label5_icon5 = Label(self.bottom, image=self.image5_icon5)
        self.label5_icon5.place(x=640, y=300)

        #button 6 = Salary Status
        self.Button6 = Button(self.bottom, text="    View Salary Status    ", command=self.SalaryStatus, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button6.place(x=250, y=460)

        #image6
        self.image6_icon6 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\salary.png")
        self.label6_icon6 = Label(self.bottom, image=self.image6_icon6)
        self.label6_icon6.place(x=270, y=300)

        #button 7 = Logout
        self.Button7 = Button(self.bottom, text="             Logout             ", font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36', command=self.destroy)
        self.Button7.place(x=990, y=460)

        #image7
        self.image7_icon7 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\logout.png")
        self.label7_icon7 = Label(self.bottom, image=self.image7_icon7)
        self.label7_icon7.place(x=1000, y=300)

    def AllEmployeeInformation(self):
        root = Tk()
        root.title("All Employee's Record")
        root.geometry('700x500')
        root.resizable(False, False)
        root.configure(bg="#2f4858")

        #frames
        self.top = Frame(root, height=100, bg='White')
        self.top.pack(fill=X)

        self.bottom = Frame(root, height=400, bg='#2f4858')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text="All Employee's Record", font='TimesNewRoman 24 bold', bg='#0077b6', fg='White')
        self.heading.place(x=230, y=40)

        #bottom frame
        #txt = Text(self.bottom)
        #for i in con.execute('SELECT emp_id,name,phone,password,designation,department,doj FROM Employee where doj != "" '):
            #txt.insert(INSERT, i)
            #txt.insert(INSERT, '\n')

            #txt.pack()

        rows = []
        cur.execute('SELECT emp_id,name,phone,designation,department,doj FROM Employee where doj != "" ')

        column_names = [description[0] for description in cur.description]


        data = [tuple(column_names)] + cur.fetchall()


        for i in range(100):

            cols = []
            for j in range(6):
                e = Entry(self.bottom, relief=GROOVE)
                e.grid(row=i, column=j, sticky=NSEW)
                e.insert(INSERT, '\n')
                e.insert(INSERT, data[i][j])
                cols.append(e)
            rows.append(cols)

    def approve(self):
        window = Approve_Leave()

    def leavelist(self):
        root = Tk()
        root.title("All Leaves List")
        root.geometry('700x500')
        root.resizable(False, False)
        root.configure(bg="#2f4858")

        #frames
        self.top = Frame(root, height=100, bg='White')
        self.top.pack(fill=X)

        self.bottom = Frame(root, height=400, bg='#2f4858')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text="Leave List", font='TimesNewRoman 24 bold', bg='#0077b6', fg='White')
        self.heading.place(x=230, y=40)

        #bottom frame
        #txt = Text(self.bottom)
        #for i in con.execute('SELECT leave_id,emp_id,date1,date2,type,status FROM Leave where status=="Pending"'):
            #txt.insert(INSERT, i)
            #txt.insert(INSERT, '\n')

            #txt.pack()

        rows = []
        cur.execute('SELECT leave_id,emp_id,date1,date2,type,status FROM Leave where status=="Pending"')

        column_names = [description[0] for description in cur.description]

        data = [tuple(column_names)] + cur.fetchall()

        for i in range(100):

            cols = []
            for j in range(6):
                e = Entry(self.bottom, relief=GROOVE)
                e.grid(row=i, column=j, sticky=NSEW)
                e.insert(INSERT, '\n')
                e.insert(INSERT, data[i][j])
                cols.append(e)
            rows.append(cols)

    def regulariserequest(self):
        window = Approve_Request()

    def attendance(self):
        window = attendance()

    def SalaryStatus(self):
        root = Tk()
        root.title("Salary Status")
        root.geometry('1360x900')
        root.resizable(False, False)
        root.configure(bg="#2f4858")

        #frames
        self.top = Frame(root, height=100, bg='White')
        self.top.pack(fill=X)

        self.bottom = Frame(root, height=400, bg='#2f4858')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text="Salary Record", font='TimesNewRoman 24 bold', bg='#0077b6', fg='White')
        self.heading.place(x=230, y=40)

        #bottom frame
        #txt = Text(self.bottom)
        #for i in con.execute('SELECT * FROM Salary where emp_id != "" '):
            #txt.insert(INSERT, i)
            #txt.insert(INSERT, '\n')

            #txt.pack()

        rows = []
        cur.execute('SELECT * FROM Salary where emp_id != "" ')

        column_names = [description[0] for description in cur.description]

        data = [tuple(column_names)] + cur.fetchall()

        for i in range(100):

            cols = []
            for j in range(11):
                e = Entry(self.bottom, relief=GROOVE)
                e.grid(row=i, column=j, sticky=NSEW)
                e.insert(INSERT, '\n')
                e.insert(INSERT, data[i][j])
                cols.append(e)
            rows.append(cols)