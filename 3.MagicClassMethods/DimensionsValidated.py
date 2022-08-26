s_inp = '1 2 3; 4 5 6.5; 1 2 3; 2.5 6 44'  # эту строку (переменную s_inp) в программе не менять


class Dimensions:
    def __init__(self, a, b, c):
        self.a = self.__val(a)
        self.b = self.__val(b)
        self.c = self.__val(c)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __val(self, num):
        num = float(num)
        if not num > 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        return num
    def __eq__(self, other):
        return hash(self) == hash(other)
    def __lt__(self, other):
        return hash(self) < hash(other)


lst_dims = []
for dim in s_inp.split(';'):
    a, b, c = dim.split()
    lst_dims.append(Dimensions(a, b, c))

print(sorted(lst_dims))
lst_dims.sort()


