class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        self.validate(key, value)
        object.__setattr__(self, key, value)

    def validate(self, key, value):
        if key == 'title' or key == 'author':
            if not isinstance(value, str):
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'pages' or key == 'year':
            if not isinstance(value, int):
                raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
print(f'{book.title} : {book.pages}')
book2 = Book()