


class RetriveMixin:
    def __init__(self):
        super().__init__()

    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')



class GeneralView:
    def __init__(self):
        super().__init__()
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')


    def render_request(self, request):
        if request.get('method', 0) not in self.allowed_methods:
            raise TypeError(f"Method {request.get('method')} hasnt access")


        method_request = self.__getattribute__(request.get('method').lower())
        return method_request(request)

class DetailView(RetriveMixin, GeneralView, UpdateMixin):
    allowed_methods = ('GET', 'PUT', )



view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html) # GET: https://stepik.org/course/116336/
print(DetailView.__mro__)








