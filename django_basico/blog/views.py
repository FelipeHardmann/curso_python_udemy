from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    return HttpResponse("You're in my view")

def exemplo(request):
    return HttpResponse("You're in example")