from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("login/", LoginView.as_view(template_name="Home/login.html"), name="login"),
     path("register/", views.register, name="register"),
     path("about/", views.about, name="about"), 
     path("logout/", LogoutView.as_view(template_name="Home/logout.html"), name="logout"),
]
urlpatterns += staticfiles_urlpatterns()
