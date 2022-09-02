class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table = {}

    def __getitem__(self, coords):
        self.__cellvalid(coords)
        return self.table[coords]

    def __setitem__(self, coords, data):
        if not coords in self.table.keys():
            self.table[coords] = Cell(data)
        else:
            self.table[coords].value = data
        self.__rows_counting()
        self.__cols_counting()


    def __rows_counting(self):
        rlist = []
        self.rows = 0
        for coord in self.table.keys():
            i, j = coord
            rlist.append(i)
        for i in list(set(rlist)):
            self.rows += 1
        return self.rows
    def __cols_counting(self):
        clist = []
        self.cols = 0
        for coord in self.table.keys():
            i, j = coord
            clist.append(j)
        for i in list(set(clist)):
            self.cols += 1
        return self.cols

    def __cellvalid(self, coords):
        if not self.table[coords]:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __removevalid(self, coords):
        if not coords in self.table.keys():
            raise IndexError('ячейка с указанными индексами не существует')

    def add_data(self, row, col, data):
        self.table[(row, col)] = Cell(data)
        self.__rows_counting()
        self.__cols_counting()

    def remove_data(self, row, col):
        self.__removevalid((row, col))
        self.table[(row, col)] = None
        self.__rows_counting()
        self.__cols_counting()

dd = SparseTable()
dd.add_data(1, 2, 'Привет')
dd.add_data(1, 3, 'Звони в полицию!')
dd.add_data(2, 3, 'Алло')
dd.add_data(3, 4, 'Валерий?')
try:
    dd.remove_data(5, 5)
except Exception as ex:
    print('='*10)
    print(f'Ошибка поймана: {ex}')
    print('='*10)
dd.remove_data(1, 3)
print(dd.cols)
dd.add_data(0, 1, 'Леонтьев?')
dd[1, 2] = 'Пока, пока!'
dd[5, 5] = 'Прием, прием'
print(dd.cols)
