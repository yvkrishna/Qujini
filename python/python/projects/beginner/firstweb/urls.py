from django.urls import path
from . import views

urlpatterns=[
     path('',views.start, name='start'),
     path('start/',views.open,name='open'),
     path('blog/',views.lists,name='lists'),
     path('blog/send',views.send,name="send")
]