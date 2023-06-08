from django.shortcuts import render


def blog(request):
    return render(
        request,
        template_name='blog/index.html',
        context={
            'text': 'Olá, você está no blog agora'
        }
    )

def exemplo(request):
    return render(
        request,
        template_name='blog/exemplo.html',
        context={
            'text': 'Olá, agora você viajou e está no exemplo',
            'title': 'Title for example - '
        }
    )