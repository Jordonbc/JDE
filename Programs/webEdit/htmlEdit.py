__author__ = "Jordonbc"
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import askstring
import webbrowser



settings = {}

try:
    exec(open("Programs/webEdit/settings", "r").read(), settings)
except:
    print("Settings Currupted!, Resetting")
    with open("Programs/webEdit/settings", "w") as file:
        file.write("""fgColour = '#000000'
bgColour = '#FFFFFF'
cursor = '#FFFFFF'""")

class webEdit:
    def open(self):
        self.saveLocation = askopenfilename(filetypes=[("HTML", "html"), ("All Files", "*")])
        if self.saveLocation != "":
            self.textbox.delete(0.0, END)
            self.textbox.insert(0.0, open(self.saveLocation, "r").read().strip())
        self.root.title("WebEdit - " + str(self.saveLocation))

    def save(self):
        self.saveLocation = asksaveasfilename(filetypes=[("HTML", "html"), ("All Files", "*")])
        if self.saveLocation != "":
            file = open(self.saveLocation, "w")
            file.write(str(self.textbox.get(0.0, END)).strip())
            file.close()
        self.root.title("WebEdit - " + str(self.saveLocation))

    def new(self):
        if self.textbox.get(0.0, END) == "\n":
            # template = askopenfile(defaultextension="HET", filetypes=[("Template", "HET"), ("All Files", "*")])
            template = open("Programs/webEdit/Templates/HTML 5/Default.HET", "r")
            if template != None:
                template = template.read()
                self.textbox.delete(0.0, END)
                self.textbox.insert(0.0, template)
        else:
            if askyesno(title="Sure?", message="Are you sure?"):
                # template = askopenfile(defaultextension="HET", filetypes=[("Template", "HET"), ("All Files", "*")])
                template = open("Programs/webEdit/Templates/HTML 5/Default.HET", "r")
                if template != None:
                    template = template.read()
                    self.textbox.delete(0.0, END)
                    self.textbox.insert(0.0, template)
        self.root.title("WebEdit - New File")

    def createMenu(self):
        menu = Menu(self.root)
        menu.configure(bg=settings["bgColour"], fg=settings["fgColour"])
        fileMenu = Menu(menu)
        fileMenu.configure(bg=settings["bgColour"], fg=settings["fgColour"])
        viewMenu = Menu(menu)
        viewMenu.configure(bg=settings["bgColour"], fg=settings["fgColour"])
        snippetsMenu = Menu(menu)
        snippetsMenu.configure(bg=settings["bgColour"], fg=settings["fgColour"])
        headlineMenu = Menu(menu)
        headlineMenu.configure(bg=settings["bgColour"], fg=settings["fgColour"])
        self.root.configure(menu=menu)
        menu.add_cascade(label="File", menu=fileMenu)
        menu.add_cascade(label="Code Snippets", menu=snippetsMenu)

        def paragraph():
            self.textbox.insert(INSERT, "<p></p>")

        def div():
            self.textbox.insert(INSERT, "<div></div>")

        def br():
            self.textbox.insert(INSERT, "<br>")

        def headline_1():
            self.textbox.insert(INSERT, "<h1></h1>")

        def headline_2():
            self.textbox.insert(INSERT, "<h2></h2>")

        def headline_3():
            self.textbox.insert(INSERT, "<h3></h3>")

        def headline_4():
            self.textbox.insert(INSERT, "<h4></h4>")

        def headline_5():
            self.textbox.insert(INSERT, "<h5></h5>")

        def headline_6():
            self.textbox.insert(INSERT, "<h6></h6>")

        def insertImage():
            location = askstring(title="Image", prompt="Image")
            self.textbox.insert(INSERT, "<img src='" + location + "'/>")

        def Link():
            address = askstring(title="Link", prompt="Link Address")
            text = askstring(title="Link", prompt="Text")
            self.textbox.insert(INSERT, "<a href='" + address + "'>"+text+"</a>")

        def openSettings():
            self.textbox.delete(0.0, END)
            self.textbox.insert(0.0, open("settings").read())

        def view_default():
            if self.saveLocation != "":
                webbrowser.open_new(self.saveLocation)

        snippetsMenu.add_command(label="Paragraph", command=paragraph)
        snippetsMenu.add_command(label="Division", command=div)
        snippetsMenu.add_command(label="Image", command=insertImage)
        snippetsMenu.add_command(label="Link", command=Link)
        snippetsMenu.add_command(label="Break", command=br)
        snippetsMenu.add_cascade(label="Headline", menu=headlineMenu)
        headlineMenu.add_command(label="1", command=headline_1)
        headlineMenu.add_command(label="2", command=headline_2)
        headlineMenu.add_command(label="3", command=headline_3)
        headlineMenu.add_command(label="4", command=headline_4)
        headlineMenu.add_command(label="5", command=headline_5)
        headlineMenu.add_command(label="6", command=headline_6)

        fileMenu.add_command(label="New", command=self.new)
        fileMenu.add_command(label="Save", command=self.save)
        fileMenu.add_command(label="Open", command=self.open)
        fileMenu.add_separator()
        fileMenu.add_command(label="Settings", command=openSettings)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.root.destroy)

        menu.add_command(label="View in  browser", command=view_default)

        # menu.add_cascade(label="View", menu=viewMenu)

        # viewMenu.add_command(label="Default program", command=view_default)

    def createWidgets(self):
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.textbox = Text(self.root)
        self.textbox.pack(side=TOP, expand=YES, fill=BOTH)
        self.textbox.configure(bg=settings["bgColour"], fg=settings["fgColour"], insertbackground=settings["cursor"],
                               yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.textbox.yview)

        def saveShortcut(event):
            self.save()

        def openShortcut(event):
            self.open()

        def newShortcut(event):
            self.new()

        self.textbox.bind("<Control-s>", saveShortcut)
        self.textbox.bind("<Control-o>", openShortcut)
        self.textbox.bind("<Control-n>", newShortcut)

    def __init__(self, master):
        self.saveLocation = ""
        self.root = Toplevel(master)
        self.root.title("WebEdit")
        self.root.configure(bg=settings["bgColour"])
        self.createWidgets()
        self.createMenu()
        self.new()

        self.root.mainloop()
