from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

class Notepad:
    root = Tk()
    root.title("untitled notepad")
    root.geometry("700x400")
    TextArea = Text(root, font=("arial",15))
    menubar = Menu(root)
    FileMenu = Menu(menubar, tearoff=0)
    EditMenu = Menu(menubar, tearoff=0)
    HelpMenu = Menu(menubar, tearoff=0)

    #scrollbar = ScrollBar(TextArea)
    file = None

    def __init__(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.TextArea.grid(sticky=N+S+E+W)

        self.FileMenu.add_command(label="New")
        self.FileMenu.add_command(label="save")
        self.FileMenu.add_command(label="Open")
        self.FileMenu.add_command(label="Exit")

        self.menubar.add_cascade(label="Select All        ctrl+A")
        self.menubar.add_cascade(label="Cut        ctrl+x")
        self.menubar.add_cascade(label="Copy        ctrl+c")
        self.menubar.add_cascade(label="File",menu=self.FileMenu)
        self.menubar.add_cascade(label="File",menu=self.EditMenu)
        self.menubar.add_cascade(label="File",menu=self.HelpMenu)