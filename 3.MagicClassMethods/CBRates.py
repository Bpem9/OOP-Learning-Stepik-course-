class CentralBank:
    def __new__(cls, *args, **kwargs):
        return None

    def __init__(self):
        self.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    @classmethod
    def register(cls, money):
        print('--registrated--')
        money.cb = CentralBank


class MoneyR:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume
        self.rub_volume = round(self.__volume, 2)

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = round(volume, 2)

    def checking(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        if not other.cb:
            raise ValueError("Неизвестен курс валют.")

    def __eq__(self, other):
        self.checking(other)
        return self.volume == other.rub_volume

    def __lt__(self, other):
        self.checking(other)
        return self.volume < other.rub_volume

    def __le__(self, other):
        self.checking(other)
        return self.volume <= other.rub_volume


class MoneyD:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    def checking(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        if not other.cb:
            raise ValueError("Неизвестен курс валют.")

    def converting(self):
        print('--dollar converted--')
        self.rub_volume = round(self.volume * self.cb.rates['rub'], 2)


    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb
        self.converting()

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __eq__(self, other):
        self.checking(other)
        return self.rub_volume == other.rub_volume

    def __lt__(self, other):
        self.checking(other)
        return self.rub_volume < other.rub_volume

    def __le__(self, other):
        self.checking(other)
        return self.rub_volume <= other.rub_volume


class MoneyE:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    def checking(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        if not other.cb:
            raise ValueError("Неизвестен курс валют.")

    def converting(self):
        print('--euro converted--')
        self.rub_volume = round(self.__volume * self.cb.rates['euro'] * self.cb.rates['rub'], 2)

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb
        self.converting()

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __eq__(self, other):
        self.checking(other)
        return self.rub_volume == other.rub_volume

    def __lt__(self, other):
        self.checking(other)
        return self.rub_volume < other.rub_volume

    def __le__(self, other):
        self.checking(other)
        return self.rub_volume <= other.rub_volume

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)
e = MoneyE(900)
d2 = MoneyD(500.0005)

CentralBank.register(r)
CentralBank.register(d)
CentralBank.register(d2)

print(d2.rub_volume)
if d == d2:
    print("неплохо")
else:
    print("нужно поднажать")
