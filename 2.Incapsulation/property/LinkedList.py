class Stack:
    def __init__(self):
        self.list = []
        self.top = None

    def push(self, obj):
        self.list.append(obj)
        self.top = self.list[0]

    def pop(self):
        self.list.pop()
        if len(self.list) == 0:
            self.top = None
    def get_data(self):
        return [obj.data for obj in self.list]


class StackObj:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
st.get_data()    # ['obj1', 'obj2']
