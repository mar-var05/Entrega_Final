from django.shortcuts import redirect,render
from django.http import HttpRequest,HttpResponse

from . import models
from . import forms
# Create your views here.

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#def index  (request:HttpRequest) -> HttpResponse:
 #   return render(request,"Producto/index.html")

class ProductoList(ListView):
    model = models.Producto
    template_name = "Producto/List_Producto.html"
    context_object_name = "List"

class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("Producto:List_Producto")


class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("Producto:List_Producto")


class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy ("Producto:List_Producto")


#class Producto            