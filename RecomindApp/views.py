from django.shortcuts import render
from . import models

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def movies(request):
    peliculas = models.Items.objects.all()
    return render(
        request,
        "movies.html",
        {
            "peliculas": peliculas,
        }
    )
    
def movie(request, id):
    pelicula = models.Items.objects.get(ID=id)
    return render(
        request, 
        "movie.html",
        {
            "seleccion": pelicula
        }
    )

def games(request):
    juegos = models.Items.objects.all()
    return render(
        request,
        "games.html",
        {
            "juegos": juegos,
        }
    )
    
def game(request, id):
    juego = models.Items.objects.get(ID=id)
    return render(
        request, 
        "game.html",
        {
            "seleccion": juego
        }
    )

def animes(request):
    animes = models.Items.objects.all()
    return render(
        request,
        "animes.html",
        {
            "animes": animes,
        }
    )
    
def anime(request, id):
    anime = models.Items.objects.get(ID=id)
    return render(
        request, 
        "anime.html",
        {
            "seleccion": anime
        }
    )