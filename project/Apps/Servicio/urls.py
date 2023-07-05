
from django.urls import path
from django.contrib.auth.decorators import login_required, user_passes_test
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.models import User
from django.views.generic import TemplateView

def is_superuser(user):
    return user.is_authenticated and user.is_superuser

urlpatterns = [
    #path("", views.index, name="index"),
    path("",TemplateView.as_view(template_name = "Servicio/index.html"), name ="index"),
    path("list/", views.ServicioList.as_view(), name="Servicio_list"),
    path("create/", user_passes_test(is_superuser, login_url='/login/')(views.ServicioCreate.as_view()), name="Servicio_create"),
    path("delete/<int:pk>", views.ServicioDelete.as_view(), name="Servicio_delete"),
    path("update/<int:pk>", views.ServicioUpdate.as_view(), name="Servicio_update"),
    path("detail/<int:pk>", views.ServicioDetail.as_view(), name="Servicio_detail"),
]

urlpatterns += staticfiles_urlpatterns()

# from django.contrib.admin.views.decorators import staff_member_required
# from django.urls import path
# from . import views
# from django.views.generic import TemplateView

# urlpatterns = [
#      path("",TemplateView.as_view(template_name = "Servicio/index.html"), name ="index"),
#     path("list/", views.ServicioList.as_view(), name ="Servicio_list"),
#     path("create/", staff_member_required(views.ServicioCreate.as_view()), name="Servicio_create"),
#     path("delete/<int:pk>", views.ServicioDelete.as_view(), name="Servicio_delete"),
#     path("update/<int:pk>", views.ServicioUpdate.as_view(), name="Servicio_update"),
#     path("detail/<int:pk>", views.ServicioDetail.as_view(), name="Servicio_detail"),
# ]