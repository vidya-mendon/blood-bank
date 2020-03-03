from tkinter import *
import sqlite3 as sql
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.plots = plt
        self.plots.xlabel("Blood Groups")
        self.plots.ylabel("Quantity Available")
        self.plots.title("Values")
        self.table = "blood_bank"
        self.connection = sql.connect("Blood.db")
        self.cursor = self.connection.cursor()
        self.x = ["O+", "O-", "A+", "A-",
                  "B+", "B-", "AB+", "AB-"]
        self.y = []

    def show_graph(self):
        self.get_data_from_database()
        self.plots.plot(self.x, self.y)
        self.plots.show()

    def get_data_from_database(self):
        for index, blood_group in enumerate(self.x):
            rows = self.cursor.execute(
                "select * from %s where bgroup='%s'" % (self.table, blood_group)).fetchall()
            quantity = 0
            for value in rows:
                quantity += value[3]
            self.y.append(quantity)
