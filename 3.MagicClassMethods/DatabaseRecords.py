import sys
from random import randint


class Record:
    __counter = 0

    def __init__(self, fio, descr, old):
        self.pk = self.__count()
        self.fio = fio
        self.descr = descr
        self.old = old
    @classmethod
    def __count(cls):
        cls.__counter += 1
        return cls.__counter

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)
    def __repr__(self):
        return self.descr


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        if record in self.dict_db.keys():
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = []
            self.dict_db[record].append(record)

    def read(self, pk):
        for value in self.dict_db.values():
            for item in value:
                if item.pk == pk:
                    return item

db = DataBase('path')
lst_in = ['Балакирев С.М.; программист; 33', 'Кузнецов Н.И.; дваведчик-нелегал; 35', 'Суворов А.В.; полководец; 42', 'Иванов И.И.; фигурант всех подобных списков; 26', 'Балакирев С.М.; преподаватель; 33']
for item in lst_in:
    fio, descr, old = item.split('; ')
    old = int(old)
    db.write(Record(fio, descr, old))

print(db.dict_db)
print(db.read(2))