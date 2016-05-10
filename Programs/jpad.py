import logging
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

jpadLog = logging.getLogger("jpad.py")

jpadLog.debug("Atempting to read settings file")
try:
    config = {}
    exec(open("JDE/Settings/settings.conf").read(), config)
    jpadLog.debug("System settings Detected!")
except Exception as e:
    jpadLog.error(str(e))


class jpadEditor:
    def minimize(self):
        jpadLog.debug("Running minimize")
        try:
            self.appFocus = 0
        except Exception as e:
            jpadLog.error(str(e))

    def closeApp(self):
        jpadLog.debug("Running closeApp")
        try:
            # self.appIcon.destroy()
            self.window.destroy()
        except Exception as e:
            jpadLog.error(str(e))

    def focusApp(self):
        jpadLog.debug("Running focusApp")
        try:
            if self.appFocus == 0:
                self.window.focus_force()
                self.appFocus = 1

            else:
                self.appFocus = 0
                self.window.focus_set()
        except Exception as e:
            jpadLog.error(str(e))

    def createMenu(self):
        jpadLog.debug("Running createMenu")
        try:
            self.menu = Menu(self.window)
            self.window.config(menu=self.menu)
            self.filemenu = Menu(self.menu)
            self.menu.add_cascade(label="File", menu=self.filemenu)
            self.filemenu.add_command(label="New", command=self.new)
            self.filemenu.add_command(label="Open...", command=self.open_command)
            self.filemenu.add_command(label="Save", command=self.save_command)
            self.filemenu.add_command(label="Save As", command=self.saveAs_command)
            self.filemenu.add_separator()
            self.filemenu.add_command(label="Exit", command=self.exit_command)

            self.fontMenu = Menu(self.menu)
            self.menu.add_cascade(label="Font", menu=self.fontMenu)
            self.fontMenu.add_command(label="font", command=self.chfont)
        except Exception as e:
            jpadLog.error(str(e))

    def new(self):
        jpadLog.debug("Running new")
        try:
            self.window.title("Jpad Text Editor" + "     File: New File")
            self.textPad.delete(0.0, END)
        except Exception as e:
            jpadLog.error(str(e))

    def exit_command(self):
        jpadLog.debug("Running exit_command")
        try:
            self.closeApp()
        except Exception as e:
            jpadLog.error(str(e))

    def saveAs_command(self):
        jpadLog.debug("Running saveAs_command")
        try:
            self.jpadFile = asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text Files", ".txt"), ("Python .py", ".py"),
                                                         ("Python .pyw", ".pyw"),
                                                         ("All Files", ".*")])
            self.window.title("Jpad Text Editor" + "     File: " + str(self.jpadFile))
            self.jpadFile = open(str(self.jpadFile), "w")
            if self.jpadFile != None:
                # slice off the last character from get, as an extra return is added
                self.data = str(self.textPad.get(0.0, END)).replace("\n", "")
                self.jpadFile.write(self.data)
                self.jpadFile.close()
        except Exception as e:
            jpadLog.error(str(e))

    def save_command(self):
        jpadLog.debug("Running save_command")
        try:
            self.jpadFile = open(str(self.jpadFile), "w")
            if self.jpadFile != None:
                # slice off the last character from get, as an extra return is added
                self.data = str(self.textPad.get(0.0, END)).replace("\n", "")
                self.jpadFile.write(self.data)
                self.jpadFile.close()
            else:
                self.saveAs_command()
        except Exception as e:
            jpadLog.error(str(e))

    def open_command(self):
        jpadLog.debug("Running open_command")
        try:
            self.jpadFile = askopenfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", ".txt"), ("Python .py", ".py"),
                                                       ("Python .pyw", ".pyw"),
                                                       ("All Files", ".*")], )

            self.window.title("Jpad Text Editor" + "     File: " + str(self.jpadFile))
            self.jpadFile = open(str(self.jpadFile), "r")
            if self.jpadFile != None:
                self.contents = self.jpadFile.read()
                self.textPad.delete(0.0, END)
                self.textPad.insert(0.0, self.contents)
                self.jpadFile.close()
        except Exception as e:
            jpadLog.error(str(e))

    def chfont(self):
        def apply():
            try:
                self.textPad.configure(font=(self.font1.get(), int(self.font2.get()), self.font3.get()))
                self.font[0] = self.font1.get()
                self.font[1] = self.font2.get()
                self.font[2] = self.font3.get()

                self.rootFont.destroy()
            except:
                self.msg.configure(text="Whoops, something went wrong while applying your font!")

        self.rootFont = Tk()
        self.rootFont.title("Font")
        self.rootFont.geometry("320x110")

        self.font1 = Entry(self.rootFont)
        self.font2 = Entry(self.rootFont)
        self.font3 = Entry(self.rootFont)

        self.font1.insert(0, self.font[0])
        self.font2.insert(0, self.font[1])
        self.font3.insert(0, self.font[2])

        self.applyButton = Button(self.rootFont, text="Apply Font", command=apply)
        self.msg = Label(self.rootFont)

        self.font1.pack()
        self.font2.pack()
        self.font3.pack()
        self.applyButton.pack()
        self.msg.pack()

        self.rootFont.mainloop()

    def createWidgets(self):
        self.textPad = Text(self.window)
        self.textPad.configure(bg=self.menuColour)
        self.textPad.configure(font=(self.font[0], int(self.font[1]), self.font[2]))
        self.textPad.focus()

        try:
            if self.jpadFile != None:
                self.window.title("Jpad Text Editor" + "     File: " + str(self.jpadFile))
                self.jpadFile = open(str(self.jpadFile), "r")
                self.contents = self.jpadFile.read()
                self.textPad.delete(0.0, END)
                self.textPad.insert(0.0, self.contents)
                self.jpadFile.close()
        except:
            pass

        self.textPad.pack(expand=YES, fill=BOTH)

    def createWindow(self):
        self.window = Toplevel(self.master)
        self.sWidth = self.window.winfo_screenwidth()
        self.sHeight = self.window.winfo_screenheight()
        self.window.title("Jpad")
        self.window.geometry(self.widthHeight)
        self.window.maxsize(self.sWidth, self.sHeight)
        self.window.minsize("200", "200")
        self.createWidgets()
        self.createMenu()

        self.window.bind("<Unmap>", self.minimize)
        self.window.protocol("WM_DELETE_WINDOW", self.closeApp)

        self.window.mainloop()

    def __init__(self, master, file=None):
        self.jpadFile = file
        self.master = master
        self.width = "500"
        self.height = "400"
        self.appFocus = 1
        self.widthHeight = self.width + "x" + self.height
        try:
            self.menuColour = config["colour"].replace("\n", "")
        except:
            self.menuColour = None
        self.font = ["Arial", "11", "normal"]

        self.createWindow()


if __name__ == "__main__":
    jpadEditor(None)
