class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class Bag:
    def __init__(self, max_weight):
        self._bag = []
        self._max_weight = max_weight
    def add_thing(self, thing):
        try:
            self._current_weight = self._weight_counting(self._bag)
            self._total_weight = thing.weight + self._current_weight
            if self._total_weight <= self._max_weight:
                self._bag.append(thing)
                print(f'Добавлено: {thing.name}\n{self._total_weight} / {self._max_weight}')
            else:
                raise ValueError('превышен суммарный вес предметов')
        except Exception as e:
            print(f'Не могу добавить вещь, потому что: {e}')
    def _weight_counting(self, bag):
        return sum(thing.weight for thing in bag)
    def __getitem__(self, index):
        self.__val(index)
        return self._bag[index]
    def __setitem__(self, index, value):
        self.__val(index)
        self.__weight_val(index, value)
        self._bag[index] = value
    def __delitem__(self, index):
        self.__val(index)
        self._bag.pop(index)
    def __val(self, index):
        if not isinstance(index, int) or not -len(self._bag) <= index <= len(self._bag):
            raise IndexError('неверный индекс')

    def __weight_val(self, index, thing):
        new_bag = self._bag.copy()
        new_bag.pop(index)
        self._current_weight = self._weight_counting(new_bag)
        self._total_weight = self._current_weight + thing.weight
        if not self._total_weight <= self._max_weight:
            raise ValueError('превышен суммарный вес предметов')

# bag = Bag(1000)
# bag.add_thing(Thing('книга', 200))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name) # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name) # платок
# del bag[0]
# print(bag[0].name) # платок
# bag.add_thing(Thing('ножницы', 300))
# t = bag[4] # генерируется исключение IndexError

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"