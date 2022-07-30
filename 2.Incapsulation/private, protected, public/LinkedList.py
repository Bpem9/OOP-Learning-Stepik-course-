class LinkedList:
    def __init__(self):
        self.llst = []
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        self.llst.append(obj)
        self.head = self.llst[0]
        self.tail = self.llst[len(self.llst) - 1]

    def remove_obj(self):
        self.llst.remove(obj)
        self.tail = self.llst[len(self.llst) - 1]

    def get_data(self):
        return [obj.__data for obj in self.llst]




lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']