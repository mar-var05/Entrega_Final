from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("Producto_detalle", views.Producto_detalle, name="Producto_detalle")
]