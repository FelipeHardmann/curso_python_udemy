# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return HttpResponse('Bem vindo ao blog')

def exemplo(request):
    return HttpResponse('Estamos no blog, na parte de exemplo')
