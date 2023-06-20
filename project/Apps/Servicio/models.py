from django.db import models

# Create your models here.

class Servicio(models.Model):   
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    Precio = models.PositiveIntegerField()
    servicio_disponible = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre_servicio}-- {self.Precio}--{self.servicio_disponible}"
    
class Meta:
    verbose_name = "Servicio"
    verbose_name_plural = "Servicios"
