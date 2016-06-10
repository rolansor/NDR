from django.contrib.auth.decorators import login_required
from django.shortcuts import render


#@login_required
def inicio(request):
    context = {}
    return render(request, 'inicio.html', context)

def ingreso(request):
    context = {}
    return render(request, 'ingreso.html', context)

def reportes_geograficos(request):
    context = {}
    return render(request, 'reportes_geograficos.html', context)

def reportes_graficos(request):
    context = {}
    return render(request, 'reportes_graficos.html', context)

def reportes_fisicos(request):
    context = {}
    return render(request, 'reportes_fisicos.html', context)