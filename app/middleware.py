from django.http import HttpResponse



class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response



    def process_view(self,request, view_func, view_args, view_kwargs):
        if request.method =='POST':

            print(request.POST)
            print(type(request.POST))
            print(request.data)
            print(type(request.data))
            if request.POST['name']=='shiv':
                return None
            else:
                return HttpResponse('return from middleware')
        else:
            return None

