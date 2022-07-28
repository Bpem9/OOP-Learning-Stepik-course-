class Clock:
    def __init__(self, time=0):
        self.__time = time
    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
    def get_time(self):
        return self.__time
    @classmethod
    def __check_time(cls, tm):
        return isinstance(tm, int) and 0 <= tm < 100000

clock = Clock()
clock.set_time(4530)
print(clock.get_time())

