from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('hello',views.hello,name='abc'),
    path('main',views.main,name='abc')
]