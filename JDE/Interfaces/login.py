import logging
from tkinter import *

loginLog = logging.getLogger(__name__)


class login:
    def reposition(self, event):
        loginLog.debug("Running reposition")
        self.frame.place_configure(x=int(self.window.winfo_width() / 3), y=self.window.winfo_height() / 3,
                                   width=int(int(self.window.winfo_width()) / 3),
                                   height=int(int(self.window.winfo_height()) / 3))

    def callback(self, event):
        loginLog.debug("Running callback")
        self.username = self.user.get()

        try:
            self.file = open(self.userDirs + self.username.lower() + ".profile", "r")
            self.file.close()
        except:
            self.message.configure(text="Err: Username or password is incorrect!")

        self.file = open(self.userDirs + self.username.lower() + ".profile", "r")

        self.line = self.file.readlines()

        self.password = self.passw.get()
        if self.username == self.line[1].strip() and self.password == self.line[2].strip():
            self.message.configure(text="Logged in.")
            self.active = self.username
            self.tmp = open("active", "w")
            self.tmp.write(self.active)
            self.window.destroy()
            # user_dir = line[4]
        else:
            self.message.configure(text="Err: Username and password don't match the profile")

    def createWidgets(self):
        loginLog.debug("Running createWidgets")
        self.titleLabel = Label(self.frame, text="Login to " + self.windowTitle + "\n", bg=self.bgColour)
        self.usertitle = Label(self.frame, text="---Username---", bg=self.bgColour)
        self.passtitle = Label(self.frame, text="---Password---", bg=self.bgColour)
        self.message = Label(self.frame, bg=self.bgColour)
        self.user = Entry(self.frame)
        self.passw = Entry(self.frame, show="*")
        self.go = Button(self.frame, text="Log in!", bg="#00FF00")

        self.titleLabel.pack()
        self.usertitle.pack()
        self.user.pack()
        self.passtitle.pack()
        self.passw.pack()
        self.go.pack()
        self.message.pack()

        self.user.focus()

        self.go.bind("<Button-1>", self.callback)
        self.go.bind("<Return>", self.callback)
        self.passw.bind("<Return>", self.callback)
        self.window.bind("<Configure>", self.reposition)

        self.window.mainloop()

    def createColour(self):
        loginLog.debug("Running createColour")
        try:
            self.window.configure(bg=self.bgColour)
        except:
            pass

    def createIcon(self):
        loginLog.debug("Running createIcon")
        try:
            self.window.wm_iconbitmap(self.icon)
        except:
            pass

    def createBackground(self):
        loginLog.debug("Running createBackground")
        try:
            self.background_image = PhotoImage(file=self.bg)
            self.canvas.create_image(0, 0, image=self.background_image, anchor=NW)
            self.canvas.pack(expand=YES, fill=BOTH)
        except Exception as e:
            loginLog.error(str(e))

    def fullScreen(self, event):
        loginLog.debug("Running fullscreen")
        if self.max == 0:
            self.window.attributes('-fullscreen', True)
            self.max = 1
        else:
            self.window.attributes('-fullscreen', False)
            self.max = 0

    def createWindow(self):
        loginLog.debug("Running createWindow")
        self.window = Tk()
        self.window.title(self.windowTitle)
        self.window.geometry(self.widthHeight)
        self.canvas = Canvas(self.window, width=self.bgWidth, height=self.bgHeight)
        self.frame = Frame(self.canvas)
        self.frame.configure(bg=self.bgColour)

        self.canvas.pack()

        self.window.attributes('-fullscreen', True)
        self.max = 1
        self.window.bind("<Escape>", self.fullScreen)

    def __init__(self, windowTitle="Login Window", widthHeight="1920x1080", icon="", bgColour=None, bg=None,
                 bgWidth="350", bgHeight="250",
                 userDirs=""):
        loginLog.debug("Running __init__")
        self.windowTitle = windowTitle
        self.widthHeight = widthHeight
        self.icon = icon
        self.bgColour = bgColour
        self.bg = bg
        self.bgWidth = bgWidth
        self.bgHeight = bgHeight
        self.userDirs = userDirs
        self.username = ""
        self.active = ""

        self.createWindow()
        self.createBackground()
        self.createIcon()
        self.createWidgets()
