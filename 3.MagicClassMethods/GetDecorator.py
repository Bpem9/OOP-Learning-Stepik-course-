class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, request, *args, **kwargs):
        return self.get(self, request, *args, **kwargs)

    def get(self, func, request, *args, **kwargs):
        try:
            if request['method'] == 'GET':
                return f'GET: {self.__fn(request)}'
            else:
                return None
        except KeyError:
            return f'GET: {self.__fn(request)}'

@HandlerGET
def contact(request):
    return 'Привет!'

res = contact({"method": "GET", "url": "contact.html"})
print(res)