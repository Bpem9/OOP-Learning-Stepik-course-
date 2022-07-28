from accessify import private
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    @private
    @classmethod
    def check_number(cls, x):
        return isinstance(x, (int, float))
    def set_coord(self, x, y):
        if self.check_number(x) and self.check_number(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError
    def get_coord(self):
        return self.__x, self.__y

pt = Point(1, 2)
print(pt.get_coord())
pt.set_coord(23.5, 42)
print(pt.get_coord())
pt.__x = 12
pt.__y = 32
print(pt.get_coord())
pt.check_number(5)