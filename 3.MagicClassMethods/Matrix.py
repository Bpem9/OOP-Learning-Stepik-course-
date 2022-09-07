class Matrix:
    def __init__(self, rows_or, cols=0, fill_value=0):
        if type(rows_or) == int:
            if not isinstance(rows_or, int) or not isinstance(cols, int):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.rows = rows_or
            self.cols = cols
            if not isinstance(fill_value, (int, float)):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.fill_value = fill_value
            self.matrix = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.rows = len(rows_or)
            self.cols = len(rows_or[0])
            if not all(len(r) == self.cols for r in rows_or) or \
                    not all(self.__is_digit(x) for row in rows_or for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.matrix = rows_or
    @staticmethod
    def __is_digit(x):
        return type(x) in (int, float)

    def __index_validating(self, coords):
        i, j = coords
        if not isinstance(i, int) or not 0 <= i <= self.rows:
            raise IndexError('недопустимые значения индексов')
        if not isinstance(j, int) or not 0 <= j <= self.cols:
            raise IndexError('недопустимые значения индексов')

    def __value_valdating(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')

    def __len_validating(self, othr):
        if not self.rows == othr.rows or not self.cols == othr.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __getitem__(self, coords):
        self.__index_validating(coords)
        i, j = coords
        return self.matrix[i][j]

    def __setitem__(self, coords, value):
        self.__index_validating(coords)
        self.__value_valdating(value)
        i, j = coords
        self.matrix[i][j] = value

    def __add__(self, othr):
        if isinstance(othr, Matrix):
            self.__len_validating(othr)
            return Matrix([[self[i, j] + othr[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            return Matrix([[self[i, j] + othr for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, othr):
        if isinstance(othr, Matrix):
            self.__len_validating(othr)
            return Matrix([[self[i, j] - othr[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            return Matrix([[self[i, j] - othr for j in range(self.cols)] for i in range(self.rows)])

mt = [[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]]
m1 = Matrix(mt)
# print(m1.matrix)
m2 = Matrix(4, 5, 10)
m3 = m1 - m2
print(m3)
