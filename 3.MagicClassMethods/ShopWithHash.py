import re
lst_in = ['Системный блок: 1500 75890.56', 'Монитор Samsung: 2000 34000', 'Клавиатура: 200.44 545', 'Монитор Samsung: 2000 34000']

import sys
import re

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name.capitalize()
        self.weight = weight
        self.price = price
        self.count = 1
    def __hash__(self):
        return hash((self.name, self.weight, self.price))
    def __eq__(self, other):
        return hash(self) == hash(other)


shop_items = {}
for item in lst_in:
    # good = re.search(r'([a-zA-Zа-яА-Я-]*\s?[a-zA-Zа-яА-Я-]+)(?=:)', item).group(0).strip()
    good = item[:item.index(':')]
    # weight = re.search(r'(?<=:\s)\d+\.?\d+', item).group(0).strip()
    weight = item.split()[-2]
    # price = re.search(r'(?<=\d\s)\d+\.?\d+', item).group(0).strip()
    price = item.split()[-1]
    print(good, weight, price)
    a = ShopItem(good, weight, price)
    if a in shop_items.keys():
        a.count += 1
    shop_items[a] = [a, a.count]


it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"
print(v)
print(v[0][1], v[1][1], v[2][1], len(v), sep='\n')
print('='*10)

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"
print(v[0][0].name.strip())
print(v[0][1], v[1][1], v[2][1], len(v), sep='\n')