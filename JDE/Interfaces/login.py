import logging
import PIL.Image
import PIL.ImageTk
from tkinter import *
import threading

loginLog = logging.getLogger(__name__)

loginLog.debug("Atempting to read settings file")
try:
    config = {}
    exec(open("JDE/Settings/settings.conf").read(), config)
    loginLog.debug("System settings Detected!")
except Exception as e:
    loginLog.error(str(e))


class login:
    def reposition(self, event):
        if self.tempWidth != self.window.winfo_width() or self.tempHeight != self.window.winfo_height():
            loginLog.debug("Running reposition")
            def reposFrame():
                self.frame.place_configure(x=int(self.window.winfo_width() / 3), y=self.window.winfo_height() / 3,
                                           width=int(int(self.window.winfo_width()) / 3),
                                           height=int(int(self.window.winfo_height()) / 3))

            if self.background_image.width() != self.window.winfo_width() or self.background_image.height() != self.window.winfo_height():
                def reposBackground():
                        if config["resizeBackground"]:
                            try:
                                self.canvas.delete("Background")
                                background_image_resized = self.bg_image.resize((self.window.winfo_width(), self.window.winfo_height()),
                                                                                PIL.Image.ANTIALIAS)
                                self.background_image = PIL.ImageTk.PhotoImage(background_image_resized)
                                self.canvas.backgroundImage = self.background_image
                                self.canvas.create_image(0, 0, image=self.background_image, anchor=NW, tag="Background")
                            except Exception as e:
                                loginLog.error(str(e))

                threading.Thread(target=reposFrame, daemon=True).start()
                threading.Thread(target=reposBackground, daemon=True).start()
            self.tempWidth = self.window.winfo_width()
            self.tempHeight = self.window.winfo_height()

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

        self.reposition(self)

        def configureWindow():
            self.window.bind("<Configure>", self.reposition)

        threading.Thread(target=configureWindow, daemon=True).start()

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
            self.bg_image = PIL.Image.open(self.bg, "r")
            self.background_image = PIL.ImageTk.PhotoImage(self.bg_image)
            self.canvas.bgImage = self.background_image
            self.canvas.create_image(0, 0, image=self.background_image, anchor=NW, tag="Background")
            self.canvas.configure(highlightthickness=0, relief=FLAT)
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

        self.tempWidth = self.window.winfo_width()
        self.tempHeight = self.window.winfo_height()

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
