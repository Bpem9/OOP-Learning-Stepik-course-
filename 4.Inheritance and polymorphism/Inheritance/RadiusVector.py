class Vector:
    def __init__(self, *args):
        self.coords = list(args)
    def __add__(self, other):
        if len(self.coords) == len(other.coords):
            return Vector(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __sub__(self, other):
        if len(self.coords) == len(other.coords):
            return Vector(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])
    def get_coords(self):
        return tuple(self.coords)

class VectorInt(Vector):
    def __init__(self, *args):
        self.__type_validating(args)
        self.coords = list(args)
    def __type_validating(self, args):
        for i in list(args):
            if not isinstance(i, int):
                raise ValueError('координаты должны быть целыми числами')
    def __add__(self, other):
        new = [self.coords[i] + other.coords[i] for i in range(len(self.coords))]
        if all(list(map(lambda x: isinstance(x, int), new))):
            return VectorInt(*new)
        else:
            return Vector(*new)
    def __sub__(self, other):
        new = [self.coords[i] - other.coords[i] for i in range(len(self.coords))]
        if all(list(map(lambda x: isinstance(x, int), new))):
            return VectorInt(*new)
        else:
            return Vector(*new)


list1 = VectorInt(1, 2, 3)
list2 = Vector(3, 4, 5)
v1 = list1 - list2
print(v1.get_coords())
print(type(v1))