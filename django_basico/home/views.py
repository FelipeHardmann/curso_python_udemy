from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("You're in home")