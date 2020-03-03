# Importing essential packages
from tkinter import *
import tkinter.messagebox

# Importing class
from package.Showinfo import Showinfo


class Search:
    def __init__(self, parent):

        # Setting up the window
        self.need_window = Toplevel(parent)
        self.need_window.title("Search Blood Bank")
        self.need_window.geometry("500x400")

        # Adding Input variables
        self.name = StringVar()
        self.var = StringVar()

        # Heading
        lbl_0 = Label(self.need_window,
                      text="Search Blood Bank", bg="grey", width="300",
                      height="2", font=("Calibri", 18), fg="white"
                      ).pack()
        Label(self.need_window, text="").pack()

        # Name
        lbl_1 = Label(self.need_window, text="Name (optional)",
                      font=("bold", 8)).pack()
        entry_1 = Entry(self.need_window, textvar=self.name).pack(pady=10)

        # Blood group
        lbl_2 = Label(self.need_window, text="Blood Group",
                      width=20, font=("bold", 8)).pack()
        r1 = Radiobutton(self.need_window, text="A Positive", variable=self.var,
                         value="A+").pack()
        r2 = Radiobutton(self.need_window, text="B Positive", variable=self.var,
                         value="B+").pack()
        r3 = Radiobutton(self.need_window, text="O Positive", variable=self.var,
                         value="O+").pack()
        r4 = Radiobutton(self.need_window, text="A Negative", padx=30, variable=self.var,
                         value="A-").pack()
        r5 = Radiobutton(self.need_window, text="B Negative", padx=30, variable=self.var,
                         value="B-").pack()
        r6 = Radiobutton(self.need_window, text="O Negative", padx=30, variable=self.var,
                         value="O-").pack()
        r7 = Radiobutton(self.need_window, text="AB Positive", padx=30, variable=self.var,
                         value="AB+").pack()
        r8 = Radiobutton(self.need_window, text="AB Negative", padx=30, variable=self.var,
                         value="AB-").pack()

        # Submit Button
        Button(self.need_window, text="Search", width=20, bg="brown",
               fg="white", command=self.show).pack(pady=10)

    def show(self):
        # Setting up the window
        show_window = Showinfo(self.need_window)
        show_window.show_information(self.var)
