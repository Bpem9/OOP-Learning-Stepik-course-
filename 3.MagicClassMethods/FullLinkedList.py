class Stack:
    def __init__(self):
        self.top = self.tail = None

    def push_back(self, obj):
        if self.top is None:
            self.top = self.tail = obj
        else:
            self.tail.next = obj
            self.tail = obj


    def push_front(self, obj):
        obj.next = self.top
        self.top = obj

    def listlength(self):
        i = 0
        obj = self.top
        while obj:
            obj = obj.next
            i += 1
        return i

    def __itembyindex(self, index):
        self.__indexval(index)
        i = 0
        obj = self.top
        while i != index:
            obj = obj.next
            i += 1
        return obj

    def __indexval(self, index):
        if not isinstance(index, int) or not 0 <= index < len(self):
            print(len(self))
            raise IndexError('неверный индекс')

    def __len__(self):
        return self.listlength()

    def __getitem__(self, index):
        item = self.__itembyindex(index)
        return item.data

    def __setitem__(self, index, value):
        item = self.__itembyindex(index)
        item.data = value

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next



class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

st = Stack()
st.push_back(StackObj('Автомобиль'))
st.push_back(StackObj('Крутите барабан!'))
st.push_back(StackObj('Откройте букву'))
st.push_back(StackObj('Приз! В студию!'))
st.push_front(StackObj('Подарки! В студию!'))

print(st[-1])
print('='*10)

for i in st:
    print(i.data)
print('='*10)
