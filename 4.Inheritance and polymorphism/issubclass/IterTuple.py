class Tuple(tuple):
    def __init__(self, obj):
        if isinstance(obj, list):
            self.list = obj
        else:
            self.list = list(obj)
        self.tuple = tuple(obj)

    def __add__(self, other):
        if isinstance(other, Tuple):
            return Tuple(self.list + other.list)
        else:
            return Tuple(self.list + list(other))

names = ['Alfa', 'Beta', 'Gamma']
names2 = ['Delta', 'Epsilon']
tnames = Tuple(names)
nnames = Tuple(names2)
adnames = tnames + 'Python'
# adnames = tnames + nnames
# adnames = tnames + ['Igor', 'Omega']
print(adnames)