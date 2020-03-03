from tkinter import *
import sqlite3


class Showinfo:
    def __init__(self, parent):
        self.show_window = Toplevel(parent)
        self.show_window.title("Blood Bank Information")
        self.show_window.geometry("750x300")
        self.connection = sqlite3.connect("Blood.db")
        self.cursor = self.connection.cursor()
        self.table = "blood_bank"
        self.labels = ['Name', 'Age', 'Address',
                       'Quantity', 'Blood Group', 'Phone Number']

    def show_information(self, blood_group):
        print(blood_group.get())
        print(self.show_window.winfo_width())
        rows = self.read_database(blood_group.get())
        if len(rows) != 0:
            self.print_labels()
            for rowindex, row in enumerate(rows):
                for columnindex, item in enumerate(row):
                    e = Entry(self.show_window,
                              borderwidth=1, justify=CENTER, width=15)
                    e.insert(0, item)
                    e.grid(row=rowindex+1, column=columnindex, sticky=NSEW)
        else:
            Label(self.show_window, text='%s' % ("No Records Found for blood group %s" % (blood_group.get())),
                  borderwidth=1, justify=CENTER).grid(row=0, column=0, sticky=NSEW)

    def print_labels(self):
        for index, value in enumerate(self.labels):
            Label(self.show_window, text='%s' % (value),
                  borderwidth=1, justify=CENTER, width=15).grid(row=0, column=index, sticky=NSEW)

    def read_database(self, blood_group):
        try:
            if blood_group != '':
                rows = self.cursor.execute(
                    "select * from %s where bgroup='%s'" % (self.table, blood_group))
                return rows.fetchall()
            else:
                rows = self.cursor.execute(
                    "select * from %s" % (self.table))
                return rows.fetchall()
        except Exception as e:
            print("Failed connecting database : ", e)
            self.connection.close()
