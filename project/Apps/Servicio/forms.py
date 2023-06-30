from django import forms
from . import models


class ServicioForm(forms.ModelForm):
    class Meta:
        model = models.Servicio
        fields = "__all__"