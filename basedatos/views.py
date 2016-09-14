from datetime import datetime

from decimal import Decimal
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import os.path

from NDR.settings import STATICFILES_DIRS
from models import *

@csrf_exempt
def recibirjson(request):
    context = {}
    if request.method =='POST':
        ##Obtenemos el archivo del post
        archivo = request.FILES["archivo"]

        ##Guardamos el archivo en el servidor
        guardada = save_file(archivo)

        if guardada == -1:
            #Ya existe el archivo httpcode = 201
            return HttpResponse(status=201)

        elif guardada == 1:
            #Si es una imagen, solo necesitamos subirla.
            if(str(archivo._get_name()).endswith('.jpg')):
                return HttpResponse(status=200)

            else:
                ##Transformamos el archivo en json
                json_encuesta = leer_json(archivo)

                ##Guardamos en la base el json
                sincronizada = guardar_encuesta(json_encuesta)

                ##Si ha sido guardada y sincronizada
                if sincronizada:
                    return HttpResponse(status=500)
                else:
                    return HttpResponse(status=500)
        else:
            return HttpResponse(status=500)

    else:
        return HttpResponse(status=200)

def save_file(file):
    filename = file._get_name()
    ruta = clasificarjson(str(filename))
    if os.path.isfile(ruta + filename ):
        return -1
    else:
        try:
            fd = open('%s%s' % (ruta, str(filename)), 'wb')
            for chunk in file.chunks():
                fd.write(chunk)
            fd.close()
            return 1
        except IOError:
            return 0

def clasificarjson(filename):
    a,b = filename.split("_")
    if a == 'prep':
        return '%s/preparacion/' % MEDIA_ROOT
    if a == 'cons':
        return '%s/consentimientos/' % STATICFILES_DIRS
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
        return data_json
    except IOError:
        return ""


def guardar_encuesta(json):
    tipo_formulario = json["tipo_formulario"]

    if tipo_formulario == "Preparacion":
        try:
            guardarpreparacion(json)
            return True
        except:
            return False
    elif tipo_formulario == "Informacion_General":
        try:
            guardarinformacion(json)
            return True
        except:
            return False
    elif tipo_formulario == "Medidas":
        try:
            guardarmedidas(json)
            return True
        except:
            return False
    elif tipo_formulario == "Presion":
        try:
            guardarpresion(json)
            return True
        except:
            return False
    elif tipo_formulario == "Laboratorio":
        try:
            guardarlaboratorio(json)
            return True
        except:
            return False


def guardarpreparacion(json):
    codigo_encuesta = json["id_formulario"]
    objeto = Preparacion()
    objeto.prep_fecha_creacion = datetime.strptime(json["hora_creacion"], "%A, %B %d %Y, %I:%M %p")
    objeto.prep_nombres = json["preparacion"][0]["nombres"]
    objeto.prep_ayunas = stringtobool(json["preparacion"][0]["ayunas"])
    objeto.prep_lugar = json["preparacion"][0]["lugar_encuesta"]
    objeto.prep_fecha = datetime.strptime(json["preparacion"][0]["fecha_encuesta"], "%A, %B %d %Y, %I:%M %p")
    objeto.prep_foto_cons = '/static/consentimientos/' + 'cons_' + json["id_formulario"] + '.jpg'
    objeto.prep_nombre_resp = json["nombres_encuestador"]
    objeto.prep_cedula_resp = json["cedula_encuestador"]
    objeto.prep_uuid_creado = json["uuid_creado"]

    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
        if encuesta.fk_preparacion is None:
            objeto.save()
            encuesta.enc_fecha_mod = datetime.now()
            encuesta.fk_preparacion = objeto
            encuesta.save()
        else:
            print "Ya existe la encuesta"
    except:
        objeto.save()
        encuesta = Encuesta()
        encuesta.enc_codigo = codigo_encuesta
        encuesta.enc_fecha_mod = datetime.now()
        encuesta.fk_preparacion = objeto
        encuesta.save()

