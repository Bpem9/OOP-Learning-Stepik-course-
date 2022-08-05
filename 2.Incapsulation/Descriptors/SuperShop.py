class Validate:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def price_validating(self, price):
        self.min_value = self.min_length
        self.max_value = self.max_length
        self.price = price
        return isinstance(self.price, (int, float)) and self.min_value <= self.price <= self.max_value

    def name_validating(self, name):
        self.name = name
        return isinstance(self.name, str) and self.min_length <= len(self.name) <= self.max_length


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.name_validating(value):
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, price):
        self.price = '_' + price

    def __get__(self, instance, owner):
        return getattr(instance, self.price)

    def __set__(self, instance, value):
        if self.validator.price_validating(value):
            setattr(instance, self.price, value)


class Product:
    name = StringValue(validator=Validate(2, 50))
    price = PriceValue(validator=Validate(0, 10000))

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")