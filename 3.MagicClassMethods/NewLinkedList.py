class StackObj:
    def __init__(self, data):
        self.data = data
        self.__next = None
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, obj):
        self.__next = obj

class Stack:
    def __init__(self):
        self.counter = 0
        self.top = None
    def push(self, new):
        if self.top is None:
            self.top = new
        else:
            i = 0
            obj = self.top
            while obj.next:
                obj = obj.next
            obj.next = new
        self.counter += 1

    def pop(self):
        i = 0
        obj = self.top
        last = self.top
        while obj.next.next:
            obj = obj.next
            last = obj.next
            i += 1
        self.counter -= 1
        obj.next = None
        return last
    def __getitem__(self, index):
        self.__val(index)
        i = 0
        obj = self.top
        while i < index:
            obj = obj.next
            i += 1
        return obj
    def __setitem__(self, index, new_obj):
        self.__val(index)
        i = 0
        obj = self.top
        while i < index:
            obj = obj.next
            i += 1
        obj.data = new_obj.data
    def __val(self, index):
        if not isinstance(index, int) or not -self.counter < index < self.counter:
            raise IndexError('неверный индекс')


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
last = st.pop()
print(last)
# res = st[3] # исключение IndexError