def guardarinformacion(json):

    objeto = Informacion()
    datetime.now()
    objeto.inf_fecha_creacion = datetime.strptime(json["hora_creacion"], "%A, %B %d %Y, %I:%M %p")
    objeto.inf_nombre_resp = json["nombres_encuestador"]
    objeto.inf_cedula_resp = json["cedula_encuestador"]
    objeto.inf_uuid_creado = json["uuid_creado"]

    # Nombres
    objeto.inf_nombres = json["informacion_general"][0]["nombres"].upper().strip()

    # Apellidos
    objeto.inf_apellidos = json["informacion_general"][0]["apellidos"].upper().strip()

    # Sexo 0 Masculino/ 1 Femenino
    sexo = int(json["informacion_general"][0]["sexo"])
    if sexo == 0:
        objeto.inf_sexo = Catalogo.objects.get(id_catalogo=9)
    elif sexo == 1:
        objeto.inf_sexo = Catalogo.objects.get(id_catalogo=10)

    # Fecha Nacimiento
    datetime.now()
    objeto.inf_fecha_nac = datetime.strptime(json["informacion_general"][0]["fecha_nac"], "%d-%m-%Y")

    #Telefonos
    telefono = int(json["informacion_general"][0]["telefono"].strip())
    objeto.inf_telefono = telefono

    # Estado Civil
    est_civil = json["informacion_general"][0]["estado_civil"].upper().strip()
    objeto.inf_est_civil = Catalogo.objects.get(cat_descripcion=est_civil)

    # Etnia
    etnia = json["informacion_general"][0]["etnia"].upper().strip()
    objeto.inf_etnia = Catalogo.objects.get(cat_descripcion=etnia)

    #Canton
    canton = json["vivienda"][0]["canton"].upper().strip()
    test = Localidad.objects.filter(loc_padre__isnull=False).get(loc_descripcion=canton)
    objeto.inf_canton = Localidad.objects.filter(loc_padre__isnull=False).get(loc_descripcion=canton)

    #Provincia
    provincia =json["vivienda"][0]["provincia"].upper().strip()
    test = Localidad.objects.filter(loc_padre__isnull=True).get(loc_descripcion=provincia)
    objeto.inf_provincia = Localidad.objects.filter(loc_padre__isnull=True).get(loc_descripcion=provincia)

    #Vivienda
    vivienda = json["vivienda"][0]["vivienda"].upper().strip()
    objeto.inf_vivienda = Catalogo.objects.get(cat_descripcion=vivienda)

    #Direccion
    objeto.inf_direccion = json["vivienda"][0]["direccion"].upper().strip()

    #Personas
    objeto.inf_personas = int(json["vivienda"][0]["personas"])

    #Agua
    agua =  json["vivienda"][0]["agua"].upper().strip()
    objeto.inf_agua = Catalogo.objects.get(cat_descripcion=agua)

    #Cloacas
    cloacas = int(json["vivienda"][0]["cloacas"])
    if (cloacas == 1):
        objeto.inf_cloacas = True
    elif (cloacas == 0):
        objeto.inf_cloacas = False

    #Cabeza de Familia
    cbz_fam = int(json["economia_familiar"][0]["cbzfam"])
    if (cbz_fam == 1):
        objeto.inf_cbzfam = True
    elif (cbz_fam == 0):
        objeto.inf_cbzfam= False

    #Ingresos
    ingresos = int (json["economia_familiar"][0]["ingresos"])
    if (ingresos == 1):
        objeto.inf_ingresos = True
    elif (ingresos == 0):
        objeto.inf_ingresos = False

    #Llega a fin de Mes
    llega_fin = int(json["economia_familiar"][0]["llegafin"])
    if (llega_fin == 1):
        objeto.inf_llegafin = True
    elif (llega_fin == 0):
        objeto.inf_llegafin = False

    #Ocupacion
    ocupacion = json["economia_familiar"][0]["ocupacion"].upper().strip()
    objeto.inf_ocupacion = Catalogo.objects.get(cat_descripcion=ocupacion)

    #Trabajo
    objeto.inf_trabajo = json["economia_familiar"][0]["trabajo"].upper().strip()

    #Estudios
    estudios = json["economia_familiar"][0]["estudios"].upper().strip()
    objeto.inf_estudios = Catalogo.objects.get(cat_descripcion=estudios)

    #Seguro
    seguro = int (json["salud"][0]["seguro"])
    if (seguro == 1):
        objeto.inf_seguro = True
    elif (seguro == 0):
        objeto.inf_seguro = False

    #Detalle Seguro
    objeto.inf_det_seguro = json["salud"][0]["det_seguro"].upper().strip()

    #Chequeos
    chequeos = int(json["salud"][0]["chequeos"])
    if (chequeos == 1):
        objeto.inf_chequeos = True
    elif (chequeos == 0):
        objeto.inf_chequeos = False

    #Detalle chequeos por mes
    det_mes_chequeos = json["salud"][0]["det_mes_chequeo"]
    if det_mes_chequeos != "":
        objeto.inf_mes_chequeos = int(det_mes_chequeos)
    elif det_mes_chequeos == "":
        objeto.inf_mes_chequeos = 0

    #Detalle chequeos veces
    det_vec_chequeos = json["salud"][0]["det_vec_chequeo"]
    if det_vec_chequeos != "":
        objeto.inf_vec_chequeos = int(det_vec_chequeos)
    elif det_vec_chequeos == "":
        objeto.inf_vec_chequeos = 0

    #Diabetes
    diabetes = int(json["salud"][0]["diabetes"])
    if (diabetes == 1):
        objeto.inf_diabetes = True
    elif (diabetes == 0):
        objeto.inf_diabetes = False

    #Tiempo diabetes
    tiempo_diab = json["salud"][0]["det_tmp_diabetes"]
    if tiempo_diab != "":
        objeto.inf_tiempo_diab = int(tiempo_diab)
    elif tiempo_diab == "":
        objeto.inf_tiempo_diab = 0

    #Presion
    presion = int(json["salud"][0]["presion"])
    if (presion == 1):
        objeto.inf_presion = True
    elif (presion == 0):
        objeto.inf_presion = False

    #Enfermedad Renal
    enf_renal = int(json["salud"][0]["renal"])
    if (enf_renal == 1):
        objeto.inf_enf_renal = True
    elif (enf_renal == 0):
        objeto.inf_enf_renal = False

    #Detalle Enfermedad Renal
    objeto.inf_det_renal = json["salud"][0]["det_renal"].upper().strip()

    #Otra enfermedad
    otra_enf = int(json["salud"][0]["enfermedad"])
    if (otra_enf == 1):
        objeto.inf_otra_enf = True
    elif (otra_enf == 0):
        objeto.inf_otra_enf = False

    #Detalle otra enfermedad
    objeto.inf_det_enf = json["salud"][0]["det_enfermedad"].upper().strip()

    #Insulina
    insulina = int(json["medicamentos"][0]["insulina"])
    if (insulina == 1):
        objeto.inf_insulina = True
    elif (insulina == 0):
        objeto.inf_insulina = False

    #Hipoglucemia
    hipoglucemia = int(json["medicamentos"][0]["hipoglucemias"])
    if (hipoglucemia == 1):
        objeto.inf_hipoglucemias = True
    elif (hipoglucemia == 0):
        objeto.inf_hipoglucemias = False

    #Detalle hipoglucemia
    objeto.inf_det_hipogluce = json["medicamentos"][0]["det_hipoglucemias"].upper().strip()

    #Razon 1
    razon_1 = int(json["medicamentos"][0]["razon_1"])
    if (razon_1 == 1):
        objeto.inf_razon_1 = True
    elif (razon_1 == 0):
        objeto.inf_razon_1 = False

    # Razon 2
    razon_2 = int(json["medicamentos"][0]["razon_2"])
    if (razon_2 == 1):
        objeto.inf_razon_2 = True
    elif (razon_2 == 0):
        objeto.inf_razon_2 = False

    # Razon 3
    razon_3 = int(json["medicamentos"][0]["razon_3"])
    if (razon_3 == 1):
        objeto.inf_razon_3 = True
    elif (razon_3 == 0):
        objeto.inf_razon_3 = False

    # Razon 4
    razon_4 = int(json["medicamentos"][0]["razon_4"])
    if (razon_4 == 1):
        objeto.inf_razon_4 = True
    elif (razon_4 == 0):
        objeto.inf_razon_4 = False

    #Medicamento para la presion
    med_presion = int(json["medicamentos"][0]["medicina_presion"])
    if (med_presion == 1):
        objeto.inf_med_presion = True
    elif (med_presion == 0):
        objeto.inf_med_presion = False

    #Detalle medicamento para la presion
    objeto.inf_det_med_pre = json["medicamentos"][0]["det_medicina_presion"].upper().strip()

    #Analgesicos
    analgesicos = int(json["medicamentos"][0]["analgesicos"])
    if (analgesicos == 1):
        objeto.inf_analgesicos = True
    elif (analgesicos == 0):
        objeto.inf_analgesicos = False

    #Detalle de analgesicos
    objeto.inf_det_analgesicos = json["medicamentos"][0]["det_analgesicos"].upper().strip()

    #Medicamentos Otros
    med_otros = int(json["medicamentos"][0]["medicinas_otros"])
    if (med_otros == 1):
        objeto.inf_med_otros = True
    elif (med_otros == 0):
        objeto.inf_med_otros = False

    #Detalle otros medicamentos
    objeto.inf_det_med_otros = json["medicamentos"][0]["det_medicinas_otros"].upper().strip()

    #Medicamento 1
    med_1 = int(json["medicamentos"][0]["med_1"])
    if (med_1 == 1):
        objeto.inf_med_1 = True
    elif (med_1 == 0):
        objeto.inf_med_1 = False

    # Medicamento 2
    med_2 = int(json["medicamentos"][0]["med_2"])
    if (med_2 == 1):
        objeto.inf_med_2 = True
    elif (med_2 == 0):
        objeto.inf_med_2 = False

    # Medicamento 3
    med_3 = int(json["medicamentos"][0]["med_3"])
    if (med_3 == 1):
        objeto.inf_med_3 = True
    elif (med_3 == 0):
        objeto.inf_med_3 = False

    #Glucosa en la sangre
    glucosa = int(json["antecedentes"][0]["ant_glucosa"])
    if (glucosa == 1):
        objeto.inf_glucosa = True
    elif (glucosa == 0):
        objeto.inf_glucosa = False

    #Diabetes familia
    dia_familia = int(json["antecedentes"][0]["ant_familia"])
    if (dia_familia == 1):
        objeto.inf_dia_familia = True
    elif (dia_familia == 0):
        objeto.inf_dia_familia = False

    #Diabetes parientes
    dia_parientes = int(json["antecedentes"][0]["ant_parientes"])
    if (dia_parientes == 1):
        objeto.inf_dia_parientes = True
    elif (dia_parientes == 0):
        objeto.inf_dia_parientes = False

    #Antecedentes Diabetes en el Embarazo
    ant_embarazo = int(json["antecedentes"][0]["ant_embarazo"])
    if (ant_embarazo == 1):
        objeto.inf_ant_embarazo = True
    elif (ant_embarazo == 0):
        objeto.inf_ant_embarazo = False

    #Antecedente Peso Hijos
    peso_hijos = int(json["antecedentes"][0]["ant_pso_hijos"])
    if (peso_hijos == 1):
        objeto.inf_peso_hijos = True
    elif (peso_hijos == 0):
        objeto.inf_peso_hijos = False

    #Antecedentes Presion Familia
    pre_familia = int(json["antecedentes"][0]["ant_presion"])
    if (pre_familia == 1):
        objeto.inf_pre_familia = True
    elif (pre_familia == 0):
        objeto.inf_pre_familia = False

    #Antecedentes Enfermedad Renal Familiar
    renal_familia = int(json["antecedentes"][0]["ant_renal"] )
    if (renal_familia == 1):
        objeto.inf_renal_familia = True
    elif (renal_familia == 0):
        objeto.inf_renal_familia = False

    #Detalle enfermedad renal familiar
    objeto.inf_det_renal_fam = json["antecedentes"][0]["det_ant_enf_renal"].upper().strip()

    #Tabaco
    tabaco = int(json["habitos"][0]["tabaco"])
    if (tabaco == 1):
        objeto.inf_tabaco = True
    elif (tabaco == 0):
        objeto.inf_tabaco = False

    #Detalle frecuencia tabaco
    det_tabaco = json["habitos"][0]["det_frc_tabaco"]
    if det_tabaco != "":
        objeto.inf_det_tabaco = int(det_tabaco)
    elif det_tabaco == "":
        objeto.inf_det_tabaco = 0

    #Alcohol
    alcohol = int(json["habitos"][0]["alcohol"])
    if (alcohol == 1):
        objeto.inf_alcohol = True
    elif (alcohol == 0):
        objeto.inf_alcohol = False

    #Detalle frecuencia alcohol
    det_alcohol = json["habitos"][0]["det_frc_alcohol"]
    if det_alcohol != "":
        objeto.inf_det_alcohol = int(det_alcohol)
    elif det_alcohol == "":
        objeto.inf_det_alcohol = 0

    #Otros Habitos
    otros_hab = int(json["habitos"][0]["otros"])
    if (otros_hab == 1):
        objeto.inf_otros_hab = True
    elif (otros_hab == 0):
        objeto.inf_otros_hab = False

    #Detalles otros habitos
    objeto.inf_det_otro_hab = json["habitos"][0]["det_frc_otros"].upper().strip()

    #Ejercicios
    ejercicios = json["habitos"][0]["ejercicios"].upper().strip()
    objeto.inf_ejercicios = Catalogo.objects.get(cat_descripcion=ejercicios)

    codigo_encuesta = json["id_formulario"]

    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
        if encuesta.fk_informacion is None:
            objeto.save()
            encuesta.enc_fecha_mod = datetime.now()
            encuesta.fk_informacion = objeto
            encuesta.save()
        else:
            print "Ya existe la encuesta"
    except:
        objeto.save()
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

    objeto.med_nombre_resp = json["nombres_encuestador"]
    objeto.med_cedula_resp = json["cedula_encuestador"]
    objeto.med_uuid_creado = json["uuid_creado"]
    codigo_encuesta = json["id_formulario"]

    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
        if encuesta.fk_medidas is None:
            objeto.save()
            encuesta.enc_fecha_mod = datetime.now()
            encuesta.fk_medidas = objeto
            encuesta.save()
        else:
            print "Ya existe la encuesta"
    except:
        objeto.save()
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

    objeto.pres_nombre_resp = json["nombres_encuestador"]
    objeto.pres_cedula_resp = json["cedula_encuestador"]
    objeto.pres_uuid_creado = json["uuid_creado"]
    codigo_encuesta = json["id_formulario"]
    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
        if encuesta.fk_presion is None:
            objeto.save()
            encuesta.enc_fecha_mod = datetime.now()
            encuesta.fk_presion = objeto
            encuesta.save()
        else:
            print "Ya existe la encuesta"
    except:
        objeto.save()
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

    objeto.lab_nombre_resp = json["nombres_encuestador"]
    objeto.lab_cedula_resp = json["cedula_encuestador"]
    objeto.lab_uuid_creado = json["uuid_creado"]
    codigo_encuesta = json["id_formulario"]
    try:
        encuesta = Encuesta.objects.get(enc_codigo=codigo_encuesta)
        if encuesta.fk_laboratorio is None:
            objeto.save()
            encuesta.enc_fecha_mod = datetime.now()
            encuesta.fk_laboratorio = objeto
            encuesta.save()
        else:
            print "Ya existe la encuesta"
    except:
        objeto.save()
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