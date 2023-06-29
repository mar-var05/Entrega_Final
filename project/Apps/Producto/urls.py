from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
   # path("", views.index, name="index"),
   path("",TemplateView.as_view(template_name = "Producto/index.html"), name ="index"),
    path("list/", views.ProductoList.as_view(), name ="Producto_list"),
    path("create/", views.ProductoCreate.as_view(), name="Producto_create"),
    path("delete/<int:pk>", views.ProductoDelete.as_view(), name="Producto_delete"),
    path("update/<int:pk>", views.ProductoUpdate.as_view(), name="Producto_update"),
    path("detail/<int:pk>", views.ProductoDetail.as_view(), name="Producto_detail"),
]