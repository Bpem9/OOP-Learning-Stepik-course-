from random import randint # функция для генерации целых случайных значений в диапазоне [a; b]

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw = ''
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length
    def __call__(self, *args, **kwargs):
        for i in range(randint(self.min_length, self.max_length)):
            self.psw += self.psw_chars[randint(0, len(self.psw_chars)-1)]
        return self.psw
letters = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(letters, 5, 20)
print(rnd())
