class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __validate(self, other):
        if isinstance(other, Vector) and len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        self.__validate(other)
        if isinstance(other, int):
            args = list(map(lambda x: x + other, self.coords))
            return Vector(*args)
        if isinstance(other, Vector):
            args = []
            for i in range(len(self.coords)):
                args.append(self.coords[i] + other.coords[i])
            return Vector(*args)

    def __sub__(self, other):
        self.__validate(other)
        if isinstance(other, int):
            args = list(map(lambda x: x - other, self.coords))
            return Vector(*args)
        if isinstance(other, Vector):
            args = []
            for i in range(len(self.coords)):
                args.append(self.coords[i] - other.coords[i])
            return Vector(*args)

    def __mul__(self, other):
        self.__validate(other)
        if isinstance(other, Vector):
            args = []
            for i in range(len(self.coords)):
                    args.append(self.coords[i] * other.coords[i])
            return Vector(*args)

    def __iadd__(self, other):
        self.__validate(other)
        if isinstance(other, int):
            args = list(map(lambda x: x + other, self.coords))
            return Vector(*args)
        if isinstance(other, Vector):
            for i in range(len(self.coords)):
                self.coords[i] += other.coords[i]
            return self
    def __isub__(self, other):
        self.__validate(other)
        if isinstance(other, int):
            args = list(map(lambda x: x - other, self.coords))
            return Vector(*args)
        if isinstance(other, Vector):
            for i in range(len(self.coords)):
                self.coords[i] -= other.coords[i]
            return self

        def __eq__(self, other):
            newlst = list(filter(lambda x: x not in other.coords, self.coords))
            return False if newlst else True

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True