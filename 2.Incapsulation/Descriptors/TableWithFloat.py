class FloatValue:
    def validate(self, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell(0.0) for i in range(self.M)] for j in range(self.N)]


table = TableSheet(5, 3)

number = 1
for cell in table.cells:
    for obj in cell:
        obj.value = float(number)
        number += 1

for cell in table.cells:
    megavalues = [[obj.value for obj in cell] for cell in table.cells]

print(megavalues)
