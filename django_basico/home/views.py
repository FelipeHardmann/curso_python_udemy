from django.shortcuts import render


def home(request):
    return render(
        request,
        template_name='home/index.html',
        context={
            'text': 'Olá home'
        }
    )