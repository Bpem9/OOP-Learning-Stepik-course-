class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.checking(width):
            if self.__width != width:
                self.__width = width
                self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.checking(height):
            if self.__height != height:
                self.__height = height
                self.show()

    @staticmethod
    def checking(x):
        if isinstance(x, int) and 0 <= x <= 10000:
            return True
        return False

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

