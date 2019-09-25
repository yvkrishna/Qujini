from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def home(request):
    return HttpResponse('hello vedha krishna books')

def add_books(request):
    return render(request,'addbook.html')

def addbooks(request):
    book_name=request.POST["bookname"]
    author_id=request.POST["authid"]
    genre=request.POST["genres"]
    
    Book.objects.create(name=book_name,genre=genre,author_id=author_id)
    return HttpResponse('added to database successfully')
