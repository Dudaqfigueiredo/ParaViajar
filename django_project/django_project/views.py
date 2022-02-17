from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def index(request):
    return render(request, 'blog/index.html')

    

def business(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/business.html',context)

