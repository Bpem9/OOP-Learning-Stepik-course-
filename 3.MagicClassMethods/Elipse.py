class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return True if self.__dict__ else False

    def get_coords(self):
        if not bool(self):
            raise AttributeError('нет координат для извлечения')
        return (self.x1, self.y1, self.x2, self.y2)


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
ll = [el for el in lst_geom if el]
print(ll)
