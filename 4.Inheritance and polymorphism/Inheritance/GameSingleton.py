class Singleton:
    __instance = None
    __instance_base = None
    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__instance_base is None:
                cls.__instance_base = object.__new__(cls)
            return cls.__instance_base
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    @classmethod
    def __del__(cls):
        cls.__instance = None

class Game(Singleton):
    def __init__(self, name):
        if not 'name' in self.__dict__:
            self.name = name

g = Game('Сапер')
print(type(g))