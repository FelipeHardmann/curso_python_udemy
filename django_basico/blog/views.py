from django.shortcuts import render
from blog.data import posts

# Create your views here.
def blog(request):
    context = {
        'text': 'Text of blog',
        'posts': posts
    }
    
    return render(
        request,
        'blog/blog.html',
        context
    )

def example(request):
    context = {
        'text': 'Text of example'
    }

    return render(
        request,
        'blog/example.html',
        context
    )