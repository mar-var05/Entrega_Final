from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
     path("", TemplateView.as_view(template_name="Posteos/index.html"), name="index"),
     path("list/", views.PosteosList.as_view(), name="Posteos_list"),
     path("create/", views.PosteosCreate.as_view(), name="Posteos_create"),
    path("delete/<int:pk>", views.PosteosDelete.as_view(), name="Posteos_delete"),
    path("update/<int:pk>", views.PosteosUpdate.as_view(), name="Posteos_update"),
    path("detail/<int:pk>", views.PosteosDetail.as_view(), name="Posteos_detail"),

     
]