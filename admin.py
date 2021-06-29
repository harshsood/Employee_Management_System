from tkinter import *
from tkinter import messagebox
from AdminLogin import AdminLogin

class admin(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("500x300+550+250")
        self.title('Admin Login')
        self.resizable(False,False)

        #frame
        self.frame = Frame(self, height=300, bg='#ecf39e')
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
            window = AdminLogin()
            self.destroy()
        else:
            messagebox.showinfo("Info", "wrong password")
