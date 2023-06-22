from django import forms
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth.models import User
#from UserProfile.models import Usuario


#class CustomerUserCreationForm(UserCreationForm):
    #class Meta:
        #model = Usuario
        #fiels = ("Username","Email_Address", "password1", "password2",)
        #widgets = {
            #"Username": forms.TextInput(attrs={"class":"form-control"}),
            #"Email_Address": forms.EmailInput(),
            #"password1": forms.PasswordInput(attrs={"class": "form-control"}),
            #"password2" : forms.PasswordInput(attrs={"class":"forms-control"}),
        #}


#class CustomAuthenticationForm(AuthenticationForm):
    #class Meta:
        #model = Usuario
        #fields = ["username", "password"]
        #widgets = {
            #"username": forms.TextInput(attrs={"class": "form-control"}),
            #"password": forms.PasswordInput(attrs={"class": "form-control"}),
        #}