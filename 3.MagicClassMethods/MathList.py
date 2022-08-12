class ListMath:
    def __init__(self, list1=[]):
        self.lst_math = list(filter(lambda item: isinstance(item, (int, float)) and type(item) != bool, list1))

    def __add__(self, other):
        self.new_lst = list(map(lambda item: item + other, self.lst_math))
        return ListMath(self.new_lst)
    def __radd__(self, other):
        return self + other
    def __iadd__(self, other):
        self.lst_math = list(map(lambda item: item + other, self.lst_math))
        return self

    def __sub__(self, other):
        self.new_lst = list(map(lambda item: item - other, self.lst_math))
        return ListMath(self.new_lst)
    def __rsub__(self, other):
        self.new_lst = list(map(lambda item: other - item, self.lst_math))
        return ListMath(self.new_lst)
    def __isub__(self, other):
        self.lst_math = list(map(lambda item: item - other, self.lst_math))
        return self

    def __mul__(self, other):
        self.new_lst = list(map(lambda item: item * other, self.lst_math))
        return ListMath(self.new_lst)
    def __rmul__(self, other):
        return self * other
    def __imul__(self, other):
        self.lst_math = list(map(lambda item: item * other, self.lst_math))
        return self

    def __truediv__(self, other):
        self.new_lst = list(map(lambda item: item / other, self.lst_math))
        return ListMath(self.new_lst)
    def __rtruediv__(self, other):
        self.new_lst = list(map(lambda item: other / item, self.lst_math))
        return ListMath(self.new_lst)
    def __itruediv__(self, other):
        self.lst_math = list(map(lambda item: item / other, self.lst_math))
        return self


lst2 = ListMath([1, False, 2, -5, "abc", 7])
lst = ListMath()
# lst = lst / 2
# lst /= 13.0
# print(lst.lst_math)
# print(res5.lst_math)
# print(res6.lst_math)
print(lst.lst_math)