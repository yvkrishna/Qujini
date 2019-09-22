from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('hello world')

def hello(request):
    return HttpResponse('hello vk')

def main(request):
    #return render(request,'secondweb/new.html',{"name":"vedha krishna"})
    return HttpResponse(cd)