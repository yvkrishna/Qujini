from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.home,name="home"),
    path('addbooks/',views.addbooks,name="addbooks"),
    path('add_books/',views.add_books,name="add_books")
]