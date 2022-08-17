class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim
    def __repr__(self):
        return self.name
    def __gt__(self, other):
        return self.dim.volume > other.dim.volume
    def __ge__(self, other):
        return self.dim.volume >= other.dim.volume
    def __lt__(self, other):
        return self.dim.volume < other.dim.volume
    def __le__(self, other):
        return self.dim.volume <= other.dim.volume

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __get_volume(self):
        self.__volume = self.__a * self.__b * self.__c
        return self.__volume

    def __repr__(self):
        return str(self.volume)

    @classmethod
    def __validating_limits(cls, x):
        if cls.MIN_DIMENSION <= x <= cls.MAX_DIMENSION:
            return True
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, x):
        if self.__validating_limits(x):
            self.__a = x
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, x):
        if self.__validating_limits(x):
            self.__b = x
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, x):
        if self.__validating_limits(x):
            self.__c = x
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value


    def __gt__(self, other):
        return self.__get_volume() > other.__get_volume()
    def __ge__(self, other):
        return self.__get_volume() >= other.__get_volume()
    def __lt__(self, other):
        return self.__get_volume() < other.__get_volume()
    def __le__(self, other):
        return self.__get_volume() <= other.__get_volume()

item1 = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
item2 = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
item3 = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
item4= ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = [item1, item2, item3, item4]
lst_shop_sorted = sorted(lst_shop, key = lambda item: item.dim)
d1 = Dimensions(40, 30, 120)
d2 = Dimensions(10, 20, 50)
print(lst_shop_sorted)
# print(d1 > d2)
# print(d1.volume, d2.volume, sep='/')
# d2.a = 600
# d2.b = 200
# d2.c = 30
# print(d1.volume, d2.volume, sep='/')

# print(d1 > d2)
# print(item2.dim)
