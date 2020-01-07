from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime

# Create your views here.


def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', {"posts": posts, "now": now})

def showDetails(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'show_detail.html', locals())
    except:
        return redirect('/')