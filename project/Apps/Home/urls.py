from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
]
urlpatterns += staticfiles_urlpatterns()
