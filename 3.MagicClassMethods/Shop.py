class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id = 0
    types = {'name': [str], 'id': [int], 'weight': [int, float], 'price': [int, float]}

    def __init__(self, name, weight, price):
        self.id = Product.id
        self.name = name
        self.weight = weight
        self.price = price
        self.new_id()

    @classmethod
    def new_id(cls):
        cls.id += 1

    def __setattr__(self, key, value):
        self.validating(key, value)
        object.__setattr__(self, key, value)

    def __delattr__(self, key):
        if key == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")

    def validating(self, key, value):
        if type(value) not in self.types[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ('weight', 'price') and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", -1, 512))

for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")