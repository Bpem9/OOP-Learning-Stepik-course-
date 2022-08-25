class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.arr = [cell(0) for _ in range(max_length)]

    def __getitem__(self, index):
        self.__index_checking(index)
        return self.arr[index] if isinstance(self.arr[index], int) else self.arr[index].value

    def __setitem__(self, index, value):
        self.__index_checking(index)
        self.arr[index].value = value

    def __str__(self):
        return ' '.join(str(cell) for cell in self.arr)

    def __index_checking(self, index):
        if not isinstance(index, int) or not -self.max_length <= index < self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')


class Integer:
    def __init__(self, start_value):
        self.__num = start_value

    @property
    def value(self):
        return self.__num

    @value.setter
    def value(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        self.__num = value

    def __repr__(self):
        return str(self.value)

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел

ar_int[1] = 10
print(ar_int[1])
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError
