from datetime import datetime

from decimal import Decimal
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

@csrf_exempt
def recibirjson(request):
    context = {}
    if request.method =='POST':
        ##Obtenemos el archivo del post
        archivo = request.FILES["archivo"]

        ##Guardamos el archivo en el servidor
        guardada = save_file(archivo)

        if(str(archivo._get_name()).endswith('.jpg')):
            return HttpResponse(status=200)

        else:
            ##Transformamos el archivo en json
            json_encuesta = leer_json(archivo)

            ##Guardamos en la base el json
            sincronizada = guardar_encuesta(json_encuesta)

            ##Si ha sido guardada y sincronizada
            if guardada and sincronizada:
                return HttpResponse(status=200)
            elif guardada and not sincronizada:
                return HttpResponse(status=200)
            elif guardada and not sincronizada:
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=200)

    else:
        #temp = leer_json("infog_AB12345.json","/media/informacion_general/")
        #clasificarjson("infog_AB12345.json")
        return render(request, '/recibirjson', context)

def save_file(file):
    filename = file._get_name()
    ruta = clasificarjson(str(filename))
    try:
        fd = open('%s%s' % (ruta, str(filename)), 'wb')
        for chunk in file.chunks():
            fd.write(chunk)
        fd.close()
    except IOError:
        return False
    return True

def clasificarjson(filename):
    a,b = filename.split("_")
    if a == 'prep':
        return '%s/preparacion/encuestas/' % MEDIA_ROOT
    if a == 'cons':
        return '%s/preparacion/consentimientos/' % MEDIA_ROOT
    elif a == 'info':
        return '%s/informacion_general/' % MEDIA_ROOT
    elif a == 'medi':
        return '%s/medidas/' % MEDIA_ROOT
    elif a == 'pres':
        return '%s/presion/' % MEDIA_ROOT
    elif a == 'labo':
        return '%s/laboratorio/' % MEDIA_ROOT
    else:
        return '%s/default/' % MEDIA_ROOT

def leer_json(file):
    filename = file._get_name()
    ruta = clasificarjson(str(filename))
    try:
        f = open('%s%s' % (ruta,str(filename)),'r')
        json_string = f.read()
        f.close()
        data_json = json.loads(json_string)
    except IOError:
        return ""
    return data_json

def guardar_encuesta(json):
    tipo_formulario = json["tipo_formulario"]

    if tipo_formulario == "Preparacion":
        guardarpreparacion(json)

    elif tipo_formulario == "Informacion_General":
        guardarinformacion(json)

    elif tipo_formulario == "Medidas":
        guardarmedidas(json)

    elif tipo_formulario == "Presion":
        guardarpresion(json)

    elif tipo_formulario == "Laboratorio":
        guardarlaboratorio(json)

    return True


def guardarpreparacion(json):
    objeto = Preparacion()
    objeto.prep_fecha_creacion = datetime.strptime(json["hora_creacion"], "%A, %B %d %Y, %I:%M %p")
    objeto.prep_nombres = json["preparacion"][0]["nombres"]
    objeto.prep_ayunas = stringtobool(json["preparacion"][0]["ayunas"])
    objeto.prep_lugar = json["preparacion"][0]["lugar_encuesta"]
    objeto.prep_fecha = datetime.strptime(json["preparacion"][0]["fecha_encuesta"], "%A, %B %d %Y, %I:%M %p")
    objeto.prep_foto_cons = '%s/preparacion/consentimientos/no_image.png' % MEDIA_ROOT
    objeto.prep_nombre_resp = ""
    objeto.prep_cedula_resp = ""
    objeto.prep_uuid_creado = json["uuid_creado"]
    objeto.save()
    codigo_encuesta = json["id_formulario"]
    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
    except:
        encuesta = None

    if encuesta is not None:
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_preparacion = objeto
        encuesta.save()
    if encuesta is None:
        encuesta = Encuesta()
        encuesta.enc_codigo = codigo_encuesta
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_preparacion = objeto
        encuesta.save()

def guardarinformacion(json):
    objeto = Informacion()
    objeto.inf_fecha_creacion = datetime.strptime(json["hora_creacion"], "%A, %B %d %Y, %I:%M %p")
    objeto.inf_nombre_resp = ""
    objeto.inf_cedula_resp = ""
    objeto.inf_uuid_creado = json["uuid_creado"]
    objeto.inf_sexo = json["informacion_general"][0]["sexo"]

    codigo_encuesta = json["id_formulario"]
    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
    except:
        encuesta = None

    if encuesta is not None:
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_informacion = objeto
        encuesta.save()
    if encuesta is None:
        encuesta = Encuesta()
        encuesta.enc_codigo = codigo_encuesta
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_informacion = objeto
        encuesta.save()

