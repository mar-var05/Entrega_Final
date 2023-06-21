from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models. Model):
    Nombre_Producto = models.CharField(max_length=100, unique=True)
    Descripcion = models.CharField(max_length=150, null=True, blank=True)
    Precio = models.PositiveIntegerField(blank= True, null=True,default=0)    
    Se_encuentra_disponible = models.BooleanField(default=False)
    Cantidad = models.FloatField()
    
    def __str__(self):
        return f"{self.Nombre_Producto} -- {self.Precio} -- {self.Se_encuentra_disponible}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
