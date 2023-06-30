from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . import models, forms
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Posteos/index.html")


class PosteosList(ListView):
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Posteos.objects.filter(titulo__icontains=query)
        else:
            object_list = models.Posteos.objects.all()
        return object_list  
    

class PosteosCreate(CreateView):
    model = models.Posteos
    form_class = forms.PosteosForm
    success_url = reverse_lazy("Posteos:Posteos_list")


class PosteosUpdate(UpdateView):
    model = models.Posteos
    form_class = forms.PosteosForm
    success_url = reverse_lazy("Posteos:Posteos_list")


class PosteosDelete(DeleteView):
    model = models.Posteos
    success_url = reverse_lazy("Posteos:Posteos_list")


class PosteosDetail(DetailView):
    model = models.Posteos