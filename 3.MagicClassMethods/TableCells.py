class TableValues:
    def __init__(self, rows, cols, type_data):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def __type_valid(self, value):
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')
    def __index_valid(self, coords):
        i, j = coords
        if not isinstance(i, int) or not 0 <= i <= self.rows:
            raise IndexError('неверный индекс i')
        if not isinstance(j, int) or not 0 <= j <= self.cols:
            raise IndexError('неверный индекс j')
    def show(self):
        for item in self.table:
            print(*item)
        print('='*10)

    def __getitem__(self, coords):
        self.__index_valid(coords)
        i, j = coords
        return self.table[i][j]

    def __setitem__(self, coords, value):
        self.__index_valid(coords)
        self.__type_valid(value)
        i, j = coords
        self.table[i][j].data = value

    def __iter__(self):
        for row in self.table:
            yield (el.data for el in row)


class Cell:
    def __init__(self, data):
        self.__data = data

    def __repr__(self):
        return str(self.__data)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

tbl = TableValues(4, 4, int)
tbl[1, 3] = 12
tbl.show()
for row in tbl:
    for el in row:
        print(el)
