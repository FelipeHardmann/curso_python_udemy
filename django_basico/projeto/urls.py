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
from django.urls import path
from django.http import HttpResponse

# Utiliza o padrão MVT(MVC)
# O view é responsável por organizar, parecido com o controller
# Toda view recebe uma request e retorna uma response
def my_view(request):
    return HttpResponse('Erro 404 \
                        Essa página, não existe, por favor, tente outra URL')

def home(request):
    return HttpResponse('Home')

'''
    Assim que nós adicionamos outra URL no nosso urlpatterns
    não conseguimos entrar na página antiga da doc do Django

    Importamos o HttpResponse por conta de precisarmos de uma resposta do servidor
    Assim que o usuário informar fizer a request(requisição)
'''
# Área administrativa do django 
# O path precisa receber uma rota e uma view, por padrão
urlpatterns = [
    path('', home),
    path('blog/', my_view),
    path('admin/', admin.site.urls),
]