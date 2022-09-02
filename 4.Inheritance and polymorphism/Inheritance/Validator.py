class Validator:
    def __call__(self, data, *args, **kwargs):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return True

    def _is_valid(self, data):
        pass


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, int) and self.min_value <= data <= self.max_value

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, float) and self.min_value <= data <= self.max_value

it = IntegerValidator(-2, 2)
fl = FloatValidator(-2.4, 2.6)
print(it(1))
print(fl(2.0))
