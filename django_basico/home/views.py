from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        'text': 'Example of text at home'
    }

    return render(
        request,
        'home/home.html',
        context
    )