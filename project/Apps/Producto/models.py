from django.db import models

# Create your models here.

class Producto(models.Model):
    Nombre_Producto = models.CharField(max_length=100, unique=True)
    Descripcion = models.CharField(max_length=200,blank=True, null=True)
    Precio = models.PositiveBigIntegerField(blank=True, null=True,default=0)
    Cantidad = models.FloatField()

    def __str__(self):
       return f"{self.Nombre_Producto} -- {self.Precio}--{self.Cantidad}"    


class Meta:
    verbose_name = "Producto"
    verbose_name_plural = "Productos"