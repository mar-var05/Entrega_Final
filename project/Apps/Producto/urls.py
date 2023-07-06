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
    path("",TemplateView.as_view(template_name = "Producto/index.html"), name ="index"),
    path("list/", views.ProductoList.as_view(), name="Producto_list"),
    path("create/", user_passes_test(is_superuser, login_url='/login/')(views.ProductoCreate.as_view()), name="Producto_create"),
    path("delete/<int:pk>", views.ProductoDelete.as_view(), name="Producto_delete"),
    path("update/<int:pk>", views.ProductoUpdate.as_view(), name="Producto_update"),
    path("detail/<int:pk>", views.ProductoDetail.as_view(), name="Producto_detail"),
]
urlpatterns += staticfiles_urlpatterns()


# from django.urls import path
# from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib.auth.decorators import login_required 
# from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from django.views.generic import TemplateView

# urlpatterns = [
#   # path("", views.index, name="index"),
#   path("",TemplateView.as_view(template_name = "Producto/index.html"), name ="index"),
#    path("list/", views.ProductoList.as_view(), name ="Producto_list"),
#    path("create/", staff_member_required(views.ProductoCreate.as_view()), name="Producto_create"),
#    path("delete/<int:pk>", staff_member_required (views.ProductoDelete.as_view()), name="Producto_delete"),
#     path("update/<int:pk>",staff_member_required (views.ProductoUpdate.as_view()), name="Producto_update"),
#     path("detail/<int:pk>", staff_member_required(views.ProductoDetail.as_view()), name="Producto_detail"),
# ]
# urlpatterns += staticfiles_urlpatterns()
