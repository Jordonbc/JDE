from tkinter import *
import os

path = "E:/programming/"

class fileBrowser:
    def update(self):
        self.path = os.path.realpath(self.path)
        self.folderListbox.delete(0, END)
        self.fileListbox.delete(0, END)

        self.addressBox.delete(0, END)
        self.addressBox.insert(0, self.path)

        self.folderListbox.insert(0, "Back")

        for item in os.listdir(self.path):
            if not self.path.startswith("."):
                if os.path.isdir(os.path.join(self.path, item)):
                    self.folderListbox.insert(END, item)
                else:
                    self.fileListbox.insert(END, item)


    def createWidgets(self):
        self.folderListbox = Listbox(self.root)
        self.fileListbox = Listbox(self.root)

        self.addressBox = Entry(self.root)
        self.addressBox.insert(0, self.path)

        self.folderListbox.insert(0, "Back")

        def test(event):
            if self.folderListbox.get(self.folderListbox.curselection()) == "Back":
                self.path = os.path.abspath(os.path.join(self.path, os.pardir))
            else:
                self.path = os.path.join(self.path, self.folderListbox.get(self.folderListbox.curselection()))
            self.update()

        def refresh(event):
            self.path = os.path.abspath(self.addressBox.get())
            self.update()

        def upd(event):
            self.update()

        self.update()

        self.addressBox.bind("<Return>", refresh)
        self.folderListbox.bind("<F5>", upd)

        self.folderListbox.bind('<Double-1>', test)

        self.addressBox.pack(side=TOP, expand=NO, fill=X)
        self.folderListbox.pack(side=LEFT, expand=YES, fill=BOTH)
        self.fileListbox.pack(side=LEFT, expand=YES, fill=BOTH)
    def __init__(self, master, path):
        self.path = os.path.abspath(os.path.dirname(os.path.realpath(path)))
        self.root = Toplevel(master)
        self.root.title("File Browser")
        self.createWidgets()

        self.root.mainloop()