class Validator:
    def __init__(self, amount=None):
        self.__amount = amount
    def am_valid(self):
        print('am_valid worked')
        if not isinstance(self.amount, (int, float)):
            raise TypeError('Значение экземпляра должно быть целым или вещественным числом')
    def cl_valid(self):
        print('cl_valid worked')
        if not isinstance(self.amount, (int, float, Currency)):
            raise ArithmeticError('Операнд должен быть вещественным или целым, или экземпляром Currency')
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

class Currency:
    def __init__(self, amount, val = Validator()):
        self.__amount = amount
        self.val = val
        self.val.amount = amount
        self.val.am_valid()

    def __mul__(self, ex_cur):
        self.val.cl_valid()
        if isinstance(ex_cur, Currency):
            ex_cur = ex_cur.amount
        return Currency(self.amount * ex_cur)

    def __imul__(self, other):
        self.val.cl_valid()
        print('__imul__')
        if isinstance(other, Currency):
            other = other.amount
        self.amount *= other
        return self


    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

if __name__ == '__main__':
    usd = Currency(125)
    rub = usd * Currency(65)
    rub *= Currency(1.02)
    print(rub.amount)