class ListInteger(list):
    def __init__(self, list):
        super().__init__(list)
    def __setitem__(self, index, value):
        self.__type_val(value)
        super().__setattr__(index, value)
    def __type_val(self, item):
        if isinstance(item, (list, tuple)):
            for x in item:
                if not isinstance(x, int):
                    raise TypeError('можно передавать только целочисленные значения')
        else:
            if not isinstance(item, int):
                raise TypeError('можно передавать только целочисленные значения')

    def append(self, value):
        self.__type_val(value)
        super().append(value)

l = ListInteger((5, 6, 7))
l.append(5)
print(l)