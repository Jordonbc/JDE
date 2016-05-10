import logging
import os
import time
import webbrowser
from tkinter import *

from JDE.Interfaces import start
from Programs import jpad
from Programs import info

desktopLog = logging.getLogger("desktop.py")

desktopLog.debug("Atempting to read settings file")
try:
    config = {}
    exec(open("JDE/Settings/settings.conf").read(), config)
    desktopLog.debug("System settings Detected!")
except Exception as e:
    desktopLog.error(str(e))


class desktop:
    def box(self, event):
        desktopLog.debug("Running box")
        try:
            if (self.clicked == False):
                self.searchvar.set("")
                self.search.config(fg="black")
                self.clicked = True
        except Exception as e:
            desktopLog.error(str(e))

    def search_internet(self, event):
        desktopLog.debug("Running search_internet")
        # TODO: Find a way to implement a browser
        try:
            webbrowser.open_new_tab("https://www.google.co.uk/#q=" + self.searchvar.get().replace(" ", "+"))
        except Exception as e:
            desktopLog.error(str(e))

    def reposition(self, event):
        desktopLog.debug("Running reposition")
        try:
            self.cHeight = self.window.winfo_height()
            self.cWidth = self.window.winfo_width()

            self.centerWidth = self.window.winfo_x() + int(int(self.cWidth) / 2)
            self.centerHeight = self.window.winfo_y() + int(int(self.cHeight) / 2)

            self.screenCenter = str(self.centerWidth) + "+" + str(self.centerHeight)

            # self.startPic.place_configure(x=int(0), y=int(self.cHeight) - 55)

            self.search.place_configure(x=0, y=int(self.cHeight) - 55, height=55, width=300)

            # versionText.place(x=int(cWidth) - 300, y=int(cHeight) - 120)

            self.toolbar.place_configure(x=258, y=int(self.cHeight) - 55, height=55, width=int(self.cWidth))

            self.notifcationBar.place_configure(x=int(self.cWidth) - 500, y=int(self.cHeight) - 55, height=55,
                                                width=500)

            self.windowX = self.window.winfo_x()
            self.windowY = (self.window.winfo_y() + self.window.winfo_height())

            # displayTime.pack_configure(side=RIGHT)
        except Exception as e:
            desktopLog.error(str(e))

    def fullScreen(self, event):
        desktopLog.debug("Running fullscreen")
        try:
            if self.max == 0:
                self.window.attributes('-fullscreen', True)
                self.max = 1
            else:
                self.window.attributes('-fullscreen', False)
                self.max = 0
        except Exception as e:
            desktopLog.error(str(e))

    def clockTick(self):
        desktopLog.debug("Running clockTick")
        try:
            self.desktopRefresh()
            # cTime = time.strftime("%H:%M:%S")
            # print(cTime)
            self.cTime = time.strftime("%H:%M")
            if self.cTime != self.time1:
                self.time1 = self.cTime
                self.displayTime.configure(text=self.cTime)
                self.displayTime.after(1000, self.clockTick)
            else:
                self.displayTime.after(1000, self.clockTick)
        except Exception as e:
            desktopLog.error(str(e))

    def createSearch(self):
        desktopLog.debug("Running createSearch")
        try:
            self.searchText = Label(self.window, text="Search for: ")
            self.searchvar = StringVar()
            self.search = Entry(self.window, textvariable=self.searchvar, font=(14), bg=self.menuColour)
            self.search.bind("<Button-1>", self.box)
            self.search.bind("<Return>", self.search_internet)
            self.search.place(x=0, y=350, height=50, width=100)
            self.search.insert(0, "Search")
        except Exception as e:
            desktopLog.error(str(e))

    def contextMenuPopup(self, event):
        desktopLog.debug("Running contextMenuPopup")
        try:
            # start.start(self.menuColour, event.x_root, event.y_root)
            self.contextMenu.post(event.x_root, event.y_root)
        except Exception as e:
            desktopLog.error(str(e))

    def nothing(self):
        pass

    def addContextMenuEntry(self, label="New Label", command=nothing, state=NORMAL):
        self.contextMenu.add_command(label=label, command=command, state=state)

    def createContextMenu(self):
        desktopLog.debug("Running createContextMenu")
        try:
            self.contextMenu = Menu(self.window, tearoff=0)

            self.contextMenu.add_command(label="Refresh", command=self.desktopRefresh)
            self.contextMenu.add_command(label="Jpad", command=jpad.jpadEditor)
            self.contextMenu.add_command(label="File Explorer", state=DISABLED)
            self.contextMenu.add_command(label="Hardware Monitor", state=DISABLED)
            self.contextMenu.add_command(label="Music Player", state=DISABLED)
            self.contextMenu.add_command(label="Info", command=info.info)
            self.contextMenu.add_command(label="Terminal", state=DISABLED)
            self.contextMenu.add_command(label="Settings", state=DISABLED)
            self.contextMenu.add_command(label="Restart", state=DISABLED)
            self.contextMenu.add_command(label="Shutdown", command=sys.exit)

        except Exception as e:
            desktopLog.error(str(e))

    def desktopRefresh(self):
        try:
            desktopLog.debug("Running desktopRefresh")
            self.fileImage = PhotoImage(file="JDE/Images/file.png")
            self.f = []
            self.l = []
            fName = []
            self.place = []
            files = -1
            self.space = 80

            prefix = self.user_dir

            # prefix = os.path.expanduser("~")
            def openFile(self):
                # print(fName)
                self.fileURL = prefix + "/Desktop/" + str(fName[files])
                # print(fileURL)
                self.a = jpad
                self.a.jpadEditor(str(self.fileURL))

            def openFolder(self):
                self.folderURL = prefix + "/Desktop/" + str(fName[files])
                self.file_Explorer(self.folderURL)

            try:
                for self.file in os.listdir(self.prefix + "/Desktop"):
                    if self.file not in fName:
                        self.l.append(Label(self.window, text=self.file, font=("Arial", 11, "bold")))

                        files += 1

                        fName.append(self.file)
                        self.place.append(files)

                        self.space += 80

                        self.f.append(Button(self.window, image=self.fileImage))

                        self.f[files].place(x=int(80), y=int(20) + self.space, width=40, height=40)

                        if ".txt" in self.file:
                            self.f[files].bind("<Double-Button-1>", openFile)
                        elif ".py" in self.file:
                            self.f[files].bind("<Double-Button-1>", openFile)
                        elif ".pyw" in self.file:
                            self.f[files].bind("<Double-Button-1>", openFile)
                        elif os.path.isdir(prefix + "/Desktop/" + self.file):
                            self.f[files].bind("<Double-Button-1>", openFolder)
                        else:
                            pass
                        self.l[files].place(x=int(100), y=int(70) + self.space, anchor=CENTER)
            except:
                pass
        except Exception as e:
            desktopLog.error(str(e))

    def refresh(self):
        desktopLog.debug("Running refresh")
        try:
            self.desktopRefresh()
        except Exception as e:
            desktopLog.error(str(e))

    def createStart(self):
        desktopLog.debug("Running createStartPic")
        try:
            start.start(self.menuColour, int(0), int(self.window.winfo_height()))
        except Exception as e:
            desktopLog.error(str(e))
            pass

    def createBackground(self):
        try:
            desktopLog.debug("Running createBackground")
            self.background_image = PhotoImage(file=self.background)
            self.canvas.create_image(0, 0, image=self.background_image, anchor=NW)
        except Exception as e:
            desktopLog.error(str(e))

    def createIcon(self):
        desktopLog.debug("Running createIcon")
        try:
            self.window.wm_iconbitmap("System/JordonOS Logo.ico")
        except Exception as e:
            desktopLog.error(str(e))

    def createWindow(self):
        desktopLog.debug("Running createWindow")
        try:
            self.window = Tk()
            self.window.title("Jordon's Desktop Environment")
            self.window.geometry(self.widthHeight)
            self.window.minsize(640, 360)
            self.windowX = self.window.winfo_x()
            self.windowY = self.window.winfo_y()

            self.canvas = Canvas(self.window, width=self.width, height=self.height)
            self.canvas.pack(expand=YES, fill=BOTH)

            self.toolbar = Frame(self.window, bg=self.menuColour)
            self.toolbar.place(x=0, y=int(self.height) - 55)

            self.notifcationBar = Frame(self.window, bg=self.menuColour)
            self.notifcationBar.place(x=int(self.width) - 100, y=int(self.height) - 55)

            self.window.attributes('-fullscreen', True)
            self.max = 1

            self.displayTime = Label(self.notifcationBar, text=self.cTime, bg=self.menuColour, font=("System", 20))
            self.displayTime.pack(side=RIGHT)

            self.window.bind("<F5>", self.refresh)

            self.window.bind("<Escape>", self.fullScreen)
            self.window.bind("<Configure>", self.reposition)

            self.window.bind("<Button-3>", self.contextMenuPopup)

            self.createBackground()
            self.createIcon()
            self.createSearch()
            self.createContextMenu()
            self.clockTick()

            self.window.mainloop()
        except Exception as e:
            desktopLog.error(str(e))

    def __init__(self, windowTitle="Desktop Environment", width="1920", height="1080", minWidth="", username=""):
        desktopLog.debug("Running __init__")
        try:
            self.width = width
            self.height = height
            self.widthHeight = str(self.width + "x" + self.height)
            self.windowTitle = windowTitle
            self.cTime = time.strftime("%H:%M")
            self.time1 = ""
            self.menuColour = config["colour"].replace("\n", "")
            self.startMenuPic = config["startPic"].replace("\n", "")
            self.background = config["background"]
            self.user_dir = config["userDirs"] + username + "/"
            self.prefix = self.user_dir
            self.clicked = 0

            self.createWindow()

        except Exception as e:
            desktopLog.error(str(e))
