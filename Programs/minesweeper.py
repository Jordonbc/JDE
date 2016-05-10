import random
from tkinter import *
from tkinter import messagebox


def mine_sweeper(master, colour="#39d972"):
    class MineSweeperCell(Label):
        '''Creates a minesweeper square that is part of a grid'''

        def __init__(self, master):
            '''Makes an unmarked minesweeper grid square; 0 represents blank and 9 represents bomb'''
            # create cell label
            Label.__init__(self, master, height=1, width=2, text='', bg=colour, bd=5, font=('Arial', 10), relief=RAISED)
            self.value = ''  # store cell value
            self.clicked = False  # store whether it is clicked
            self.flagged = False  # store whether it is flagged
            self.checked = False  # store whether it has been checked (for 0's)
            # color dictionary
            self.colorMap = ['', 'blue', 'darkgreen', 'red', 'purple', 'maroon', 'cyan', 'black', 'gray']
            # attaches mouse clicks to functions
            self.bind('<Button-1>', self.reveal)
            self.bind('<Button-3>', self.flag)

        def get_value(self):
            '''Returns value of cell'''
            return self.value

        def is_clicked(self):
            '''Tells if cell has been clicked'''
            return self.clicked

        def is_flagged(self):
            '''Tells if cell is flagged'''
            return self.flagged

        def flag(self, event):
            '''Flags the square if player believes there is a bomb'''
            if self.flagged == False and self.clicked == False and int(
                    self.master.flags) > 0 and self.master.winner == False:
                # if no flag
                self['text'] = '*'
                self.master.subFlag()  # subtract from remaining bombs
                self.flagged = True  # set self.flagged to true
            elif self.flagged == True and self.clicked == False and int(self.master.flags) < int(
                    self.master.bombs) and self.master.winner == False:  # if it is already flagged
                self['text'] = ''  # remove flag
                self.master.addFlag()  # add to remaining bombs
                self.flagged = False  # set self.flagged to False

        def set_value(self, value):
            '''Sets the value of the cell'''
            self.value = value

        def reveal(self, event):
            '''Reveals the hidden cell value'''
            if self.clicked == False:
                if 0 < self.value < 9:
                    if self.flagged == False and self.master.loser == False:  # checks if it is a valid click
                        self['relief'] = SUNKEN
                        # set text and color
                        self['text'] = str(self.value)
                        self['fg'] = self.colorMap[self.value]
                        self['bg'] = 'gray65'
                        self["bd"] = 5
                        self.clicked = True
                        self.master.CheckWin()
                elif self.value == 9:
                    if self.master.winner == False and self.flagged == False:  # if it is a bomb
                        self['text'] = '*'  # make text a bomb
                        self['bg'] = 'red'  # make background red
                        self["bd"] = 5
                        self['relief'] = SUNKEN
                        self.clicked = True
                        self.master.CheckLoss()
                elif self.value == 0:
                    if self.flagged == False and self.master.loser == False:
                        self['text'] = ''
                        self.master.uncover_other_blank(self)
                        self['relief'] = SUNKEN
                        self['bg'] = 'gray65'
                        self["bd"] = 5
                        self.clicked = True
                        self.master.CheckWin()

        def expose(self):
            '''Exposes surrounding zeros'''
            if self.clicked == False:
                if 0 < self.value < 9:
                    if self.flagged == False and self.master.loser == False:
                        self['text'] = str(self.value)  # set text and color
                        self['fg'] = self.colorMap[self.value]
                        self['relief'] = SUNKEN
                        self['bg'] = 'gray65'
                        self["bd"] = 5
                        self.clicked = True
                        self.master.CheckWin()
                elif self.value == 9:
                    if self.flagged == False:  # if it is a bomb
                        self['text'] = '*'  # make text a bomb
                        self['bg'] = 'red'  # make background red
                        self["bd"] = 5
                        self['relief'] = SUNKEN
                        self.clicked = True
                elif self.value == 0:
                    if self.flagged == False and self.master.loser == False:
                        self['text'] = ''
                        self.master.uncover_other_blank(self)
                        self['relief'] = SUNKEN
                        self['bg'] = 'gray65'
                        self["bd"] = 5
                        self.clicked = True
                        self.master.CheckWin()

    class MineSweeperGrid(Frame):
        '''Creates a minesweeper grid to play the game on'''

        def __init__(self, master, width, height, numBombs):
            '''Creates a grid with the given width, height, and number of bombs'''
            Frame.__init__(self, master, bg=colour, bd=5)
            self.grid()
            # sets the number of bombs
            self.bombs = numBombs
            # sets the number of flags
            self.flags = numBombs
            # create something to set the bombs up around each square
            self.count = 0
            self.winner = False
            self.loser = False
            # create the label that will keep track of flags
            self.flagTrack = Label(self, text=self.flags, bg=colour, height=1, width=2, font=("Arial", 36))
            self.flagTrack.grid(row=height, columnspan=width)
            # create the bombs
            self.cells = {}
            for i in range(int(numBombs)):
                y = random.randint(0, int(width) - 1)
                x = random.randint(0, int(height) - 1)
                while (x, y) in self.cells.keys():
                    y = random.randint(0, int(width) - 1)
                    x = random.randint(0, int(height) - 1)
                self.cells[(x, y)] = MineSweeperCell(self)
                self.cells[(x, y)].set_value(9)
                self.cells[(x, y)].grid(row=x, column=y)
            # create the other cells
            for row in range(int(height)):
                for column in range(int(width)):
                    if (row, column) not in self.cells.keys():
                        self.count = 0
                        if (row + 1, column) in self.cells.keys():
                            if self.cells[(row + 1, column)].get_value() == 9:
                                self.count = self.count + 1
                        if (row + 1, column + 1) in self.cells.keys():
                            if self.cells[(row + 1, column + 1)].get_value() == 9:
                                self.count = self.count + 1
                        if (row, column + 1) in self.cells.keys():
                            if self.cells[(row, column + 1)].get_value() == 9:
                                self.count = self.count + 1
                        if (row - 1, column + 1) in self.cells.keys():
                            if self.cells[(row - 1, column + 1)].get_value() == 9:
                                self.count = self.count + 1
                        if (row - 1, column) in self.cells.keys():
                            if self.cells[(row - 1, column)].get_value() == 9:
                                self.count = self.count + 1
                        if (row - 1, column - 1) in self.cells.keys():
                            if self.cells[(row - 1, column - 1)].get_value() == 9:
                                self.count = self.count + 1
                        if (row, column - 1) in self.cells.keys():
                            if self.cells[(row, column - 1)].get_value() == 9:
                                self.count = self.count + 1
                        if (row + 1, column - 1) in self.cells.keys():
                            if self.cells[(row + 1, column - 1)].get_value() == 9:
                                self.count = self.count + 1
                        self.cells[(row, column)] = MineSweeperCell(self)
                        self.cells[(row, column)].set_value(self.count)
                        self.cells[(row, column)].grid(row=row, column=column)

        def subFlag(self):
            '''Subtracts one from the flagcount'''
            self.flags = int(self.flags) - 1
            self.flagTrack['text'] = str(self.flags)

        def addFlag(self):
            '''Adds one from the flagcount'''
            self.flags = int(self.flags) + 1
            self.flagTrack['text'] = str(self.flags)

        def uncover_other_blank(self, cell):
            '''Uncovers all blank squares adjacent to the marked square'''
            for coords, mine in self.cells.items():
                if mine == cell:
                    c = coords
            x = int(float(c[0]))
            y = int(float(c[1]))
            cell.checked = True
            # checks all cells in radius
            if (x + 1, y) in self.cells.keys():
                if self.cells[(x + 1, y)].checked == False:
                    self.cells[(x + 1, y)].expose()
            if (x + 1, y + 1) in self.cells.keys():
                if self.cells[(x + 1, y + 1)].checked == False:
                    self.cells[(x + 1, y + 1)].expose()
            if (x, y + 1) in self.cells.keys():
                if self.cells[(x, y + 1)].checked == False:
                    self.cells[(x, y + 1)].expose()
            if (x - 1, y + 1) in self.cells.keys():
                if self.cells[(x - 1, y + 1)].checked == False:
                    self.cells[(x - 1, y + 1)].expose()
            if (x - 1, y) in self.cells.keys():
                if self.cells[(x - 1, y)].checked == False:
                    self.cells[(x - 1, y)].expose()
            if (x - 1, y - 1) in self.cells.keys():
                if self.cells[(x - 1, y - 1)].checked == False:
                    self.cells[(x - 1, y - 1)].expose()
            if (x, y - 1) in self.cells.keys():
                if self.cells[(x, y - 1)].checked == False:
                    self.cells[(x, y - 1)].expose()
            if (x + 1, y - 1) in self.cells.keys():
                if self.cells[(x + 1, y - 1)].checked == False:
                    self.cells[(x + 1, y - 1)].expose()

        def CheckWin(self):
            '''Checks if player won'''
            doneList = []
            for key in self.cells.keys():
                if self.cells[key].clicked == True and self.cells[key].value != 9:
                    doneList.append(self.cells[key])
            if len(doneList) == int(height) * int(width) - int(numBombs):
                messagebox.showinfo('Minesweeper', 'Congratulations -- you won!', parent=self)
                self.winner = True
                playagain()

        def CheckLoss(self):
            '''Checks if player lost'''
            self.loser = True
            self.flagTrack['text'] = '0'
            messagebox._show('Minesweeper', 'You Lose!', parent=self)
            for key in self.cells.keys():
                if self.cells[key].value == 9:
                    self.cells[key].flagged = False
                    self.cells[key].expose()
            playagain()

    def playagain():
        again = messagebox.askyesno("Minesweeper", "Do you want to play again?")
        if again == TRUE:
            root.destroy()
            __init__()

        else:
            root.destroy()

    def __init__():
        global width
        global height
        global numBombs
        width = 10
        height = 10
        numBombs = 30
        global root
        root = Toplevel(master)
        root.maxsize(270, 335)
        root.minsize(270, 335)
        root.title('Minesweeper')
        global game
        game = MineSweeperGrid(root, width, height, numBombs)
        game.mainloop()

    __init__()