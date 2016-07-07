from tkinter import *
import sys
from tkinter.filedialog import askopenfilename, asksaveasfilename


def PyIDE():
    def openFile():
        file = askopenfilename(defaultextension=".py",
                               filetypes=[("Python .py", ".py"), ("Python .pyw", ".pyw")])

        if file != "":
            with open(file, "r") as openfile:
                input.delete(0.0, END)
                input.insert(0.0, openfile.read())

    def save():
        file = asksaveasfilename(defaultextension=".py",
                                 filetypes=[("Python .py", ".py"), ("Python .pyw", ".pyw")])

        if file != "":
            with open(file, "w") as saveFile:
                saveFile.write(input.get(0.0, END))

    class TextRedirector(object):
        def __init__(self, widget, tag="stdout"):
            self.widget = widget
            self.tag = tag

        def write(self, str):
            output.delete(0.0, END)
            self.widget.configure(state="normal")
            self.widget.insert("end", str, (self.tag,))
            self.widget.configure(state="disabled")
            self.widget.see(END)

    def run():
        exec(input.get(0.0, END))

    rootInterpreter = Tk()
    rootInterpreter.title("Terminal")
    rootInterpreter.geometry("200x200")
    rootInterpreter.minsize(200, 200)

    menu = Menu(rootInterpreter)
    rootInterpreter.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open", command=openFile)
    filemenu.add_command(label="Save", command=save)
    filemenu.add_command(label="Save As", state=DISABLED)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=sys.exit)

    output = Text(rootInterpreter, state=DISABLED, wrap="word")
    output.configure(state=NORMAL)
    output.configure(state=DISABLED)
    output.pack(side=TOP, expand=YES, fill=BOTH)

    input = Text(rootInterpreter)
    input.focus()
    input.pack(side=BOTTOM, expand=YES, fill=BOTH)

    sys.stderr = TextRedirector(output, "stderr")

    sys.stdout = TextRedirector(output, "stdout")

    rootInterpreter.mainloop()

    # rootInterpreter.protocol("WM_DELETE_WINDOW", closeApp)


PyIDE()
