from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    context = {
        'text': 'Text of blog'
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