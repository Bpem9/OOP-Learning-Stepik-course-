import math

class LineTo:
    def __init__(self, x=0, y=0):
        self.x0 = self.y0 = 0
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.pathlist = []
        for line in args:
            self.add_line(line)
        self.sum = 0
    def get_path(self):
        return self.pathlist
    def get_length(self):
        for obj in self.pathlist:
            obj.length = math.sqrt((obj.x-obj.x0)**2 + (obj.y-obj.y0)**2)
            self.sum += obj.length
        return self.sum
    def add_line(self, line):
        self.pathlist.append(line)
        if len(self.pathlist) > 1:
            line.x0 = self.pathlist[-2].x
            line.y0 = self.pathlist[-2].y

line1 = LineTo(10, 20)
line2 = LineTo(10, 30)
patha = PathLines(line1, line2)
patha.add_line(LineTo(20, -10))
print(patha.get_length())
