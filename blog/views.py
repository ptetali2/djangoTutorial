from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    #dictonary of posts
    context = {
        'posts': Post.objects.all()
    }
    #goes to html template and returns http request
    return render(request, 'blog/home.html', context)
def about(request):
     return render(request, 'blog/about.html', {'title': 'About Page'})