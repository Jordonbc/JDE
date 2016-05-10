from tkinter import *


class info:
    def createWindow(self):
        self.window = Tk()
        self.window.configure(bg=self.menuColour)
        self.window.title("JDE Information Panel")
        self.window.geometry("500x300")

        # glassOSLogo = PhotoImage(file="GlassOS/Glass_OS_Logo.png")
        # glassOSPicture = Button(rootInfo, image=glassOSLogo)

        glassOSPicture = Label(self.window, text="JDE " + self.version,
                               font=("Space Bd BT Bold", 32, ""), fg="#FF0000", bg=self.menuColour)
        glassOSPicture.pack()

        text = Label(self.window, text="You are currently running JDE " + self.version + ".", bg=self.menuColour)

        text.pack(expand=YES, fill=BOTH)

        self.window.mainloop()

    def __init__(self):
        try:
            config = {}
            exec(open("JDE/Settings/settings.conf").read(), config)

            self.menuColour = config["colour"]
            self.version = config["version"]

        except:
            pass

        self.createWindow()
