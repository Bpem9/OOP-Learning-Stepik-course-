import time


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            return False
        object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            return False
        object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            return False
        object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filters = {}

    def add_filter(self, slot_num, filter):
        if self.validate(slot_num, filter):
            if slot_num not in self.filters.keys():
                self.filters[slot_num] = filter

    def get_filters(self):
        return tuple(value for key, value in sorted(self.filters.items()))

    def validate(self, slot_num, filter):
        if isinstance(filter, Mechanical) and slot_num == 1:
            return True
        if isinstance(filter, Aragon) and slot_num == 2:
            return True
        if isinstance(filter, Calcium) and slot_num == 3:
            return True
        return False

    @classmethod
    def exp_valid(cls, filter):
        if 0 <= time.time() - filter.date <= cls.MAX_DATE_FILTER:
            return True

    def remove_filter(self, slot_num):
        del self.filters[slot_num]

    def water_on(self):
        if list(sorted(self.filters.keys())) != [1, 2, 3]:
            return False
        if self.exp_valid(list(self.filters.values())[0]) and self.exp_valid(
                list(self.filters.values())[1]) and self.exp_valid(list(self.filters.values())[2]):
            return True
        else:
            return False

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
print(my_water.get_filters())
my_water.remove_filter(1)
my_water.add_filter(1, Mechanical(time.time()))
print(my_water.get_filters())
