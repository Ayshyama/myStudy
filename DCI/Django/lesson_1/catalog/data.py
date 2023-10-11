from catalog.models import Movie


# movies = Movie.objects.all()
# POSTS = movies.values()

movies = Movie.objects.all().values('title', 'year', 'genre', 'director', 'description')

format_data = "My List of Movies:<br>"
for movie in movies:
    format_data += f"Title: {movie['title']}, Year: {movie['year']}, Genre: {movie['genre']}<br>"

POSTS = format_data
