from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(forms.Form):
    Student=forms.RadioSelect()
    Teacher=forms.RadioSelect()
    # Username=forms.CharField(max_length=100,required=True)
    Email=forms.EmailField(required=True)
    Password1=forms.PasswordInput()
    Password2=forms.PasswordInput()
    
    # class Meta:
    #     model=User
    #     fields=['Student','Teacher','Name','Email','Password1','password2']