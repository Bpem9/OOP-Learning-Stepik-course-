pole = tuple(tuple(i for i in range(3)) for _ in range(3))
print(pole)
print('='*10)
polupole = pole[1][1:2]
print(polupole)
print('='*10)
for item in pole:
    print(*item)
print('='*10)
for item in polupole:
    print(item)