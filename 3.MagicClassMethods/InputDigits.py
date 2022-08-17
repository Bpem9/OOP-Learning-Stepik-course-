class InputDigits:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        string = self.func()
        return [int(item) for item in list(string.split())]

@InputDigits
def input_dg():
    return input('Введи числа через пробел:')
res = input_dg()
print(res)
# print(type(input('Ввди чет')))