from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})

def login(request):
    pass

def forgot_password(request):
    pass



def login(request):
    pass

def forgot_password(request):
    pass

