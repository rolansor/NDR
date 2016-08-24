from __future__ import unicode_literals

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


class Informacion(models.Model):
    id_informacion = models.AutoField(primary_key=True)
    inf_fecha_creacion = models.DateTimeField()
    inf_nombres = models.CharField(max_length=150)
    inf_apellidos = models.CharField(max_length=150)
    inf_sexo = models.CharField(max_length=150)
    inf_fecha_nac = models.CharField(max_length=150)
    inf_telefono = models.CharField(max_length=150)
    inf_est_civil = models.CharField(max_length=150)
    inf_etnia = models.CharField(max_length=150)
    inf_canton = models.CharField(max_length=150)
    inf_provincia = models.CharField(max_length=150)
    inf_vivienda = models.CharField(max_length=150)
    inf_direccion = models.CharField(max_length=150)
    inf_personas = models.CharField(max_length=150)
    inf_agua = models.CharField(max_length=150)
    inf_cloacas = models.CharField(max_length=150)
    inf_cbzfam = models.CharField(max_length=150)
    inf_ingresos = models.CharField(max_length=150)
    inf_llegafin = models.CharField(max_length=150)
    inf_ocupacion = models.CharField(max_length=150)
    inf_trabajo = models.CharField(max_length=150)
    inf_estudios = models.CharField(max_length=150)
    inf_seguro = models.CharField(max_length=150)
    inf_det_seguro = models.CharField(max_length=150)
    inf_chequeos = models.CharField(max_length=150)
    inf_mes_chequeos = models.CharField(max_length=150)
    inf_vec_chequeos = models.CharField(max_length=150)
    inf_diabetes = models.CharField(max_length=150)
    inf_tiempo_diab = models.CharField(max_length=150)
    inf_presion = models.CharField(max_length=150)
    inf_enf_renal = models.CharField(max_length=150)
    inf_det_renal = models.CharField(max_length=150)
    inf_otra_enf = models.CharField(max_length=150)
    inf_det_enf = models.CharField(max_length=150)
    inf_insulina = models.CharField(max_length=150)
    inf_hipoglucemias = models.CharField(max_length=150)
    inf_det_hipogluce = models.CharField(max_length=150)
    inf_razon_1 = models.CharField(max_length=150)
    inf_razon_2 = models.CharField(max_length=150)
    inf_razon_3 = models.CharField(max_length=150)
    inf_razon_4 = models.CharField(max_length=150)
    inf_med_presion = models.CharField(max_length=150)
    inf_det_med_pre = models.CharField(max_length=150)
    inf_analgesicos = models.CharField(max_length=150)
    inf_det_analgesicos = models.CharField(max_length=150)
    inf_med_otros = models.CharField(max_length=150)
    inf_det_med_otros = models.CharField(max_length=150)
    inf_med_1 = models.CharField(max_length=150)
    inf_med_2 = models.CharField(max_length=150)
    inf_med_3 = models.CharField(max_length=150)
    inf_glucosa = models.CharField(max_length=150)
    inf_dia_familia = models.CharField(max_length=150)
    inf_dia_parientes = models.CharField(max_length=150)
    inf_ant_embarazo = models.CharField(max_length=150)
    inf_peso_hijos = models.CharField(max_length=150)
    inf_pre_familia = models.CharField(max_length=150)
    inf_renal_familia = models.CharField(max_length=150)
    inf_det_renal_fam = models.CharField(max_length=150)
    inf_tabaco = models.CharField(max_length=150)
    inf_det_tabaco = models.CharField(max_length=150)
    inf_alcohol = models.CharField(max_length=150)
    inf_det_alcohol = models.CharField(max_length=150)
    inf_otros_hab = models.CharField(max_length=150)
    inf_det_otro_hab = models.CharField(max_length=150)
    inf_ejercicios = models.CharField(max_length=150)

    # Campos de auditoria:
    inf_nombre_resp = models.CharField(max_length=150)
    inf_cedula_resp = models.CharField(max_length=10)
    inf_uuid_creado = models.CharField(max_length=36)


    class Meta:
        db_table = 'informacion_general'

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    loc_codigo = models.CharField(max_length=3)
    loc_descripcion = models.CharField(max_length=150)
    loc_padre = models.ForeignKey('self', related_name='hijos', null=True,blank=True)

    class Meta:
        db_table = 'localidad'

class Catalogo(models.Model):
    id_catalogo = models.AutoField(primary_key=True)
    cat_descripcion = models.CharField(max_length=150)
    cat_padre = models.ForeignKey('self', related_name='hijos', null=True, blank=True)

    class Meta:
        db_table = 'catalogo'


class Encuesta(models.Model):
    id_encuesta = models.AutoField(primary_key=True)
    enc_codigo = models.CharField(max_length=7)
    enc_fecha_mod = models.DateTimeField()
    fk_preparacion = models.ForeignKey(Preparacion, related_name="fk_preparacion", null=True, blank=True)
    fk_medidas = models.ForeignKey(Medidas, related_name="fk_medidas", null=True, blank=True)
    fk_laboratorio = models.ForeignKey(Laboratorio, related_name="fk_laboratorio", null=True, blank=True)
    fk_presion = models.ForeignKey(Presion, related_name="fk_presion", null=True, blank=True)
    fk_informacion = models.ForeignKey(Informacion, related_name="fk_informacion", null=True, blank=True)

    class Meta:
        db_table = 'encuesta'