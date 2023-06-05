from django.shortcuts import render


def blog(request):
    return render(
        request,
        template_name='blog/index.html'
    )

def exemplo(request):
    return render(
        request,
        template_name='blog/exemplo.html'
    )