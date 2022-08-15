class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        else:
            return self.money + other

    def __radd__(self, other):
        return self + other


class Budget:
    def __init__(self):
        self.explist = []

    def add_item(self, it):
        self.explist.append(it)

    def remove_item(self, indx):
        self.explist.pop(indx)

    def get_items(self):
        return self.explist


it1 = Item('Автомобиль', 34000)
bd = Budget()
bd.add_item(it1)
bd.add_item(Item('Продукты', 2500))
bd.add_item(Item('Курс по Python', 0.5))
print(bd.get_items())
s = 0
for item in bd.get_items():
    s = s + item
print(s)