class Vector:
    def __init__(self, *args):
        self.coords = list(args)
    def __len_validate(self, other):
        if not len(self.coords) == len(other.coords):
            raise TypeError('Длины списков должны быть равными')
    def __make_vector(self, *coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.__len_validate(other)
        return self.__make_vector(*[i + j for i, j in zip(self.coords, other.coords)])
    def __sub__(self, other):
        self.__len_validate(other)
        return self.__make_vector(*[i - j for i, j in zip(self.coords, other.coords)])

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



list1 = VectorInt(1, 2, 3)
list2 = Vector(3, 4, 5)
v1 = list1 - list2
print(v1.get_coords())
print(type(v1))