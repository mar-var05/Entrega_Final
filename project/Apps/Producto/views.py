# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

from . import models

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Producto/index.html")

def Producto_detalle(request):
    detalle = models.Producto.objects.all()
    contexto = {"Producto":Producto_detalle}
    return render (request,"Producto/Producto_detalle.html",contexto)


