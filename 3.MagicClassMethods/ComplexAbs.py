class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, number):
        self.validate(number)
        self.__real = number

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, number):
        self.validate(number)
        self.__img = number

    def validate(self, number):
        if not isinstance(number, (int, float)):
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        self.module = (self.real ** 2 + self.img ** 2) ** 0.5
        return self.module


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)