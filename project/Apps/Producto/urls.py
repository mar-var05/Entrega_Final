from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
   # path("", views.index, name="index"),
   path("",TemplateView.as_view(template_name = "Producto/index.html"), name ="index"),
    path("List_Producto/", views.ProductoList.as_view(), name ="List_Producto"),
    path("Create_Producto/", views.ProductoCreate.as_view(), name="Create_Producto"),
    path("Delete_Producto/<int:pk>", views.ProductoDelete.as_view(), name="Delete_Producto"),
    path("Update_Producto/<int:pk>", views.ProductoUpdate.as_view(), name="Update_Producto"),
]