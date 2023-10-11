from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'testapp/home.html'


class AboutPageView(TemplateView):
    template_name = 'testapp/about.html'


def home_view(request):
    return render(request, 'testapp/home2.html', {"message": "Welcome to the homepage!"})


def about_view(request):
    return render(request, 'testapp/about2.html', {"message": "About us page!"})



