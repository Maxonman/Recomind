from django.db import models

# Create your models here.

class Tipos(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.Nombre


class Directores(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Nombre

class Categorias(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.Nombre
    
class Items(models.Model):
    ID = models.AutoField(primary_key=True)
    Tipo = models.ForeignKey(Tipos, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=100)
    Imagen = models.CharField(max_length=100, null=True)
    Descripcion = models.CharField(max_length=1000)
    Categorias = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    Valoracion = models.FloatField()
    Year = models.IntegerField()
    Director = models.ForeignKey(Directores, on_delete=models.SET_NULL, null=True)
    Terminado = models.BooleanField()
    Last_Update = models.DateField()
    Cantidad_Capitulos = models.IntegerField()
    
    def __str__(self):
        return self.Nombre
    

    
class Categorias_Aplicadas(models.Model):
    ID = models.AutoField(primary_key=True)
    Categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    Item = models.ForeignKey(Items, on_delete=models.CASCADE)

class Estudio(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Nombre

class Desarrollador(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nombre