from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
     path("",TemplateView.as_view(template_name = "Servicio/index.html"), name ="index"),
    path("list/", views.ServicioList.as_view(), name ="Servicio_list"),
    path("create/", views.ServicioCreate.as_view(), name="Servicio_create"),
    path("delete/<int:pk>", views.ServicioDelete.as_view(), name="Servicio_delete"),
    path("update/<int:pk>", views.ServicioUpdate.as_view(), name="Servicio_update"),
    path("detail/<int:pk>", views.ServicioDetail.as_view(), name="Servicio_detail"),
]