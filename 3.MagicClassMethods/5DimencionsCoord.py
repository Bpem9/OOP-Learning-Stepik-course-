class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            for arg in args:
                if isinstance(arg, int) and arg > 1:
                    self.coords = [0] * arg
        else:
            self.coords = [*args]
        self.length = 0

    def get_coords(self):
        return tuple(self.coords)

    def set_coords(self, *args):
        new = [*args]
        if len(new) >= len(self.coords):
            for i in range(len(self.coords)):
                self.coords[i] = new[i]
        if len(self.coords) > len(new):
            for i in range(len(new)):
                self.coords[i] = new[i]

    def __abs__(self):
        self.length = (sum([coord ** 2 for coord in self.coords])) ** 0.5
        return self.length

    def __len__(self):
        return len(self.coords)