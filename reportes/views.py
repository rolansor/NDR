from django.shortcuts import render

from basedatos.models import *


def reportes_geograficos(request):
    context = {}
    return render(request, 'reportes_geograficos.html', context)

def reportes_graficos(request):
    context = {}
    return render(request, 'reportes_graficos.html', context)

def reportes_preparacion(request):
    context = {}
    encuestas = Encuesta.objects.filter(fk_preparacion__isnull=False)
    context['encuestas'] = encuestas
    return render(request, 'reportes_preparacion.html', context)

def reportes_informacion(request):
    context = {}
    encuestas = Encuesta.objects.filter(fk_informacion__isnull=False)
    context['encuestas'] = encuestas
    return render(request, 'reportes_informacion.html', context)

def reportes_medidas(request):
    context = {}
    encuestas = Encuesta.objects.filter(fk_medidas__isnull=False)
    context['encuestas'] = encuestas
    return render(request, 'reportes_medidas.html', context)

def reportes_presion(request):
    context = {}
    encuestas = Encuesta.objects.filter(fk_presion__isnull=False)
    context['encuestas'] = encuestas
    return render(request, 'reportes_presion.html', context)

def reportes_laboratorio(request):
    context = {}
    encuestas = Encuesta.objects.filter(fk_laboratorio__isnull=False)
    context['encuestas'] = encuestas
    return render(request, 'reportes_laboratorio.html', context)

def reportes_personalizado(request):
    context = {}
    encuestas = ""
    context['encuestas'] = encuestas
    return render(request, 'reportes_personalizado.html', context)