class GenericView:
    def __init__(self, methods=('GET', 'POST')):
        self.methods = methods

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __methodval(self, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
    def __getval(self, request):
        if not isinstance(request, dict):
            raise TypeError('request не является словарем')
        if not 'url' in request.keys():
            raise TypeError('request не содержит обязательного ключа url')
    def render_request(self, request, method):
        self.__methodval(method)
        return getattr(self, method.lower())(request)
    def get(self, request):
        self.__getval(request)
        return f'url: {request["url"]}'


dt = DetailView()
gv = GenericView()
print(dt.render_request({'url': 'https://www.leningrad.ru'}, 'GET'))