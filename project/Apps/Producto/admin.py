from django.contrib import admin
from . import models
# Register your models here.

#admin.site.register(models.Producto)

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("Nombre","Precio", "Cantidad")
    search_fields = ("Nombre",)
    list_filter = ("Nombre",)
    ordering = ("Nombre",)
    



