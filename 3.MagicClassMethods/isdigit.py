class DigitRetrieve:
    def __init__(self):
        pass
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except ValueError:
            return None

st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]