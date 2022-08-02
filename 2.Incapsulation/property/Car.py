class Car:
    def __init__(self, model='123'):
        self.__model = model
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        if self.checking(model):
            self.__model = model
    @staticmethod
    def checking(model):
        if not isinstance(model, str):
            return False
        if len(model) > 3:
            return False
        return True
    # model = property()

car = Car()
car.model = 3
print(car.model)