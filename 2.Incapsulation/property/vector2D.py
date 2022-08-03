class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        if self.checking(x):
            self.__x = x
        if self.checking(y):
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.checking(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.checking(y):
            self.__y = y

    @classmethod
    def checking(cls, coordinate):
        if isinstance(coordinate, (int, float)) and cls.MIN_COORD <= coordinate <= cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(vector):
        return (vector.x * vector.x + vector.y * vector.y)

vector = RadiusVector2D(-100, 1024.1)
vector.y = -10.001
vector.x = '1024'
print(vector.y)
print(vector.x)