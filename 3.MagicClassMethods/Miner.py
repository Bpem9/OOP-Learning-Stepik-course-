from random import randint

class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False
    @property
    def is_mine(self):
        return self.__is_mine
    @is_mine.setter
    def is_mine(self, value):
        self.__bval(value)
        self.__is_mine = value

    @property
    def is_open(self):
        return self.__is_open
    @is_open.setter
    def is_open(self, value):
        self.__bval(value)
        self.__is_open = value

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, value):
        self.__nval(value)
        self.__number = value

    def __bval(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
    def __nval(self, value):
        if not isinstance(value, int) or not 0 <= value <= 8:
            raise ValueError("недопустимое значение атрибута")
    def __bool__(self):
        return not self.is_open

    def __repr__(self):
        if self.is_open:
            return '*' if self.__is_mine is True else str(self.__number)
        else:
            return '#'


class GamePole:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self, N, M, total_mines):
        self.__N = N
        self.__M = M
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self.__M)) for _ in range(self.__N))
        self.total_mines = total_mines
        self.init_pole()
    def __del__(self):
        GamePole.__instance = None

    @property
    def pole(self):
        return self.__pole_cells

    def __ival(self, i, j):
        if not isinstance(i, int) or not 0 <= i <= self.__N:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        if not isinstance(j, int) or not 0 <= j <= self.__M:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
    def open_cell(self, i, j):
        self.__ival(i, j)
        self.__pole_cells[i][j].is_open = True
    def show_pole(self):
        for line in self.__pole_cells:
            print(*line)
    def init_pole(self):
        for i in range(self.__N):
            for j in range(self.__M):
                self.__pole_cells[i][j].is_mine = False
                self.__pole_cells[i][j].is_open = True
        m = 0
        while m < self.total_mines:
            i = randint(0, self.__N-1)
            j = randint(0, self.__M-1)
            if self.__pole_cells[i][j].is_mine:
                continue
            self.__pole_cells[i][j].is_mine = True
            m += 1
        self.__numbers()
    def __numbers(self):
        checkers = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(self.__N):
            for j in range(self.__M):
                self.__pole_cells[i][j].number = 0
                for cell in checkers:
                    i1, j1 = cell
                    if not self.__pole_cells[i][j].is_mine and 0 <= i + i1 < self.__N and 0 <= j + j1 < self.__M:
                        if self.__pole_cells[i+i1][j+j1].is_mine:
                            self.__pole_cells[i][j].number += 1


p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"
p.show_pole()
print('=='*10)
# try:
#     cell.is_mine = 10
# except ValueError as e:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# try:
#     cell.number = 10
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
p.init_pole()
p.init_pole()
p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1
print(m)
p.show_pole()
# assert m == 10, "на поле расставлено неверное количество мин"