def guardarmedidas(json):
    objeto = Medidas()
    objeto.med_fecha_creacion = datetime.strptime(json["hora_creacion"], "%A, %B %d %Y, %I:%M %p")
    objeto.med_nombres = json["medidas"][0]["nombres"]
    peso = Decimal(json["medidas"][0]["peso"])
    estatura = int(json["medidas"][0]["estatura"])
    cintura = int(json["medidas"][0]["med_cintura"])
    cadera = int(json["medidas"][0]["med_cadera"])
    imc = peso / ((estatura/100) * (estatura/100))
    cc = cintura/cadera
    peso_sal = (estatura/100) * (estatura/100) * 25
    objeto.med_peso = peso
    objeto.med_estatura = estatura
    objeto.med_caderas = cadera
    objeto.med_cintura = cintura
    objeto.med_imc = imc
    objeto.med_indice_cc = cc
    objeto.med_peso_sal = peso_sal

    objeto.med_nombre_resp = ""
    objeto.med_cedula_resp = ""
    objeto.med_uuid_creado = json["uuid_creado"]
    objeto.save()
    codigo_encuesta = json["id_formulario"]
    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
    except:
        encuesta = None

    if encuesta is not None:
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_medidas = objeto
        encuesta.save()

    if encuesta is None:
        encuesta = Encuesta()
        encuesta.enc_codigo = codigo_encuesta
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_medidas = objeto
        encuesta.save()


def guardarpresion(json):
    objeto = Presion()
    objeto.pres_fecha_creacion = datetime.strptime(json["hora_creacion"], "%A, %B %d %Y, %I:%M %p")
    objeto.pres_nombres = json["presion"][0]["nombres"]

    pres_min_1 = int(json["presion"][0]["presion_min_1"])
    pres_min_2 = int(json["presion"][0]["presion_min_2"])
    pres_min_3 = int(json["presion"][0]["presion_min_3"])
    pres_max_1 = int(json["presion"][0]["presion_max_1"])
    pres_max_2 = int(json["presion"][0]["presion_max_2"])
    pres_max_3 = int(json["presion"][0]["presion_max_3"])

    objeto.pres_min_1 = pres_min_1
    objeto.pres_min_2 = pres_min_2
    objeto.pres_min_3 = pres_min_3
    objeto.pres_max_1 = pres_max_1
    objeto.pres_max_2 = pres_max_2
    objeto.pres_max_3 = pres_max_3

    pres_prom_min = (pres_min_1 + pres_min_2 + pres_min_3)/3
    pres_prom_max = (pres_max_1 + pres_max_2 + pres_max_3)/3

    objeto.pres_prom_min = pres_prom_min
    objeto.pres_prom_max = pres_prom_max

    objeto.pres_nombre_resp = ""
    objeto.pres_cedula_resp = ""
    objeto.pres_uuid_creado = json["uuid_creado"]
    objeto.save()
    codigo_encuesta = json["id_formulario"]
    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
    except:
        encuesta = None

    if encuesta is not None:
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_presion = objeto
        encuesta.save()
    if encuesta is None:
        encuesta = Encuesta()
        encuesta.enc_codigo = codigo_encuesta
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_presion = objeto
        encuesta.save()


def guardarlaboratorio(json):
    objeto = Laboratorio()
    objeto.lab_fecha_creacion = datetime.strptime(json["hora_creacion"], "%A, %B %d %Y, %I:%M %p")
    objeto.lab_nombres = json["resultados"][0]["nombres"]
    gluco_min = int(json["resultados"][0]["glucosa_min"])
    gluco_max = int(json["resultados"][0]["glucosa_max"])
    creatinina = Decimal(json["resultados"][0]["creatinina"])
    microalbum = Decimal(json["resultados"][0]["microalbuminuria"])
    hemo_glico = Decimal(json["resultados"][0]["hba1c"])

    objeto.lab_glucosa_min = gluco_min
    objeto.lab_glucosa_max = gluco_max
    objeto.lab_creatinina = creatinina
    objeto.lab_microalbum = microalbum
    objeto.lab_hemo_glico = hemo_glico
    objeto.lab_filtrado = 5.22

    objeto.lab_nombre_resp = ""
    objeto.lab_cedula_resp = ""
    objeto.lab_uuid_creado = json["uuid_creado"]
    objeto.save()
    codigo_encuesta = json["id_formulario"]
    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
    except:
        encuesta = None

    if encuesta is not None:
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_laboratorio = objeto
        encuesta.save()
    if encuesta is None:
        encuesta = Encuesta()
        encuesta.enc_codigo = codigo_encuesta
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_laboratorio = objeto
        encuesta.save()


def stringtobool(str):
    if str == 1:
        return True
    elif str == 0:
        return False
    else:
        return False