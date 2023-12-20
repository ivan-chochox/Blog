from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
   
    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    contenido = models.CharField(max_length=1450, verbose_name='Contenido')
    visible = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    imagen = models.ImageField(upload_to='blog/imagenes/')
    
    def __str__(self):
        return f'{self.contenido} - {self.creacion} - {self.actualizacion}'
    
class CategoriaArticulo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.articulo} - {self.categoria}'

class Autor(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    CategoriaArticulo = models.ForeignKey(CategoriaArticulo, on_delete=models.CASCADE)   
    

    def __str__(self):
        return self.nombre
