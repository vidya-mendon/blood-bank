# Importing essential packages
from tkinter import *
import tkinter.messagebox
import sqlite3


class Add:
    def __init__(self, parent):

        # Window Initialization
        self.register_window = Toplevel(parent)
        self.register_window.title("Redline | Add Blood")
        self.register_window.geometry("500x550")
        self.name = StringVar()
        self.age = IntVar()
        self.add = StringVar()
        self.quantity = IntVar()
        self.var = StringVar()
        self.mob = IntVar()

        # Database Info
        self.connection = sqlite3.connect("Blood.db")
        self.tablename = "blood_bank"

        # Heading
        lbl_0 = Label(self.register_window,
                      text="Add Blood", bg="grey", width="300",
                      height="2", font=("Calibri", 18), fg="white"
                      ).pack()
        Label(self.register_window, text="").pack()

        # Name
        lbl_1 = Label(self.register_window, text="Enter the Name",
                      font=("bold", 8)).pack()
        entry_1 = Entry(self.register_window,
                        textvar=self.name).pack(pady=(0, 20))

        # Age
        lbl_2 = Label(self.register_window, text="Enter the Age",
                      font=("bold", 8)).pack()
        entry_2 = Entry(self.register_window,
                        textvar=self.age).pack(pady=(0, 20))
        # Quantity
        lbl_21 = Label(self.register_window, text="Enter the Quantity",
                       font=("bold", 8)).pack()
        entry_21 = Entry(self.register_window,
                         textvar=self.quantity).pack(pady=(0, 20))

        # Address
        lbl_3 = Label(self.register_window, text="Enter the Address",
                      font=("bold", 8)).pack()
        entry_3 = Entry(self.register_window,
                        textvar=self.add).pack(pady=(0, 20))

        # Blood group - Radio buttons
        lbl_4 = Label(self.register_window, text="Chose the Blood Group",
                      font=("bold", 8)).pack()
        r1 = Radiobutton(self.register_window, text="A Positive", padx=5, variable=self.var,
                         value="A+").pack()
        r2 = Radiobutton(self.register_window, text="B Positive", padx=15, variable=self.var,
                         value="B+").pack()
        r3 = Radiobutton(self.register_window, text="O Positive", padx=30, variable=self.var,
                         value="O+").pack()
        r4 = Radiobutton(self.register_window, text="A Negative", padx=30, variable=self.var,
                         value="A-").pack()
        r5 = Radiobutton(self.register_window, text="B Negative", padx=30, variable=self.var,
                         value="B-").pack()
        r6 = Radiobutton(self.register_window, text="O Negative", padx=30, variable=self.var,
                         value="O-").pack()
        r7 = Radiobutton(self.register_window, text="AB Positive", padx=30, variable=self.var,
                         value="AB+").pack()
        r8 = Radiobutton(self.register_window, text="AB Negative", padx=30, variable=self.var,
                         value="AB-").pack(pady=(0, 20))

        # Mobile number
        lbl_5 = Label(self.register_window, text="Enter the Mobile Number",
                      font=("bold", 8)).pack()
        entry_5 = Entry(self.register_window,
                        textvar=self.mob).pack(pady=(0, 20))

        # Submit Button
        Button(self.register_window, text="Submit", width=20, bg="brown",
               fg="white", command=self.add_data).pack()

    def add_data(self):
        print("Accessing the database . . ")
        # Get values for adding
        name = self.name.get()
        age = self.age.get()
        address = self.add.get()
        b_group = self.var.get()
        quantity = self.quantity.get()
        mobile_number = self.mob.get()

        print(quantity)

        # Accessing the database (blood.db)
        try:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS %s(name,age,address,quantity,bgroup,mobile)" % (self.tablename))
            self.connection.execute("INSERT INTO %s VALUES(?,?,?,?,?,?)" % (self.tablename),
                                    (name, age, address, quantity, b_group, mobile_number))
            self.connection.commit()
            tkinter.messagebox.showinfo("Message", "Registration Successfull")
            self.connection.close()
        except Exception as e:
            tkinter.messagebox.showinfo(
                "Error", "Insertion Failed : " + str(e))
