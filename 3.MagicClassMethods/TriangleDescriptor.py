class Top:
    def __validating(self, value):
        if not value > 0 or not isinstance(value, (int, float)):
            raise ValueError("длины сторон треугольника должны быть положительными числами")
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        self.__validating(value)
        setattr(instance, self.name, value)
class Triangle:
    a = Top()
    b = Top()
    c = Top()
    def __init__(self, a, b, c):
        self.__triangle_checking(a, b, c)
        self.a = a
        self.b = b
        self.c = c
    def __triangle_checking(self, a, b, c):
        if not a < b+c or not b < a+c or not c < a+b:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
    def __len__(self):
        return int(self.a + self.b + self.c)
    def __call__(self, *args, **kwargs):
        return (len(self)/2 * (len(self)/2-self.a) * (len(self)/2-self.b) * (len(self)/2-self.c)**0.5)

tr = Triangle(5, 4, 3)
print(tr())