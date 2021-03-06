import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from basedatos.models import *

@csrf_exempt
def reportes_geograficos(request):
    context = {}
    if request.method == "POST":
        provincia = request.POST['provincia']
        sexo = request.POST['sexo']
        criterio = request.POST['criterio']

        provincias = []

        if provincia == '0':
            for x in range(0,6):
                mujeres_diab = Informacion.objects.filter(inf_sexo=9, inf_provincia=x, inf_diabetes=1).count()
                provincias.append(mujeres_diab)
            response={'busqueda': 'Mujeres con Diabetes',
                                            'ESM': provincias[0],'MAN': provincias[1],
                                            'GUA': provincias[2],'RIO': provincias[3],
                                            'ORO': provincias[4], 'SLN': provincias[5]}
            return HttpResponse(json.dumps(response), content_type='application/json')
        else:
            return render(request, 'reportes_geograficos.html', context)


    if request.method == "GET":
        provincias = Localidad.objects.filter(loc_padre__isnull=True)
        context['provincias'] = provincias
        sexo = Catalogo.objects.filter(cat_padre=1)
        context['sexo'] = sexo
        indicadores = Catalogo.objects.filter(cat_padre__isnull=False).exclude(cat_padre = 1)
        context['indicadores'] = indicadores
        return render(request, 'reportes_geograficos.html', context)

def reportes_graficos(request):
    context = {}
    if request.method == "GET":

        h_diab = Informacion.objects.filter(inf_sexo=9, inf_diabetes=1).count()
        m_diab = Informacion.objects.filter(inf_sexo=10, inf_diabetes=1).count()
        hombres = Informacion.objects.filter(inf_sexo=10).count()
        mujeres = Informacion.objects.filter(inf_sexo=10).count()
        diaxlocE = Informacion.objects.filter(inf_diabetes=1, inf_provincia=1).count()
        diaxlocM = Informacion.objects.filter(inf_diabetes=1, inf_provincia=2).count()
        diaxlocG = Informacion.objects.filter(inf_diabetes=1, inf_provincia=3).count()
        diaxlocO = Informacion.objects.filter(inf_diabetes=1, inf_provincia=5).count()
        diaxlocR = Informacion.objects.filter(inf_diabetes=1, inf_provincia=4).count()
        diaxlocS = Informacion.objects.filter(inf_diabetes=1, inf_provincia=6).count()

        insulinaE = Informacion.objects.filter(inf_insulina=1, inf_provincia=1).count()
        insulinaM = Informacion.objects.filter(inf_insulina=1, inf_provincia=2).count()
        insulinaG = Informacion.objects.filter(inf_insulina=1, inf_provincia=3).count()
        insulinaO = Informacion.objects.filter(inf_insulina=1, inf_provincia=5).count()
        insulinaR = Informacion.objects.filter(inf_insulina=1, inf_provincia=4).count()
        insulinaS = Informacion.objects.filter(inf_insulina=1, inf_provincia=6).count()


        context['h_diab'] = h_diab
        context['m_diab'] = m_diab
        context['hombres'] = hombres
        context['mujeres'] = mujeres
        context['diaxlocE'] = diaxlocE
        context['diaxlocM'] = diaxlocM
        context['diaxlocG'] = diaxlocG
        context['diaxlocO'] = diaxlocO
        context['diaxlocR'] = diaxlocR
        context['diaxlocS'] = diaxlocS
        context['insulinaE'] = insulinaE
        context['insulinaM'] = insulinaM
        context['insulinaG'] = insulinaG
        context['insulinaO'] = insulinaO
        context['insulinaR'] = insulinaR
        context['insulinaS'] = insulinaS


        return render(request, 'reportes_graficos.html', context)

    if request.method == "GET":
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

