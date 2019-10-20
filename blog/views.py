from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
posts = [

    {
        'author': 'José Eduardo',
        'title': 'Blog Post',
        'content': 'First Post',
        'date_posted': 'October 19, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post',
        'content': 'Seconde Post',
        'date_posted': 'October 20, 2019'
    }

]


def home(request):
    context = {
        # 'posts': posts
        'posts':Post.objects.all()
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
