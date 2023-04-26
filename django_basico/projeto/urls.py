"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from home.views import home
# from blog.views import blog

'''
    Assim que nós adicionamos outra URL no nosso urlpatterns
    não conseguimos entrar na página antiga da doc do Django

    Importamos o HttpResponse por conta de precisarmos de uma resposta do servidor
    Assim que o usuário informar fizer a request(requisição)
'''
# Área administrativa do django 
# O path precisa receber uma rota e uma view, por padrão
#O include pega da raiz, ou seja precisamos passar o caminho correto
urlpatterns = [
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
