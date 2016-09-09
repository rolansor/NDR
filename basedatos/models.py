from __future__ import unicode_literals

from django.db import models

from NDR.settings import MEDIA_ROOT

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

class Preparacion(models.Model):
    id_preparacion = models.AutoField(primary_key=True)
    prep_fecha_creacion = models.DateTimeField()
    prep_nombres = models.CharField(max_length=150)
    prep_ayunas = models.BooleanField(default=False)
    prep_lugar = models.CharField(max_length=150)
    prep_fecha = models.DateField()
    prep_foto_cons = models.ImageField(upload_to='/static/consentimientos', null=True, blank=True)
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
    inf_sexo = models.ForeignKey(Catalogo, related_name="encuestado_sexo", limit_choices_to={'cat_padre': 1})
    inf_fecha_nac = models.DateField()
    inf_telefono = models.CharField(max_length=20)
    inf_est_civil = models.ForeignKey(Catalogo, related_name="encuestado_estcivil", limit_choices_to={'cat_padre': 4})
    inf_etnia = models.ForeignKey(Catalogo, related_name="encuestado_etnia", limit_choices_to={'cat_padre': 4})

    inf_canton = models.ForeignKey(Localidad, related_name="encuestado_canton")
    inf_provincia = models.ForeignKey(Localidad, related_name="encuestado_provincia")
    inf_vivienda = models.ForeignKey(Catalogo, related_name="encuestado_vivienda", limit_choices_to={'cat_padre': 4})
    inf_direccion = models.CharField(max_length=300)
    inf_personas = models.PositiveSmallIntegerField()
    inf_agua = models.ForeignKey(Catalogo, related_name="encuestado_agua", limit_choices_to={'cat_padre': 4})
    inf_cloacas = models.BooleanField()

    inf_cbzfam = models.BooleanField()
    inf_ingresos = models.BooleanField()
    inf_llegafin = models.BooleanField()
    inf_ocupacion = models.ForeignKey(Catalogo, related_name="encuestado_ocupacion", limit_choices_to={'cat_padre': 4})
    inf_trabajo = models.CharField(max_length=150)
    inf_estudios = models.ForeignKey(Catalogo, related_name="encuestado_estudios", limit_choices_to={'cat_padre': 4})

    inf_seguro = models.BooleanField()
    inf_det_seguro = models.CharField(max_length=150)
    inf_chequeos = models.BooleanField()
    inf_mes_chequeos = models.PositiveSmallIntegerField()
    inf_vec_chequeos = models.PositiveSmallIntegerField()
    inf_diabetes = models.BooleanField()
    inf_tiempo_diab = models.PositiveSmallIntegerField()
    inf_presion = models.BooleanField()
    inf_enf_renal = models.BooleanField()
    inf_det_renal = models.CharField(max_length=150)
    inf_otra_enf = models.BooleanField()
    inf_det_enf = models.CharField(max_length=150)

    inf_insulina = models.BooleanField()
    inf_hipoglucemias = models.BooleanField()
    inf_det_hipogluce = models.CharField(max_length=150)
    inf_razon_1 = models.BooleanField()
    inf_razon_2 = models.BooleanField()
    inf_razon_3 = models.BooleanField()
    inf_razon_4 = models.BooleanField()
    inf_med_presion = models.BooleanField()
    inf_det_med_pre = models.CharField(max_length=150)
    inf_analgesicos = models.BooleanField()
    inf_det_analgesicos = models.CharField(max_length=150)
    inf_med_otros = models.BooleanField()
    inf_det_med_otros = models.CharField(max_length=150)
    inf_med_1 = models.BooleanField()
    inf_med_2 = models.BooleanField()
    inf_med_3 = models.BooleanField()

    inf_glucosa = models.BooleanField()
    inf_dia_familia = models.BooleanField()
    inf_dia_parientes = models.BooleanField()
    inf_ant_embarazo = models.BooleanField()
    inf_peso_hijos = models.BooleanField()
    inf_pre_familia = models.BooleanField()
    inf_renal_familia = models.BooleanField()
    inf_det_renal_fam = models.CharField(max_length=150)

    inf_tabaco = models.BooleanField()
    inf_det_tabaco = models.PositiveSmallIntegerField()
    inf_alcohol = models.BooleanField()
    inf_det_alcohol = models.PositiveSmallIntegerField()
    inf_otros_hab = models.BooleanField()
    inf_det_otro_hab = models.CharField(max_length=150)
    inf_ejercicios = models.ForeignKey(Catalogo, related_name="encuestado_ejercicios", limit_choices_to={'cat_padre': 4})

    # Campos de auditoria:
    inf_nombre_resp = models.CharField(max_length=150)
    inf_cedula_resp = models.CharField(max_length=10)
    inf_uuid_creado = models.CharField(max_length=36)


    class Meta:
        db_table = 'informacion_general'

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