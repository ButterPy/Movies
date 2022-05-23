from django.shortcuts import render
from .models import Movie


def show_all_movie(request):
    movies = Movie.objects.all()
    for movie in movies:
        movie.save()
    return render(request, 'movie.html', {
        'movies': movies
    })


def show_one_movie(request, id_movie: int):
    movie = Movie.objects.get(id=id_movie)

    return render(request, 'movie.html', {
        'movie': movie
    })
