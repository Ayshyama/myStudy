from django.shortcuts import render
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})


def movie_search(request, id_passed):
    movies = Movie.objects.filter(id=id_passed)
    return render(request, 'movie_search.html', {'movies': movies})
