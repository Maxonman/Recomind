from django.shortcuts import render
from . import models
from django.db.models import Q
from django.http import request

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def items(type):
    def funcionGeneral(request):
        tipo = models.Tipos.objects.get(Nombre=type)
        items = models.Items.objects.filter(Tipo=tipo)
        req = dict({
            "nombre": [''],
            "categorias": [],
            "Valoracion": [0],
            "MinimumYear": [0],
            "MaximumYear": [10000],
        }, **request.GET)
        print(req)

        if "nombre" in req:
            items = items.filter(Nombre__contains=req["nombre"][0])
        if "categorias" in req:
            for categoria in req["categorias"]:
                items = items.filter(Categorias=models.Categorias.objects.filter(Nombre=categoria)[0])
        if "Valoracion" in req:
            dato = int(req["Valoracion"][0])
            items = items.filter(Valoracion__gte=dato)
        if "MinimumYear" in req:
            if req["MinimumYear"][0] == '':
                req["MinimumYear"][0] = 0
            dato = int(req["MinimumYear"][0])
            items = items.filter(Year__gte=dato)
        if "MaximumYear" in req:
            if req["MaximumYear"][0] == '':
                req["MaximumYear"][0] = 1000000
            dato = int(req["MaximumYear"][0])
            items = items.filter(Year__lte=dato)

        if "director" in req:
            if req["director"][0] != '':
                print(req["director"][0])
                directores = models.Directores.objects.filter(Nombre__contains=req["director"][0])
                if len(directores)>1:
                    items = items.filter(Director=directores[0])
        print(req)
        
        return render(
            request,
            "general.html",
            {
                "items": items,
                "categorias": models.Categorias.objects.filter(Tipo=tipo),
                "type": type,   
            }
        )
    return funcionGeneral


def item(request, id):
    item = models.Items.objects.get(ID=id)
    return render(
        request, 
        "item.html",
        {
            "seleccion": item
        }
    )