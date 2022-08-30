class Cell:
    def __init__(self):
        self.value = 0
        self.is_free = True

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
    def __val(self, coord):
        print(coord)
        if not -len(self.pole) < coord < len(self.pole):
            raise IndexError('неверный  индекс клетки')
    def __opval(self, coord):
        i, j = coord
        if not self.pole[i][j].is_free:
            raise ValueError('клетка уже занята')

    def __getitem__(self, coord):
        for item in coord:
            if isinstance(item, int):
                self.__val(item)
        i, j = coord
        if isinstance(j, slice):
            return tuple(cell.value for cell in self.pole[i][j])
        elif isinstance(i, slice):
            return tuple(cell[j].value for cell in self.pole[i])
        return self.pole[i][j].value

    def __setitem__(self, coord, value):
        for item in coord:
            if isinstance(item, int):
                self.__val(item)
        self.__opval(coord)
        i, j = coord
        self.pole[i][j].value = value
        self.pole[i][j].is_free = False


    def clear(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole)):
                self.pole[i][j].value = 0
                self.pole[i][j].is_free = True
    def show_pole(self):
        for i in self.pole:
            print(*[j.value for j in i])
        print('='*10)

game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
# game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
game.show_pole()
# v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
print(v2, sep='\n')