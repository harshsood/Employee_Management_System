from tkinter import *
from ApplyLeave import Submit_Leave
from ShortLeave import Short_Leave
from Regularise import form
from MarkAttendance import attendance
import sqlite3

con = sqlite3.connect('db1.db')
cur = con.cursor()

class EmployeeLogin(Toplevel):
    def __init__(self,emp_id):
        Toplevel.__init__(self)

        self.geometry("1360x900")
        self.title("Employee Login")
        self.resizable(False, False)

        self.login = emp_id

        #frames
        self.top = Frame(self, height=100, bg='White')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=800, bg='#83c5be')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text='EMPLOYEE LOGIN', font=("arial", 45, "bold"), bd=10, relief=GROOVE, bg='#0077b6', fg='White')
        self.heading.place(x=370, y=0)

        #button 1 = Employee Information
        self.Button1 = Button(self.bottom, text=" Employee Information ", command=self.EmployeeInformation, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button1.place(x=80, y=190)

        #image1
        self.image1_icon1 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\employee_information.png")
        self.label1_icon1 = Label(self.bottom, image=self.image1_icon1)
        self.label1_icon1.place(x=100, y=30)

        #button 2 = Submit Leave
        self.Button2 = Button(self.bottom, text="      Submit Leave      ", command=self.apply, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button2.place(x=600, y=190)

        #image2
        self.image2_icon2 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\submitleave.png")
        self.label2_icon2 = Label(self.bottom, image=self.image2_icon2)
        self.label2_icon2.place(x=610, y=30)

        #button 3 = Regualrization Request
        self.Button3 = Button(self.bottom, text=" Regualrization Request ", command=self.regularise_request, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button3.place(x=1100, y=190)

        #image3
        self.image3_icon3 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\regularise.png")
        self.label3_icon3 = Label(self.bottom, image=self.image3_icon3)
        self.label3_icon3.place(x=1120, y=30)

        #button 4 = All Leaves Status
        self.Button4 = Button(self.bottom, text="    All Leaves Status    ", command=self.EmployeeAllStatus, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button4.place(x=340, y=360)

        #image4
        self.image4_icon4 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\all_leave_status.png")
        self.label4_icon4 = Label(self.bottom, image=self.image4_icon4)
        self.label4_icon4.place(x=350, y=200)

        #button 5 = View Salary
        self.Button5 = Button(self.bottom, text="     View Salary Slip     ", command=self.slip, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button5.place(x=850, y=360)

        #image5
        self.image5_icon5 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\salaryslip.png")
        self.label5_icon5 = Label(self.bottom, image=self.image5_icon5)
        self.label5_icon5.place(x=860, y=200)

        #button 6 = Mark Attendance
        self.Button6 = Button(self.bottom, text="    Mark Attendance   ", command=self.markattendance, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button6.place(x=80, y=530)

        #image6
        self.image6_icon6 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\markattendance.png")
        self.label6_icon6 = Label(self.bottom, image=self.image6_icon6)
        self.label6_icon6.place(x=90, y=370)

        #button 7 = Apply Short Leave
        self.Button7 = Button(self.bottom, text="     Apply Short Leave     ", command=self.shortleave, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button7.place(x=600, y=530)

        #image7
        self.image7_icon7 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\shortleave.png")
        self.label7_icon7 = Label(self.bottom, image=self.image7_icon7)
        self.label7_icon7.place(x=610, y=370)

        #button 8 = Logout
        self.Button8 = Button(self.bottom, text="             Logout             ", command=self.Employeelogout, font=("TimesNewRoman", 12, "bold"), bg='#ffc300', fg='#e71d36')
        self.Button8.place(x=1100, y=530)

        #image8
        self.image8_icon8 = PhotoImage(file=r"C:\Users\Harsh Sood\PycharmProjects\pythonProject3\logout.png")
        self.label8_icon8 = Label(self.bottom, image=self.image8_icon8)
        self.label8_icon8.place(x=1110, y=370)

    def regularise_request(self):
        window = form()

    def EmployeeInformation(self):
        root = Tk()
        root.title("Employee Information")
        root.geometry('700x500')
        root.resizable(False, False)
        root.configure(bg="#006d77")

        #frames
        self.top = Frame(root, height=100, bg='White')
        self.top.pack(fill=X)

        self.bottom = Frame(root, height=400, bg='#006d77')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text="My Profile", font='TimesNewRoman 24 bold', bg='#0077b6', fg='White')
        self.heading.place(x=230, y=40)

        #bottom frame
        rows = []
        cur.execute(f"Select emp_id,name,phone,designation,department,doj from Employee where emp_id={self.login}")

        column_names = [description[0] for description in cur.description]

        data = [column_names]
        data += [cur.fetchone()]

        for i in range(6):
            cols = []
            for j in range(2):
                e = Entry(self.bottom, relief=GROOVE)
                e.grid(row=i, column=j, sticky=NSEW)
                e.insert(INSERT, '\n')
                e.insert(INSERT, data[j][i])
                cols.append(e)
            rows.append(cols)

    #def balance(self):
        #self.check = (self.login,)
        #self.balanced = []
        #cur.execute('SELECT emp_id,medical_leave,maternity_leave,paternity_leave,casual_leave,bereavement_leave,compensatory_leave FROM Leave where emp_id=?', self.check)
        #data = cur.fetchall()
        #print(data)
        #for i in data:
            #for j in i:
                #self.balanced.append(j)
        #print(self.balanced)
        #self.WindowBalance()

    #def WindowBalance(self):
        #root = Tk()
        #root.title("Balance Window")
        #root.geometry('700x500')
        #root.resizable(False, False)
        #root.configure(bg="#006d77")

        #frames
        #self.top = Frame(root, height=100, bg='White')
        #self.top.pack(fill=X)

        #self.bottom = Frame(root, height=400, bg='#006d77')
        #self.bottom.pack(fill=X)

        #top frame design
        #self.heading = Label(self.top, text="Leave Balance", font='TimesNewRoman 24 bold', bg='#0077b6', fg='White')
        #self.heading.place(x=230, y=40)

        #bottom frame
        #label_1 = Label(self.bottom, text="Employee ID", fg="White", bg='#006d77', justify=LEFT, font=("TimesNewRoman", 16))
        #label_2 = Label(self.bottom, text=self.balanced[0], font=("TimesNewRoman", 16), bg='#006d77', fg="White")
        #label_3 = Label(self.bottom, text="Medical Leave=", fg="White", bg='#006d77', justify=LEFT, font=("TimesNewRoman", 16))
        #label_4 = Label(self.bottom, text=self.balanced[1], font=("TimesNewRoman", 16), bg='#006d77', fg="White")
        #label_5 = Label(self.bottom, text="Maternity Leave=", fg="White", bg='#006d77', justify=LEFT, font=("TimesNewRoman", 16))
        #label_6 = Label(self.bottom, text=self.balanced[2], font=("TimesNewRoman", 16), bg='#006d77', fg="White")
        #label_7 = Label(self.bottom, text="Paternity Leave=", fg="White", bg='#006d77', justify=LEFT, font=("TimesNewRoman", 16))
        #label_8 = Label(self.bottom, text=self.balanced[3], font=("TimesNewRoman", 16), bg='#006d77', fg="White")
        #label_9 = Label(self.bottom, text="Casual Leave=", fg="White", bg='#006d77', justify=LEFT,font=("TimesNewRoman", 16))
        #label_10 = Label(self.bottom, text=self.balanced[4], font=("TimesNewRoman", 16), bg='#006d77', fg="White")
        #label_1.grid(row=0, column=0)
        #label_2.grid(row=0, column=1)
        #label_3.grid(row=1, column=0)
        #label_4.grid(row=1, column=1)
        #label_5.grid(row=2, column=0)
        #label_6.grid(row=2, column=1)
        #label_7.grid(row=3, column=0)
        #label_8.grid(row=3, column=1)
        #label_9.grid(row=4, column=0)
        #label_10.grid(row=4, column=1)

    def apply(self):
        window = Submit_Leave(self.login)

    def shortleave(self):
        window = Short_Leave(self.login)

    def markattendance(self):
        window = attendance(self.login)

    def Employeelogout(self):
        self.login = -1
        self.destroy()

    def EmployeeAllStatus(self):
        root = Tk()
        root.title("All Leaves Status")
        root.geometry('700x500')
        root.resizable(False, False)
        root.configure(bg="#006d77")

        #frames
        self.top = Frame(root, height=100, bg='White')
        self.top.pack(fill=X)

        self.bottom = Frame(root, height=400, bg='#006d77')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text="Leave Status", font='TimesNewRoman 24 bold', bg='#0077b6', fg='White')
        self.heading.place(x=230, y=40)

        #bottom frame
        #txt = Text(self.bottom)
        #txt.pack()
        #cur.execute(f"SELECT leave_id,type,date1,date2,status FROM Leave where emp_id={self.login}")
        #data = cur.fetchall()
        #if any(data):
            #for i in data:
                #txt.insert(INSERT, i)
                #txt.insert(INSERT, '\n')
        #else:
            #txt.insert(INSERT, "There is no record present with given parameter")

        rows = []
        cur.execute(f"SELECT leave_id,type,date1,date2,status FROM Leave where emp_id={self.login}")

        column_names = [description[0] for description in cur.description]

        data = [tuple(column_names)] + cur.fetchall()

        for i in range(30):

            cols = []
            for j in range(5):
                e = Entry(self.bottom, relief=GROOVE)
                e.grid(row=i, column=j, sticky=NSEW)
                e.insert(INSERT, '\n')
                e.insert(INSERT, data[i][j])
                cols.append(e)
            rows.append(cols)

    def slip(self):
        root = Tk()
        root.title("Salary Slip")
        root.geometry('700x500')
        root.resizable(False, False)
        root.configure(bg="#006d77")

        #frames
        self.top = Frame(root, height=100, bg='White')
        self.top.pack(fill=X)

        self.bottom = Frame(root, height=400, bg='#006d77')
        self.bottom.pack(fill=X)

        #top frame design
        self.heading = Label(self.top, text="Salary Slip", font='TimesNewRoman 24 bold', bg='#0077b6', fg='White')
        self.heading.place(x=230, y=40)

        #bottom frame
        #txt = Text(self.bottom)
        #txt.pack()
        #cur.execute(f"Select * from Salary where emp_id={self.login}")
        #data = cur.fetchall()
        #if any(data):
            #for i in data:
                #txt.insert(INSERT, i)
                #txt.insert(INSERT, '\n')
        #else:
            #txt.insert(INSERT, "There is no record present with given parameter")

        #rows = []
        #cur.execute(f"Select * from Salary where emp_id={self.login}")

        #column_names = [description[0] for description in cur.description]

        #data = [column_names]
        #data += [cur.fetchone()]

        #for i in range(12):
            #cols = []
            #for j in range(2):
                #e = Entry(self.bottom, relief=GROOVE)
                #e.grid(row=i, column=j, sticky=NSEW)
                #e.insert(INSERT, '\n')
                #e.insert(INSERT, data[j][i])
                #cols.append(e)
            #rows.append(cols)

        rows = []
        cur.execute(f"Select * from Salary where emp_id={self.login}")

        column_names = [description[0] for description in cur.description]

        data = [column_names]
        data += [cur.fetchone()]

        for i in range(11):
            cols = []
            for j in range(2):
                e = Entry(self.bottom, relief=GROOVE)
                e.grid(row=i, column=j, sticky=NSEW)
                e.insert(INSERT, '\n')
                e.insert(INSERT, data[j][i])
                cols.append(e)
            rows.append(cols)