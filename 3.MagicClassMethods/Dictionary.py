class Morph:
    def __init__(self, *args):
        self.forms = [args]
    def add_word(self, word):
        if not word in self.forms:
            self.forms.append(word)
    def get_words(self):
        return tuple(self.forms)
    def __eq__(self, other):
        return self in other
    # def __eq__(self, other):
    #     return other in self

text = input()   # эту строчку не менять
a = Morph('связь', 'связи')
# dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях')]
#               Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
# Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
# Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

text='Мы будем устанавливать связь завтра днем.'
print(a)