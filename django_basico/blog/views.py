from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return render(
        request,
        'blog/blog.html'
    )

def example(request):
    return render(
        request,
        'blog/example.html'
    )