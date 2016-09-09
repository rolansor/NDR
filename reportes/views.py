from django.shortcuts import render

from basedatos.models import Encuesta


def reportes_geograficos(request):
    context = {}
    return render(request, 'reportes_geograficos.html', context)

def reportes_graficos(request):
    context = {}
    return render(request, 'reportes_graficos.html', context)

def reportes_fisicos(request):
    context = {}
    encuestas = Encuesta.objects.all()
    context['encuestas'] = encuestas
    return render(request, 'reportes_fisicos.html', context)
