class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = self.__prev = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj

    def __get_object_by_index(self, indx):
        obj = self.head
        n = 0
        while obj and n < indx:
            obj = obj.next
            n += 1
        return obj

    def remove_obj(self, indx):
        obj = self.__get_object_by_index(indx)
        if obj is None:
            return
        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p
        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        id = 0
        obj = self.head
        while obj:
            id += 1
            obj = obj.next
        return id

    def __call__(self, indx, *args, **kwargs):
        obj = self.__get_object_by_index(indx)
        return obj.data if obj else None


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
print(len(ln))
# assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"