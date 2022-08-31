class IterColumn:
    def __init__(self, lst, column):
        self.data = [item[column] for item in lst]
    def __iter__(self):
        yield self.data

class IterColumn2:
    def __init__(self, lst, column):
        self._lst = lst
        self._column = column
    def __iter__(self):
        self.__row = -1
        return self
    def __next__(self):
        self.__row +=1
        if self.__row != len(self._lst):
            return self._lst[self.__row][self._column]
        else:
            raise StopIteration
class IterColumn3:
    def __init__(self, lst, column):
        self._lst = lst
        self._column = column
    def __iter__(self):
        for i in self._lst:
            yield i[self._column]

lst = [['x11', 'x12', 'x13'],
       ['x21', 'x22', 'x23'],
       ['x31', 'x32', 'x33']
      ]

it = IterColumn3(lst, 2)
for i in it:
    print(i)