class Model:
    def __init__(self, **kwargs):
        self.model = 'Model'
    def query(self, **kwargs):
        for item, value in kwargs.items():
            self.model += f' {item} = {value},'
    def __str__(self):
        return self.model.strip(',')

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
model2 = Model()
print(model2)