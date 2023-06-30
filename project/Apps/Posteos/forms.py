from django import forms
from . import models

class PosteosForm(forms.ModelForm):
    class Meta:
        model = models.Posteos
        fields = "__all__"
