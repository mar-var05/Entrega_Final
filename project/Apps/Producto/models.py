from typing import Any

from django.db import models

# Create your models here.

class Producto(models.Model):
    Nombre = models.CharField(max_length=100, unique=True)
    Descripcion = models.CharField(max_length=300,blank=True, null=True)
    Precio = models.PositiveBigIntegerField()
    Cantidad = models.PositiveBigIntegerField()

    def __str__(self):
       return f"{self.Nombre} -- ${self.Precio}"


class Meta:
    verbose_name = "Producto"
    verbose_name_plural = "Productos"