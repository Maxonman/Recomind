from django.contrib import admin
from .models import Tipos, Directores, Items, Categorias, Categorias_Aplicadas, Estudio , Desarrollador

# Register your models here.

admin.site.register(Tipos)
admin.site.register(Directores)
admin.site.register(Items)
admin.site.register(Categorias)
admin.site.register(Categorias_Aplicadas)
admin.site.register(Estudio)
admin.site.register(Desarrollador)
