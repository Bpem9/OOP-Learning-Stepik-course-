import re
class FileAcceptor:
    def __init__(self, *args):
        self.extensions = [*args]

    def __call__(self, filename, *args):
        return True if re.search(r'(?<=\.)\w+$', filename).group(0) in self.extensions else False

    def __add__(self, other):
        for extension in other.extensions:
            if extension not in self.extensions:
                self.extensions.append(extension)
        return FileAcceptor(*self.extensions)


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png",
             "my.html", "data.shtml"]
acceptor1 = FileAcceptor('jpeg', 'jpg')
acceptor2 = FileAcceptor('png', 'pdf', 'jpg')
acceptor3 = acceptor1 + acceptor2
print(acceptor3.extensions)
filenames = list(filter(acceptor2, filenames))
print(filenames)

