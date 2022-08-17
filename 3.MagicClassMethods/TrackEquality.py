class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed
    @property
    def x(self):
        return self.to_x
    @x.setter
    def x(self, to_x):
        self.to_x = to_x
    @property
    def y(self):
        return self.to_y
    @y.setter
    def y(self, to_y):
        self.to_y = to_y


class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.tracklist = []
        self.length = 0

    def add_track(self, *args):
        for arg in args:
            self.tracklist.append(arg)

    def get_tracks(self):
        return tuple(self.tracklist)

    def __len__(self):
        len1 = ((self.start_x - self.tracklist[0].x) ** 2 + (self.start_y - self.tracklist[0].y) ** 2) ** 0.5
        return int(len1 + sum(self.__get_length(i) for i in range(1, len(self.tracklist))))

    def __get_length(self, i):
        return ((self.tracklist[i-1].x - self.tracklist[i].x) ** 2 + (self.tracklist[i-1].y - self.tracklist[i].y) ** 2) ** 0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)


track1 = Track(0, 0)
tl1_1 = TrackLine(2, 4, 100)
tl1_2 = TrackLine(5, -4, 100)
track1.add_track(tl1_1, tl1_2)
track2 = Track(0, 1)
tl2_1 = TrackLine(3, 2, 90)
tl2_2 = TrackLine(10, 8, 90)
track2.add_track(tl2_1, tl2_2)
res_eq = track1 < track2
print(res_eq)
print(len(track1), len(track2), sep='\n')
