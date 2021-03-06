import logging
import os
import time
import webbrowser
import PIL.Image
import PIL.ImageTk
from tkinter import *

from JDE.Interfaces import start
from Programs import jpad
from Programs import info
from Programs import imageViewer
from Programs import minesweeper
from Programs import terminal
from Programs.webEdit import htmlEdit as webEdit
from Programs import FileBrowser
import threading

desktopLog = logging.getLogger(__name__)

desktopLog.debug("Atempting to read settings file")
try:
    config = {}
    exec(open("JDE/Settings/settings.conf").read(), config)
    desktopLog.debug("System settings Detected!")
except Exception as e:
    desktopLog.error(str(e))


class desktop:
    def box(self, event):
        desktopLog.debug("Running " + desktop.box.__name__)
        try:
            if (self.clicked == False):
                self.searchvar.set("")
                self.search.config(fg="black")
                self.clicked = True
        except Exception as e:
            desktopLog.error(str(e))

    def search_internet(self, event):
        desktopLog.debug("Running " + desktop.search_internet.__name__)
        # TODO: Find a way to implement a browser
        try:
            webbrowser.open_new_tab("https://www.google.co.uk/#q=" + self.searchvar.get().replace(" ", "+"))
        except Exception as e:
            desktopLog.error(str(e))

    def reposition(self, event):
        if self.tempWidth != self.window.winfo_width() or self.tempHeight != self.window.winfo_height():
            desktopLog.debug("Running " + desktop.reposition.__name__)
            try:
                self.cHeight = self.window.winfo_height()
                self.cWidth = self.window.winfo_width()

                self.centerWidth = self.window.winfo_x() + int(int(self.cWidth) / 2)
                self.centerHeight = self.window.winfo_y() + int(int(self.cHeight) / 2)

                self.screenCenter = str(self.centerWidth) + "+" + str(self.centerHeight)

                # self.startPic.place_configure(x=int(0), y=int(self.cHeight) - 55)
                def searchPlaceRepos():
                    self.search.place_configure(x=0, y=int(self.cHeight) - 55, height=55, width=300)

                # versionText.place(x=int(cWidth) - 300, y=int(cHeight) - 120)

                def toolbarPlaceRepos():
                    self.toolbar.place_configure(x=258, y=int(self.cHeight) - 55, height=55, width=int(self.cWidth))

                def notifyBarPlaceRepos():
                    self.notifcationBar.place_configure(x=int(self.cWidth) - 500, y=int(self.cHeight) - 55, height=55,
                                                        width=500)

                def resizeBackground():
                    if self.background_image.width() != self.cWidth or self.background_image.height() != self.cHeight:
                        if config["resizeBackground"]:
                            try:
                                self.canvas.delete("background")
                                backgroundResized = self.image.resize((self.cWidth, self.cHeight), PIL.Image.ANTIALIAS)
                                self.background_image = PIL.ImageTk.PhotoImage(backgroundResized)
                                self.canvas.backgroundImage = self.background_image
                                self.canvas.create_image(0, 0, image=self.background_image, anchor=NW, tag="background")
                            except Exception as e:
                                desktopLog.error(str(e))

                threading.Thread(target=searchPlaceRepos, daemon=True).start()
                threading.Thread(target=toolbarPlaceRepos, daemon=True).start()
                threading.Thread(target=notifyBarPlaceRepos, daemon=True).start()
                threading.Thread(target=resizeBackground, daemon=True).start()

                self.windowX = self.window.winfo_x()
                self.windowY = (self.window.winfo_y() + self.window.winfo_height())

                # displayTime.pack_configure(side=RIGHT)
            except Exception as e:
                desktopLog.error(str(e))

    def fullScreen(self, event):
        desktopLog.debug("Running " + desktop.fullScreen.__name__)
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
        desktopLog.debug("Running " + desktop.clockTick.__name__)
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
        desktopLog.debug("Running " + desktop.createSearch.__name__)
        try:
            self.searchText = Label(self.window, text="Search for: ")
            self.searchvar = StringVar()
            self.search = Entry(self.window, textvariable=self.searchvar, font=(14), bg=self.menuColour, relief=FLAT)
            self.search.bind("<Button-1>", self.box)
            self.search.bind("<Return>", self.search_internet)
            self.search.place(x=0, y=350, height=50, width=100)
            self.search.insert(0, "Search")
        except Exception as e:
            desktopLog.error(str(e))

    def contextMenuPopup(self, event):
        desktopLog.debug("Running " + desktop.contextMenuPopup.__name__)
        try:
            # start.start(self.menuColour, event.x_root, event.y_root)
            self.contextMenu.post(event.x_root, event.y_root)
            self.contextMenu.focus()
        except Exception as e:
            desktopLog.error(str(e))

    def nothing(self):
        pass

    def addContextMenuEntry(self, label="New Label", command=nothing, state=NORMAL):
        self.contextMenu.add_command(label=label, command=command, state=state)

    def createContextMenu(self):
        desktopLog.debug("Running " + desktop.createContextMenu.__name__)
        try:
            self.contextMenu = Menu(self.window, tearoff=0, bg=self.contextMenuColour, bd=0, relief=FLAT)

            self.games = Menu(self.contextMenu, bg=self.contextMenuColour, tearoff=0, relief=FLAT, bd=0)
            self.applications = Menu(self.contextMenu, bg=self.contextMenuColour, tearoff=0, relief=FLAT, bd=0)

            def FileBrowserRun():
                FileBrowser.fileBrowser(self.window, os.path.realpath(os.path.dirname(__file__+"../../../")))

            def minesweeperRun():
                minesweeper.mine_sweeper(self.window, self.menuColour)

            def jpadEdit():
                jpad.jpadEditor(self.window)

            def viewImage():
                imageViewer.imageViewer(self.window)

            def runTerminal():
                terminal.terminal(self.window)

            def webEditor():
                webEdit.webEdit(self.window)
            # def runPymonitor():
            #     pyMonitor.pyMonitor(self.window)

            self.contextMenu.add_command(label="Refresh", command=self.desktopRefresh)

            self.contextMenu.add_cascade(label="Games", menu=self.games)
            self.contextMenu.add_cascade(label="Applications", menu=self.applications)

            self.applications.add_command(label="File Browser", command=FileBrowserRun)
            self.applications.add_command(label="Jpad", command=jpadEdit)
            self.applications.add_command(label="WebEdit", command=webEditor)
            self.applications.add_command(label="View Images", command=viewImage)
            self.games.add_command(label="Minesweeper", command=minesweeperRun)
            self.applications.add_command(label="File Explorer", state=DISABLED)
            self.applications.add_command(label="Hardware Monitor", state=DISABLED)
            self.applications.add_command(label="Music Player", state=DISABLED)
            self.applications.add_command(label="Info", command=info.info)
            self.applications.add_command(label="Terminal", state=ACTIVE, command=runTerminal)
            self.applications.add_command(label="Settings", state=DISABLED)
            self.contextMenu.add_command(label="Restart", state=DISABLED)
            self.contextMenu.add_command(label="Exit", command=sys.exit)

        except Exception as e:
            desktopLog.error(str(e))

    def desktopRefresh(self):
        try:
            desktopLog.debug("Running " + desktop.desktopRefresh.__name__)
            self.fileImage = PhotoImage(file="JDE/Images/file.png")
            self.f = []
            self.l = []
            fName = []
            self.place = []
            files = -1
            self.space = 80

            prefix = self.user_dir

            # prefix = os.path.expanduser("~")
            def openFile(event):
                # print(fName)
                self.fileURL = prefix + "/Desktop/" + str(fName[files])
                # print(fileURL)
                self.a = jpad
                self.a.jpadEditor(self.window, str(self.fileURL))

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

                        self.f.append(Button(self.window, image=self.fileImage, relief=FLAT))

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
            except Exception as e:
                desktopLog.error(str(e))
        except Exception as e:
            desktopLog.error(str(e))

    def refresh(self):
        desktopLog.debug("Running " + desktop.refresh.__name__)
        try:
            self.desktopRefresh()
        except Exception as e:
            desktopLog.error(str(e))

    def createStart(self):
        desktopLog.debug("Running " + desktop.createStart.__name__)
        try:
            start.start(self.menuColour, int(0), int(self.window.winfo_height()))
        except Exception as e:
            desktopLog.error(str(e))

    def createBackground(self):
        try:
            desktopLog.debug("Running " + desktop.createBackground.__name__)
            self.image = PIL.Image.open(self.background)
            self.background_image = PIL.ImageTk.PhotoImage(self.image)
            self.canvas.background_image = self.background_image
            self.canvas.create_image(0, 0, image=self.background_image, anchor=NW, tag="background")
            self.canvas.configure(relief=FLAT, highlightthickness=0)
        except Exception as e:
            desktopLog.error(str(e))

    def createIcon(self):
        desktopLog.debug("Running" + desktop.createIcon.__name__)
        try:
            self.window.wm_iconbitmap("System/JordonOS Logo.ico")
        except Exception as e:
            desktopLog.error(str(e))

    def createWindow(self):
        desktopLog.debug("Running " + desktop.createWindow.__name__)
        try:
            self.window = Tk()
            self.window.title("Jordon's Desktop Environment")
            self.window.geometry(self.widthHeight)
            self.window.minsize(640, 360)
            self.windowX = self.window.winfo_x()
            self.windowY = self.window.winfo_y()
            self.tempWidth = self.window.winfo_width()
            self.tempHeight = self.window.winfo_height()

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

            def manFefresh(event):
                self.refresh()

            self.window.bind("<F5>", manFefresh)

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
        desktopLog.debug("Running " + desktop.__init__.__name__)
        try:
            self.width = width
            self.height = height
            self.widthHeight = str(self.width + "x" + self.height)
            self.windowTitle = windowTitle
            self.cTime = time.strftime("%H:%M")
            self.time1 = ""
            self.menuColour = config["colour"].replace("\n", "")
            self.contextMenuColour = config["contextMenuColour"].replace("\n", "")
            self.startMenuPic = config["startPic"].replace("\n", "")
            self.background = config["background"]
            self.user_dir = config["userDirs"] + username + "/"
            self.prefix = self.user_dir
            self.clicked = 0

            self.createWindow()

        except Exception as e:
            desktopLog.error(str(e))
