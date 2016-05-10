from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
import gc

Canvas.image = None


class imageViewer:
    def fullScreen(self):
        try:
            if self.max == 0:
                self.window.attributes('-fullscreen', True)
                self.max = 1
            else:
                self.window.attributes('-fullscreen', False)
                self.max = 0
        except:
            pass

    def openimage(self):
        self.picfile = askopenfilename()
        if self.picfile:
            Canvas.image = PhotoImage(file=self.picfile)
            self.canvas.create_image(0, 0, anchor=NW, image=Canvas.image)
            self.canvas.configure(self.canvas, scrollregion=(0, 0, Canvas.image.width(), Canvas.image.height()))

    def createWidgets(self):
        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open Image", command=self.openimage)
        self.filemenu.add_command(label="Fullscreen", command=self.fullScreen)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.window.destroy)

        self.yscrollbar = Scrollbar(self.window)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.xscrollbar = Scrollbar(self.window, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)

        self.canvas = Canvas(self.window, width=self.canvas_width, height=self.canvas_height,
                             yscrollcommand=self.yscrollbar.set,
                             xscrollcommand=self.xscrollbar.set)
        # button = Button(root,text="Open",command=openimage)
        # button.pack(side=BOTTOM)
        self.canvas.pack(side=TOP, expand=YES, fill=BOTH)
        self.yscrollbar.config(command=self.canvas.yview)
        self.xscrollbar.config(command=self.canvas.xview)

    def createWindow(self):
        self.window = Toplevel(self.master)
        self.window.title("Image Viewer")
        # self.window.config(bg="white")
        self.createWidgets()

        self.window.attributes('-fullscreen', False)
        self.max = 0

        self.window.mainloop()

    def __init__(self, master):
        self.master = master
        self.canvas_width = 800
        self.canvas_height = 600
        self.createWindow()
