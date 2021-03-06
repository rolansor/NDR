from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User


##@login_required
from basedatos.models import *

@login_required
def inicio(request):
    context = {}
    return render(request, 'inicio.html', context)

def ingreso(request):
    context = {}
    if request.method == 'GET':
        """
        user = User.objects.create_user(username='rolansor',
                                        email='rolansor@hotmail.com',
                                        password='1234', first_name= 'Andres',
                                        last_name='Sornoza')
        user.save()
        """
        return render(request, 'ingreso.html', context)

    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['contrasena']
        usuario = auth.authenticate(username=username, password=password)
        if usuario is not None:
            return render(request, 'inicio.html', context)
        else:
            context['mensajeLogin'] = 'Su nombre o usuario son incorrectos.'
            return render(request, 'ingreso.html', context)