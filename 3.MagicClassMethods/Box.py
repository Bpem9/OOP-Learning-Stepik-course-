class Box:
    def __init__(self):
        self.box = []
    def add_thing(self, obj):
        self.box.append(obj)
    def get_things(self):
        return self.box
    def __eq__(self, other):
        return sorted(self.box) == sorted(other.box)

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass
    def __lt__(self, other):
        return self.mass < other.mass



b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))
print(b1.box)
print(b2.box)
res = b1 == b2
print(res)