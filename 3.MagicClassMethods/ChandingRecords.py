class Record:
    def __init__(self, **kwargs):
        for item, value in kwargs.items():
            object.__setattr__(self, item, value)
    def __getitem__(self, index):
        self.__index_validating(index)
        item = list(self.__dict__.keys())[index]
        return self.__dict__[item]
    def __setitem__(self, index, value):
        self.__index_validating(index)
        item = list(self.__dict__.keys())[index]
        self.__dict__[item] = value
    def __index_validating(self, index):
        if index > (len(list(self.__dict__.keys()))-1) or not isinstance(index, int):
            raise IndexError('неверный индекс поля')



c = Record(key1='value1', name='value2', key3='value3')
c[1] = 'Balakirev'
print(c.name)
print(c.__dict__)
print(c[1])
