from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

from . import forms

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Home/index.html")




