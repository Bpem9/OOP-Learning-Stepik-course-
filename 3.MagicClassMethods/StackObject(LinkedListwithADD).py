class StackObj:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push_back(self, obj):
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if self.top is None:
            self.top = obj

    def pop_back(self):
        h = self.top
        if h is None:
            return
        while h.next and h.next != self.tail:
            h = h.next
        if self.top is self.tail:
            self.top = self.tail = None
        else:
            h.next = None
            self.tail = h



    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in range(len(other)):
            self.push_back(StackObj(other[i]))
        return self

    def __imul__(self, other):
        for i in range(len(other)):
            self.push_back(StackObj(other[i]))
        return self



st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    print(f'StackObj - {h._StackObj__data}')
    print(f'd[i] - {d[i]}')
    # assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    print(f'Next - {h._StackObj__next}')
    h = h._StackObj__next
    i += 1