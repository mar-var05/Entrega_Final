from typing import Any

from django.db import models
from django.utils import timezone


# Create your models here.

class Producto(models.Model):
    Nombre = models.CharField(max_length=100, unique=True)
    Descripcion = models.CharField(max_length=300,blank=True, null=True)
    Precio = models.PositiveBigIntegerField()
    Cantidad = models.PositiveBigIntegerField()
    Ultima_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Ultima Actualización")
    imagen = models.ImageField(upload_to="Producto", blank=True, null=True)

    def __str__(self):
       return f"{self.Nombre} -- ${self.Precio:.2f}"


class Meta:
    verbose_name = "Producto"
    verbose_name_plural = "Productos"