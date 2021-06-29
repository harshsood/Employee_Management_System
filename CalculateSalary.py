from tkinter import *
import datetime
date = datetime.datetime.now().date()
date = str(date)
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('db1.db')
cur = con.cursor()

def change_text(ui_object, new_value):
   ui_object.delete(0,END)
   ui_object.insert(0,new_value)

class CalculateSalary(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("1360x900")
        self.title("Calculate Salary")
        self.configure(bg='#fed9b7')
        self.resizable(False, False)

        #frame
        frame1 = Frame(self, width=1360, height=100, bd=8, bg="#f07167")
        frame1.place(x=310, y=0)

        lbl_information = Label(frame1, font=('arial', 45, 'bold'), text="SALARY CALCULATION", relief=GROOVE, bd=10, bg="#f07167", fg="White")
        lbl_information.grid(row=0, column=0)

        f1 = Frame(self, width=1000, height=600, bd=8, bg="#fff1e6")
        f1.pack(side=LEFT)
        f2 = Frame(self, width=400, height=600, bd=8, bg="#f19c79")
        f2.pack(side=RIGHT)

        frame = Frame(f1, width=960, height=550, bd=8, bg="#eaac8b")
        frame.place(x=10,y=10)

        self.frame2 = Frame(f2, width=320, height=550, bd=8, bg="White")
        self.frame2.place(x=10,y=10)
        self.entry_payslip_text = Text(self.frame2, width=200, height=480, bg="White", bd=8, relief=GROOVE)
        self.entry_payslip_text.place(x=15,y=15)


        #labels
        label1 = Label(frame, font=('arial', 20, 'bold'), text="Personal Details", bg="#eaac8b", fg="White")
        label1.place(x=10, y=10)

        #id
        self.label_id = Label(frame, text="Employee ID", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_id.place(x=40, y=50)

        self.entry_id = Entry(frame, width=30, bd=4)
        self.entry_id.insert(0, "Enter Employee ID")
        self.entry_id.place(x=150, y=50)

        #name
        self.label_name = Label(frame, text="Name", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_name.place(x=40, y=90)

        self.entry_name = Entry(frame, width=30, bd=4)
        self.entry_name.insert(0, "Enter Name")
        self.entry_name.place(x=150, y=90)

        #department
        self.label_dept = Label(frame, text="Department", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_dept.place(x=40, y=130)

        self.entry_dept = Entry(frame, width=30, bd=4)
        self.entry_dept.insert(0, "Enter Department")
        self.entry_dept.place(x=150, y=130)

        #designation
        self.label_desg = Label(frame, text="Designation", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_desg.place(x=530, y=50)

        self.entry_desg = Entry(frame, width=30, bd=4)
        self.entry_desg.insert(0, "Enter Designation")
        self.entry_desg.place(x=670, y=50)

        #contact number
        self.label_phone = Label(frame, text="Contact Number", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_phone.place(x=530, y=90)

        self.entry_phone = Entry(frame, width=30, bd=4)
        self.entry_phone.insert(0, "Enter Contact Number")
        self.entry_phone.place(x=670, y=90)

        #Date of Issue
        self.label_DOI = Label(frame, text="Date of Application:  " + date, font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_DOI.place(x=530, y=130)

        #label2
        label2 = Label(frame, font=('arial', 20, 'bold'), text="Salary Details", bg="#eaac8b", fg="White")
        label2.place(x=10, y=170)

        #basic pay
        self.label_pay = Label(frame, text="Basic Pay", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_pay.place(x=40, y=220)

        self.entry_pay = Entry(frame, width=30, bd=4)
        self.entry_pay.insert(0, "Enter Basic Pay")
        self.entry_pay.place(x=150, y=220)

        #allowance1
        self.label_transport = Label(frame, text="Transport", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_transport.place(x=40, y=260)

        self.entry_transport = Entry(frame, width=30, bd=4)
        self.entry_transport.insert(0, "-")
        self.entry_transport.place(x=150, y=260)

        #incentive
        self.label_bonus1 = Label(frame, text="Incentive", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_bonus1.place(x=40, y=300)

        self.entry_bonus1 = Entry(frame, width=30, bd=4)
        self.entry_bonus1.insert(0, "Enter Incentive Amount")
        self.entry_bonus1.place(x=150, y=300)

        #tax
        self.label_tax = Label(frame, text="Income Tax", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_tax.place(x=530, y=220)

        self.entry_tax = Entry(frame, width=30, bd=4)
        self.entry_tax.insert(0, "-")
        self.entry_tax.place(x=700, y=220)

        #allowance2
        self.label_da = Label(frame, text="Dearness Allowance", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_da.place(x=530, y=260)

        self.entry_da = Entry(frame, width=30, bd=4)
        self.entry_da.insert(0, "-")
        self.entry_da.place(x=700, y=260)

        #leaves
        self.label_leaves = Label(frame, text="Leaves", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_leaves.place(x=530, y=300)

        self.entry_leaves = Entry(frame, width=30, bd=4)
        self.entry_leaves.insert(0, "Enter Number")
        self.entry_leaves.place(x=700, y=300)

        #pf
        self.label_pf = Label(frame, text="P.F", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_pf.place(x=40, y=340)

        self.entry_pf = Entry(frame, width=30, bd=4)
        self.entry_pf.insert(0, "-")
        self.entry_pf.place(x=150, y=340)

        #net pay
        self.label_net = Label(frame, text="Net Pay", font='arial 12 bold', bg='#eaac8b', fg='White')
        self.label_net.place(x=530, y=340)

        self.entry_net = Entry(frame, width=30, bd=4)
        self.entry_net.insert(0, "-")
        self.entry_net.place(x=700, y=340)

        #buttons
        #calculate
        button1 = Button(frame, text="Calculate", command=self.calculate, font=('arial', 16, 'bold'), width=10,  relief=GROOVE, bd=10, bg="#f07167", fg="White")
        button1.place(x=50, y=440)

        #payslip
        button2 = Button(frame, text="View Pay Slip", font=('arial', 16, 'bold'), command=self.pay, width=10, relief=GROOVE, bd=10, bg="#f07167", fg="White")
        button2.place(x=220, y=440)

        #reset
        button3 = Button(frame, text="Reset", font=('arial', 16, 'bold'), command=self.reset, width=10, relief=GROOVE, bd=10, bg="#f07167", fg="White")
        button3.place(x=500, y=440)

        #exit
        button4 = Button(frame, text="Exit", font=('arial', 16, 'bold'), command=self.Exit, width=10, relief=GROOVE, bd=10, bg="#f07167", fg="White")
        button4.place(x=670, y=440)

    def Exit(self):
        wayOut = messagebox.askyesno("Salary Calculation Window", "Do you want to Exit the page?")
        if 'yes':
            self.destroy()
            return

    def calculate(self):
        emp_id = self.entry_id.get()
        name = self.entry_name.get()
        department = self.entry_dept.get()
        designation = self.entry_desg.get()
        pay = float(self.entry_pay.get())
        ta = float(pay * 0.075)
        bonus = float(self.entry_bonus1.get())
        tax = float(pay * 0.12)
        da = float(pay * 0.25)
        leaves = float(self.entry_leaves.get()) * 100
        pf = float((pay + da) * 0.12)
        net = float(pay + da + bonus + ta - pf - leaves)

        # transport (self.entry_transport)
        # p.f (self.entry_pf)
        # income tax (self.entry_tax)
        # dearness allowance (self.entry_da)
        # net pay (self.entry_net)

        change_text(self.entry_pf, pf)
        change_text(self.entry_tax, tax)
        change_text(self.entry_da, da)
        change_text(self.entry_net, net)
        change_text(self.entry_transport, ta)

        print(pay, emp_id, name, department, designation, ta, bonus, tax, da, leaves, pf, net)

        '''Calculate the Gross Salary of an employee for following allowance & deduction.
        Get Basic Salary of Employee,
        da = 25% of Basic,
        pf = 12% of Basic,
        ta = 7.50% of Basic.
        net = pay + da + ta + bonus - tax - leaves - pf
        '''
        if emp_id and name and department and designation and pay and ta and bonus and tax and da and leaves and pf and net != "":
            try:
                # add to database
                query = "Insert into 'Salary' (emp_id,name,department,designation,pay,ta,bonus,tax,da,leaves,pf,net) values(?,?,?,?,?,?,?,?,?,?,?,?)"
                cur.execute(query, (emp_id, name, department, designation, pay, ta, bonus, tax, da, leaves, pf, net))
                con.commit()
                messagebox.showinfo("Success", "Recorded Successfully")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "fill all the fields", icon='warning')

        # print("SALARY PROGRAM")
        # name = str(input("Enter name of employee:"))
        # pay = float(input("Enter Basic Salary :"))
        # da = float(pay * 0.25)
        # pf = float((pay + da) * 0.12)
        # ta = float(pay * 0.075)
        # net = float(pay + da + ta - pf - leaves)

        # print("\n\n")
        print("S A L A R Y D E T A I L E D B R E A K U P ")
        print("==============================================")
        print(" NAME OF EMPLOYEE : ", name)
        print(" BASIC SALARY : ", pay)
        print(" DEARNESS ALLOW. : ", da)
        print(" TRAVEL ALLOW. : ", ta)
        print("==============================================")
        print(" NET SALARY PAY : ", net)
        print(" PROVIDENT FUND : ", pf)
        print("==============================================")

    def pay(self):
        self.entry_payslip_text.delete("1.0", END)
        self.entry_payslip_text.insert(END, "\t\tPay Slip\n\n")
        self.entry_payslip_text.insert(END, "Employee ID: " + self.entry_id.get() + "\n\n")
        self.entry_payslip_text.insert(END,"Name: "  + self.entry_name.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Department: " + self.entry_dept.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Designation: " + self.entry_desg.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Contact Number: " + self.entry_phone.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Basic Pay: " + self.entry_pay.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Transport Allowance: " + self.entry_transport.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Income Tax: " + self.entry_tax.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Dearness Allowance: " + self.entry_da.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Incentive: " + self.entry_bonus1.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Leaves: " + self.entry_leaves.get() + "\n\n")
        self.entry_payslip_text.insert(END, "P.F: " + self.entry_pf.get() + "\n\n")
        self.entry_payslip_text.insert(END, "Net Pay: " + self.entry_net.get() + "\n\n")

    def reset(self):
        change_text(self.entry_id, "")
        change_text(self.entry_name, "")
        change_text(self.entry_dept, "")
        change_text(self.entry_desg, "")
        change_text(self.entry_phone, "")
        change_text(self.entry_pay, "")
        change_text(self.entry_bonus1, "")
        change_text(self.entry_transport, "")
        change_text(self.entry_da, "")
        change_text(self.entry_pf, "")
        change_text(self.entry_leaves, "")
        change_text(self.entry_tax, "")
        change_text(self.entry_net, "")
        #change_text(self.entry_payslip_text, "")
        self.entry_payslip_text.delete("1.0", END)
