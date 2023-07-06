from django.db import models

# Create your models here.


class Posteos(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=120, blank=True, null=True)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now=True, editable=False)
    Ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False, verbose_name = "Ultima Actualización")
    image = models.ImageField(upload_to="Posteos", blank=True, null=True)



    def __str__(self):
      return self.titulo

    class Meta:
       verbose_name = "Posteo"
       verbose_name_plural = "Posteos"
