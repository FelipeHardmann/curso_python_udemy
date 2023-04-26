from django.contrib import admin
from django.urls import path
from blog.views import blog, exemplo

'''
    Toda url do blog, agora vai começar com blog/
    dessa forma, podemos criar um caminho para nossas urls
'''
urlpatterns = [
    path('', blog),
    path('exemplo', exemplo)
]