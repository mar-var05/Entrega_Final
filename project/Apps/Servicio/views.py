from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from . import forms,models
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
#def index(request: HttpRequest) -> HttpResponse:
 #   return render(request, "Servicio/index.html")


# List 

class ServicioDetail(DetailView):
    model = models.Servicio


class ServicioList(ListView):
    model = models.Servicio

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Servicio.objects.filter(Nombre__icontains=query)
        else:
            object_list = models.Servicio.objects.all()
        return object_list      




# Create
class ServicioCreate(LoginRequiredMixin,CreateView):
    model = models.Servicio
    form_class = forms.ServicioForm
    success_url = reverse_lazy("Servicio:index")

   # def form_valid(self, form):
    #    form.instance.owner = self.request.user
     #   return super().form_valid(form)

# Delete
class ServicioDelete(DeleteView):
    model = models.Servicio
    success_url = reverse_lazy("Servicio:Servicio_list")

# Update (Actualizar)
class ServicioUpdate(UpdateView):
    model = models.Servicio
    form_class = forms.ServicioForm
    success_url = reverse_lazy ("Servicio:Servicio_list")

# Detail (Detalle)
class ServicioDetail(DetailView):
    model = models.Servicio