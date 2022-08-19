class RenderDigit:
    def __init__(self):
        pass
    def __isdigit(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def __call__(self, number, *args,  ** kwargs):
        return int(number) if self.__isdigit(number) else None


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return [self.render(item) for item in func().split()]
        return wrapper

@InputValues(render=RenderDigit())
def input_dg():
    return input('Введи числа через пробел: ')

res = input_dg()
print(res)