class Morph:
    def __init__(self, *args):
        self.forms = list(set(map(lambda x: x.lower().strip('.,?!_:-;'), args)))
    def add_word(self, word):
        w = word.lower()
        if not w in self.forms:
            self.forms.append(w)
    def get_words(self):
        return tuple(self.forms)
    def __eq__(self, word):
        if type(word) != str:
            raise ValueError('Операнд должен быть строкой')
        return word.lower() in self.forms

dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

text = 'Мы будем устанавливать связь завтра днем.'   # эту строчку не менять

include = 0
for word in text.split():
    if word.lower().strip('.,?!_:-;') in dict_words:
        include += 1
print(include)