#from django.core.paginator import _SupportsPagination
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


#def index  (request:HttpRequest) -> HttpResponse:
#    return render(request,"Producto/index.html")

# List 

class ProductoDetail(DetailView):
    model = models.Producto


class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(Nombre__icontains=query)
        else:
            object_list = models.Producto.objects.all()
        return object_list      




# Create
class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("Producto:index")

   # def form_valid(self, form):
    #    form.instance.owner = self.request.user
     #   return super().form_valid(form)

# Delete
class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("Producto:Producto_list")

# Update (Actualizar)
class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy ("Producto:Producto_list")

# Detail (Detalle)
class ProductoDetail(DetailView):
    model = models.Producto