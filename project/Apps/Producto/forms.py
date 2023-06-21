from django import forms
from . import models

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"

        widgets = {
            "Nombre": forms.TextInput(attrs={"class":"form-control"}),
            "Descripcion": forms.TextInput(attrs={"class":"form-control"}),
            "Precio": forms.TextInput(attrs={"class":"form-control"}),
        }