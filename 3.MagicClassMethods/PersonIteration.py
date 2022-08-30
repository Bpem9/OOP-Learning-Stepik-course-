class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._sum = list(self.__dict__)
        self._sum_len = len(self._sum)
    def __val(self, index):
        if not isinstance(index, int) or not -self._sum_len <= 0 <= self._sum_len:
            raise IndexError('неверный индекс')
    def __getitem__(self, index):
        self.__val(index)
        return getattr(self, self._sum[index])
    def __setitem__(self, index, value):
        self.__val(index)
        setattr(self, self._sum[index], value)
    def __iter__(self):
        self._index = -1
        return self
    def __next__(self):
        if self._index < self._sum_len - 1:
            self._index += 1
            return getattr(self, self._sum[self._index])
        raise StopIteration


p = Person('Билл Гейтс', 'Бизнессмен', 65, 100000, 46)
char = iter(p)
for p in char:
    print(p)

