from django.shortcuts import render
from . import models
from django.db.models import Q
from django.http import request

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def movies(request):
   

    peliculas = models.Items.objects.all()

    respuesta = []

    for pelicula in peliculas:
        
        cantidad = 0
        correcto = 0

        req = dict(request.GET)

        if "nombre" in req:
            cantidad += 1
            if req["nombre"][0].lower() in pelicula.Nombre.lower():
                correcto += 1
        
        if "categorias" in req:
            cantidad += 1
            if req["categorias"][0].lower() in str(pelicula.Categorias).lower():
                correcto += 1

        if "valoracion" in req:
            cantidad += 1
            if int(req["valoracion"][0]) == int(float(str(pelicula.Valoracion))):
                correcto += 1
        
        if "year" in req:
            cantidad += 1
            if int(req["year"][0]) == int(str(pelicula.Year)):
                correcto += 1

        if "director" in req:
            cantidad += 1
            if req["director"][0].lower() in str(pelicula.Director).lower():
                correcto += 1

        if cantidad == correcto:
            respuesta.append(pelicula)

    if len(request.GET) == 0:
        respuesta = peliculas

    return render(
        request,
        "movies.html",
        {
            "peliculas": respuesta
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
    
    respuesta = []

    for jeugo in juegos:
        
        cantidad = 0
        correcto = 0

        req = dict(request.GET)

        if "nombre" in req:
            cantidad += 1
            if req["nombre"][0].lower() in juego.Nombre.lower():
                correcto += 1
        
        if "categorias" in req:
            cantidad += 1
            if req["categorias"][0].lower() in str(juego.Categorias).lower():
                correcto += 1

        if "valoracion" in req:
            cantidad += 1
            if int(req["valoracion"][0]) == int(float(str(juego.Valoracion))):
                correcto += 1
        
        if "year" in req:
            cantidad += 1
            if int(req["year"][0]) == int(str(juego.Year)):
                correcto += 1

        if "director" in req:
            cantidad += 1
            if req["Desarrollador"][0].lower() in str(juego.Desarrollador).lower():
                correcto += 1

        if cantidad == correcto:
            respuesta.append(juego)

    if len(request.GET) == 0:
        respuesta = juegos

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
    
    

    respuesta = []

    for anime in animes:
        
        cantidad = 0
        correcto = 0

        req = dict(request.GET)

        if "nombre" in req:
            cantidad += 1
            if req["nombre"][0].lower() in anime.Nombre.lower():
                correcto += 1
        
        if "categorias" in req:
            cantidad += 1
            if req["categorias"][0].lower() in str(anime.Categorias).lower():
                correcto += 1

        if "valoracion" in req:
            cantidad += 1
            if int(req["valoracion"][0]) == int(float(str(anime.Valoracion))):
                correcto += 1
        
        if "year" in req:
            cantidad += 1
            if int(req["year"][0]) == int(str(anime.Year)):
                correcto += 1

        if "estudio" in req:
            cantidad += 1
            if req["estudio"][0].lower() in str(anime.Estudio).lower():
                correcto += 1

        if cantidad == correcto:
            respuesta.append(anime)

    if len(request.GET) == 0:
        respuesta = animes

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