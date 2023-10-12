from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'testapp/home.html'

    def render_to_response(self, context, **response_kwargs):
        print(self.request.COOKIES.get('my_cookie'))
        if self.request.COOKIES.get('my_cookie') == 'my_cookie_value':
            response = HttpResponse('WITH COOKIE!')
            return response
        return super().render_to_response(context, **response_kwargs)


class AboutPageView(TemplateView):
    template_name = 'testapp/about.html'


def home_view(request):
    print(request)
    print(request.method == "GET")
    print(request.method)
    print(request.COOKIES)
    response = render(request, 'testapp/home2.html', {"message": "Welcome to the homepage!"})
    print('Response:', response)
    return response
    # response_2 = HttpResponse("Welcome to the homepage!")
    # response_2.write("<h1> Hello World! </h1>")
    # return response_2


def about_view(request):
    return render(request, 'testapp/about2.html', {"message": "About us page!"})


def server_time_view(request):
    return render(request, 'testapp/server_time.html')



