from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('search/', views.search_movies, name='search_movies'),
]
