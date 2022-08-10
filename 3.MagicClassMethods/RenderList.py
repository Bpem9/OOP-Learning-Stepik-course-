class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list
    def __call__(self, *args, **kwargs):
        string = f'<{self.type_list}>\n'
        for arg in list(*args):
            string += f'<li>{arg}</li>\n'
        return string + f'</{self.type_list}>'

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html.replace('\n', '').replace(' ', '').strip())
