import sys

class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    def __hash__(self):
        return hash((self.name, self.author))
    def __eq__(self, other):
        return hash(self) == hash(other)
    def __repr__(self):
        return self.name

# считывание списка из входного потока
lst_in = ['Python; Балакирев С.М.; 2020', 'Python ООП; Балакирев С.М.; 2021', 'Python ООП; Балакирев С.М.; 2022', 'Python; Балакирев С.М.; 2021']

lst_bs = []
for book in lst_in:
    name, author, year = book.split('; ')
    lst_bs.append(BookStudy(name, author, year))
unique_books = len(list(set(lst_bs)))