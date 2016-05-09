from tkinter import *


class start:
    def createWidgets(self):
        self.allPrograms = Frame(self.window)
        self.allPrograms.configure(bg=self.menuColour)

        self.window.geometry("242x310")

        self.hardwareMonitorButton = Button(self.allPrograms, text="Hardware Monitor", state=DISABLED,
                                            width=100,
                                            bg=self.menuColour)
        self.musicPlayerButton = Button(self.allPrograms, text="Music Player - Experimental", state=DISABLED,
                                        width=100, bg=self.menuColour)
        self.infoButton = Button(self.allPrograms, text="Glass OS Info Panel", state=DISABLED, width=100,
                                 bg=self.menuColour)
        self.CustomAppLauncherButton = Button(self.allPrograms, text="Custom App Launcher", state=DISABLED, width=100,
                                              bg=self.menuColour)
        self.terminalButton = Button(self.allPrograms, text="Terminal", state=DISABLED, width=100, bg=self.menuColour)
        self.restartButton = Button(self.allPrograms, text="Restart", state=DISABLED, width=100, bg=self.menuColour)
        self.jpadButton = Button(self.allPrograms, text="Jpad", state=DISABLED, width=100, bg=self.menuColour)
        self.chkUpdates = Button(self.allPrograms, text="Check for Updates", state=DISABLED, width=100,
                                 bg=self.menuColour)
        self.settingsButton = Button(self.allPrograms, text="Settings", state=DISABLED, width=100, bg=self.menuColour)
        self.fileExplorer = Button(self.allPrograms, text="File Explorer", state=DISABLED, width=100,
                                   bg=self.menuColour)
        self.shutdown = Button(self.allPrograms, text="Shutdown", command=sys.exit, width=100, bg=self.menuColour)

        self.musicPlayerButton.pack()
        self.jpadButton.pack()
        self.chkUpdates.pack()
        self.CustomAppLauncherButton.pack()
        self.fileExplorer.pack()
        self.infoButton.pack()
        self.hardwareMonitorButton.pack()
        self.settingsButton.pack()
        self.terminalButton.pack()
        self.restartButton.pack()
        self.shutdown.pack()

        self.allPrograms.pack()

    def createWindow(self):
        self.window = Tk()
        self.window.configure(bg=self.menuColour)
        self.window.focus()
        self.window.title("Start")

        self.createWidgets()

        def noFocus(event):
            self.window.destroy()

        self.window.bind("<FocusOut>", noFocus)

        self.window.mainloop()

    def __init__(self, colour=None, posX=0, posY=1000):
        self.menuColour = colour
        self.root_windowX = posX
        self.root_windowY = posY

        self.createWindow()
