class Track:
    def __init__(self, start_x, start_y):
        self.track = {}
        self.start_x = start_x
        self.start_y = start_y

    def add_point(self, x, y, speed):
        self.track[(x, y)] = speed

    def __getitem__(self, index):
        self.__validating_index(index)
        coords = tuple(self.track.keys())[index]
        speed = self.track[coords]
        return coords, speed

    def __setitem__(self, index, speed):
        self.__validating_index(index)
        coords = tuple(self.track.keys())[index]
        self.track[coords] = speed

    def __validating_index(self, index):
        if not isinstance(index, int) or not index in range(len(list(self.track.keys()))):
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

# res = tr[3]