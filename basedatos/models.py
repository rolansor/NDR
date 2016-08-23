from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User

from django.db import models

def definir_ruta_imagen(self, filename):
    return "cons_informados/%s" % (filename)

class Preparacion(models.Model):
    id_preparacion = models.AutoField(primary_key=True)
    prep_fecha_creacion = models.DateTimeField()
    prep_nombres = models.CharField(max_length=150)
    prep_ayunas = models.BooleanField(default=False)
    prep_lugar = models.CharField(max_length=150)
    prep_fecha = models.DateField()
    prep_foto_cons = models.ImageField(upload_to=definir_ruta_imagen, default='noimagen.png')

    #Campos de auditoria:
    prep_nombre_resp = models.CharField(max_length=150)
    prep_cedula_resp = models.CharField(max_length=10)
    prep_uuid_creado = models.CharField(max_length=36)


    class Meta:
        db_table = 'preparacion'

class Medidas(models.Model):
    id_medidas = models.AutoField(primary_key=True)
    med_fecha_creacion = models.DateTimeField()
    med_nombres = models.CharField(max_length=150)
    med_peso = models.DecimalField(max_digits=5, decimal_places=2)
    med_estatura = models.PositiveSmallIntegerField()
    med_caderas = models.PositiveSmallIntegerField()
    med_cintura = models.PositiveSmallIntegerField()
    med_imc = models.DecimalField(max_digits=5, decimal_places=2)
    med_indice_cc = models.DecimalField(max_digits=5, decimal_places=2)
    med_peso_sal = models.DecimalField(max_digits=5, decimal_places=2)

    #Campos de auditoria:
    med_nombre_resp = models.CharField(max_length=150)
    med_cedula_resp = models.CharField(max_length=10)
    med_uuid_creado = models.CharField(max_length=36)

    class Meta:
        db_table = 'medidas'

class Laboratorio(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)
    lab_fecha_creacion = models.DateTimeField()
    lab_nombres = models.CharField(max_length=150)
    lab_glucosa_min = models.DecimalField(max_digits=5, decimal_places=2)
    lab_glucosa_max = models.DecimalField(max_digits=5, decimal_places=2)
    lab_hemo_glico = models.PositiveSmallIntegerField()
    lab_microalbum = models.PositiveSmallIntegerField()
    lab_creatinina = models.PositiveSmallIntegerField()
    lab_filtrado = models.DecimalField(max_digits=5, decimal_places=2)

    #Campos de auditoria:
    lab_nombre_resp = models.CharField(max_length=150)
    lab_cedula_resp = models.CharField(max_length=10)
    lab_uuid_creado = models.CharField(max_length=36)

    class Meta:
        db_table = 'laboratorio'

class Presion(models.Model):
    id_presion = models.AutoField(primary_key=True)
    pres_fecha_creacion = models.DateTimeField()
    pres_nombres = models.CharField(max_length=150)
    pres_min_1 = models.PositiveSmallIntegerField()
    pres_min_2 = models.PositiveSmallIntegerField()
    pres_min_3 = models.PositiveSmallIntegerField()
    pres_max_1 = models.PositiveSmallIntegerField()
    pres_max_2 = models.PositiveSmallIntegerField()
    pres_max_3 = models.PositiveSmallIntegerField()
    pres_prom_min = models.PositiveSmallIntegerField()
    pres_prom_max = models.PositiveSmallIntegerField()
    #Campos de auditoria:
    pres_nombre_resp = models.CharField(max_length=150)
    pres_cedula_resp = models.CharField(max_length=10)
    pres_uuid_creado = models.CharField(max_length=36)

    class Meta:
        db_table = 'presion'


class Encuesta(models.Model):
    id_encuesta = models.AutoField(primary_key=True)
    enc_codigo = models.CharField(max_length=7)
    enc_fecha_mod = models.DateTimeField()
    fk_preparacion = models.ForeignKey(Preparacion, related_name="fk_preparacion", null=True)
    fk_medidas = models.ForeignKey(Medidas, related_name="fk_medidas", null=True)
    fk_laboratorio = models.ForeignKey(Laboratorio, related_name="fk_laboratorio", null=True)
    fk_presion = models.ForeignKey(Presion, related_name="fk_presion", null=True)
    #fk_informacion = models.ForeignKey(Preparacion, related_name="fk_preparacion", null=True)

    class Meta:
        db_table = 'encuesta'