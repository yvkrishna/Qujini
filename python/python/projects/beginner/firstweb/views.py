from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User

def start(request):
    return HttpResponse("hello world")


def open(request):
    return HttpResponse('welcome vedha krishna')


def lists(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'firstweb/post_list.html',{'posts':post})

def send(request):
    titles=request.GET['title']
    texts=request.GET['info']
    # post=[title,text]
    me=User.objects.get(username='vedhakrishna')
    Post.objects.create(author=me,title=titles,text=texts)
    new_post=Post.objects.get(title=titles)
    new_post.publish()
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'firstweb/post_list.html',{'posts':post})