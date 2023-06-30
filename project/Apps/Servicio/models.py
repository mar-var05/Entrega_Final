from django.db import models

# Create your models here.

class Servicio(models.Model):   
    nombre= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    Precio = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now=True, editable=False)
    Ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False, verbose_name="Ultima Actualización")

    def __str__(self):
        return f"{self.nombre}-- {self.Precio:.2f}"
    
class Meta:
    verbose_name = "Servicio"
    verbose_name_plural = "Servicios"
