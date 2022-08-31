class Thing:
    __id = 0
    def __init__(self, name, price):
        self.id = self.get_id()
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None

    @classmethod
    def get_id(cls):
        Thing.__id += 1
        return Thing.__id

    def get_data(self):
        return tuple(getattr(self, name) for name in self.__dict__.keys())


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm

t = Table('Мглэук', 34000, 15, (750, 600, 1200))
print(t.get_data())
b = ElBook('Клыргу', 5000, 256, (500, 500, 770))
print(b.get_data())