from django.contrib.auth.decorators import login_required
from django.shortcuts import render


#@login_required
def inicio(request):
    context = {}
    return render(request, 'inicio.html', context)

def ingreso(request):
    context = {}
    return render(request, 'ingreso.html', context)