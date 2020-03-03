# Importing essential packages
from tkinter import *
import tkinter.messagebox
import sqlite3

# Importing other windows
from package.Add import Add
from package.Search import Search
from package.Graph import Graph


class Redline:
    def __init__(self, geometry="400x400", title="Redline"):

        # Setting Window dimentions
        print("Root Window created")
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(geometry)

        # Heading
        Label(
            text="Redline", bg="brown", width="300",
            height="2", font=("Calibri", 18), fg="white"
        ).pack()

        # Search Blood Button
        Button(
            text="Inspect Logs", width="30", height="2",
            bg="brown", fg="white", command=self.create_need_window
        ).pack(pady=(10, 10))

        # Add Blood Button
        Button(
            text="Add Blood", width="30", height="2",
            bg="brown", fg="white", command=self.create_register_window
        ).pack(pady=(10, 10))

        # Visualize
        Button(
            text="Visualize Quantity", width="30", height="2",
            bg="brown", fg="white", command=self.visualize
        ).pack(pady=(10, 10))

        # Exit Button
        Button(
            text="Exit", width="30", height="2",
            bg="brown", fg="white", command=self.exit_window
        ).pack(pady=(10, 10))

    def visualize(self):
        # Creates a graph of the plots
        graph_window = Graph()
        graph_window.show_graph()

    def create_need_window(self):
        # Creates a Need blood window and adds it to the parent
        need_window = Search(self.window)

    def create_register_window(self):
        # Creates a Register blood window and adds it to the parent
        register_window = Add(self.window)

    def exit_window(self):
        # Quits the window
        self.window.destroy()
