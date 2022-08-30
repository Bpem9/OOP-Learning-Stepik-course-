class SLL:
    def __init__(self, *args):
        self.coords = list(args)
    def __getitem__(self, index):
        if isinstance(index, slice):
            return tuple(self.coords[index])
        return self.coords[index]
    def __setitem__(self, index, value):
        self.coords[index] = value

s = SLL(1, 2, 3, 4)
# s[::2] = [14, 16, 15]
print(s[2])