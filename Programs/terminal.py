__author__ = "Jordonbc"

__version__ = "1.1.0"
from tkinter import *

default_stdin = sys.stdin
default_stdout = sys.stdout
default_stderr = sys.stderr

disabledCommands = ["help()", "exit()", "sys.exit()", "quit()"]
availableCommands = ["set", "bg", "fg", "clear"]


def commands():
    print("Available Commands:")
    print("set bg [HEX COLOUR]")
    print("set fg [HEX COLOUR]")
    print("clear")
    print("run [file]")


class terminal:
    class TextRedirector(object):
        def __init__(self, widget, tag="stdout"):
            self.widget = widget
            self.tag = tag

        def write(self, str):
            self.widget.configure(state="normal")
            self.widget.insert("end", str, (self.tag,))
            self.widget.configure(state="disabled")
            self.widget.see(END)

    def __init__(self, master, command=None):
        def run(command=None):
            if input.get() != "":
                print(input.get())
                if input.get().startswith("set "):
                    if input.get().startswith("set bg "):
                        try:
                            output.configure(bg=str(input.get()).replace("set bg ", "").replace("\n", ""))
                            input.configure(bg=str(input.get()).replace("set bg ", "").replace("\n", ""))
                        except Exception as e:
                            print(str(e))
                    elif input.get().startswith("set fg "):
                        try:
                            if str(input.get()).replace("set fg ", "").replace("\n", "").lower() == "#ffffff":
                                output.configure(insertbackground="#000000")
                                input.configure(insertbackground="#000000")
                            elif str(input.get()).replace("set fg ", "").replace("\n", "").lower() == "#000000":
                                output.configure(insertbackground="#ffffff")
                                input.configure(insertbackground="#ffffff")
                            output.configure(fg=str(input.get()).replace("set fg ", "").replace("\n", ""))
                            input.configure(fg=str(input.get()).replace("set fg ", "").replace("\n", ""))
                        except Exception as e:
                            print(str(e))

                if input.get() == "clear":
                    print("\n" * 25)
                elif input.get() in disabledCommands:
                    input.delete(0, END)
                    print("Command is disabled.")

                elif input.get().startswith("run "):
                    try:
                        exec(open(str(input.get()).replace("run ", ""), "r").read())
                    except Exception as e:
                        print(str(e))

                else:
                    try:
                        exec(input.get())
                    except Exception as e:
                        print(str(e))

            input.delete(0, END)

        def closeApp():
            sys.stdin = default_stdin
            sys.stdout = default_stdout
            sys.stderr = default_stderr
            rootTerminal.destroy()

        rootTerminal = Toplevel(master)
        rootTerminal.title("Terminal")
        rootTerminal.geometry("400x300")
        rootTerminal.minsize(200, 200)
        rootTerminal.configure(bg="#000000")

        output = Text(rootTerminal, state=DISABLED, height=10, bg="#000000", fg="#FFFFFF", wrap="word", relief=FLAT)
        output.configure(state=NORMAL)
        output.insert(END, "JDE Terminal V " + __version__ + "\n")
        output.insert(END, "Type commands() to see available commands\n")
        output.configure(state=DISABLED)
        output.pack(side=TOP, expand=YES, fill=BOTH)

        input = Entry(rootTerminal, width=400, bg="#000000", fg="#FFFFFF", relief=FLAT)
        input.focus()
        input.bind("<Return>", run)
        input.pack(side=BOTTOM)

        output.configure(insertbackground="#ffffff")
        input.configure(insertbackground="#ffffff")

        sys.stdin = self.TextRedirector(output, "stdin")
        sys.stderr = self.TextRedirector(output)
        sys.stdout = self.TextRedirector(output)

        rootTerminal.protocol("WM_DELETE_WINDOW", closeApp)
        rootTerminal.mainloop()