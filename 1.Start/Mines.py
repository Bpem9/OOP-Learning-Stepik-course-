import random
class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = True
    def symbol(self):
        if self.fl_open == True:
            return '*' if self.mine == True else str(self.around_mines)
        else:
            return '#'

class GamePole:
    def __init__(self, N, M):
        self.n = N
        self.m = M
        self.init()

    def show(self):
        for row in self.pole:
            return [[el.symbol() for el in row] for row in self.pole]


    def around(self):
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.n):
            for y in range(self.n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x+i < self.n and 0 <= y+j < self.n))
                    self.pole[x][y].around_mines = mines

    def init(self):
        self.pole = [[Cell() for i in range(self.n)] for j in range(self.n)]
        l = 0
        while l != self.m:
            cell = self.pole[random.randint(0, self.n - 1)][random.randint(0, self.n - 1)]
            if cell.mine == False:
                cell.mine = True
                l += 1
        self.around()





pole = GamePole(9, 18)
