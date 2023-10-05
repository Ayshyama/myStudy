from django.shortcuts import render, get_object_or_404
from .models import Movie  # Make sure you have this import

def movie_list(request):
    # Retrieve all movies from the database
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_details(request, movie_id):
    # Retrieve a specific movie by its ID
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_details.html', {'movie': movie})

def search_movies(request):
    # Implement movie search functionality based on user input
    # You can access search parameters using request.GET.get('parameter_name')
    # Example: title_query = request.GET.get('title')
    # Implement your search logic here
    # Return the search results to a template for rendering
    return render(request, 'search_results.html', {'search_results': search_results})
