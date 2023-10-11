from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/search/<id_passed>', views.movie_search, name='movie_search'),
]
