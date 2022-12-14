class LinkedList:
    def __init__(self):
        self.llst = []
        self.head = None
        self.tail = None
    def add_obj(self, obj):
        self.llst.append(obj)
        self.head = self.llst[0]
        if len(self.llst) >= 2:
            obj.set_prev(self.llst[-2])
            self.llst[-2].set_next(obj)
        self.tail = obj
    def remove_obj(self):
        del self.llst[-1]
    def get_data(self):
        return [obj.get_data() for obj in self.llst]

class ObjList():
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None
    def set_next(self, obj):
        self.__next = obj
    def set_prev(self, obj):
        self.__prev = obj
    def get_next(self):
        return self.__next
    def get_prev(self):
        return self.__prev
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']

print(lst)
print(lst.llst[1].get_next().get_data())
print(lst.get_data())