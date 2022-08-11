class NewList:
    def __init__(self, list=[]):
        self.list = list

    def get_list(self):
        return self.list

    def __sub__(self, other):
        newlist = self.list.copy()
        if isinstance(other, NewList):
            other = other.list
        for el in other:
            if el in newlist:
                if type(el) == bool:
                    newlist.pop(list(map(str, newlist)).index(str(el)))
                else:
                    newlist.remove(el)
        return NewList(newlist)

    def __rsub__(self, other):
        return NewList(other) - self


lst1 = NewList([0, 1, -3.4, "abc", True])
lst3 = NewList([1, 0, True])
# lst2 = NewList([1, 0, True])
# res1 = lst1 - lst2
a = lst1 - [0, True]
# res2 = [0, 1, True, 444] - lst1
res3 = [1, 2, 3, 4.5] - lst3
# print(lst1.get_list())
# print(res1.get_list())
# print(res2.get_list())
print(res3.get_list())


