class TriangleListIterator:
    def __init__(self, lst):
        self._lst = lst

    def __iter__(self):
        for i in range(len(self._lst)):
            for j in range(i+1):
                yield self._lst[i][j]



lls = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
tr = TriangleListIterator(lls)
for i in tr:
    print(i)