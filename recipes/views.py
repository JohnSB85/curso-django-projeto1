from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Jhonathan Bezerril'
    })


def contato(request):
    return HttpResponse('CONTATO 2')


def sobre(request):
    return HttpResponse('SOBRE 2')
