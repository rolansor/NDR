# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-23 10:12
from __future__ import unicode_literals

import basedatos.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id_encuesta', models.AutoField(primary_key=True, serialize=False)),
                ('enc_codigo', models.CharField(max_length=7)),
                ('enc_fecha_mod', models.DateTimeField()),
            ],
            options={
                'db_table': 'encuesta',
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id_laboratorio', models.AutoField(primary_key=True, serialize=False)),
                ('lab_fecha_creacion', models.DateTimeField()),
                ('lab_nombres', models.CharField(max_length=150)),
                ('lab_glucosa_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lab_glucosa_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lab_hemo_glico', models.PositiveSmallIntegerField()),
                ('lab_microalbum', models.PositiveSmallIntegerField()),
                ('lab_creatinina', models.PositiveSmallIntegerField()),
                ('lab_filtrado', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lab_nombre_resp', models.CharField(max_length=150)),
                ('lab_cedula_resp', models.CharField(max_length=10)),
                ('lab_uuid_creado', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'laboratorio',
            },
        ),
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('id_medidas', models.AutoField(primary_key=True, serialize=False)),
                ('med_fecha_creacion', models.DateTimeField()),
                ('med_nombres', models.CharField(max_length=150)),
                ('med_peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('med_estatura', models.PositiveSmallIntegerField()),
                ('med_caderas', models.PositiveSmallIntegerField()),
                ('med_cintura', models.PositiveSmallIntegerField()),
                ('med_imc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('med_indice_cc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('med_peso_sal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('med_nombre_resp', models.CharField(max_length=150)),
                ('med_cedula_resp', models.CharField(max_length=10)),
                ('med_uuid_creado', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'medidas',
            },
        ),
        migrations.CreateModel(
            name='Preparacion',
            fields=[
                ('id_preparacion', models.AutoField(primary_key=True, serialize=False)),
                ('prep_fecha_creacion', models.DateTimeField()),
                ('prep_nombres', models.CharField(max_length=150)),
                ('prep_ayunas', models.BooleanField(default=False)),
                ('prep_lugar', models.CharField(max_length=150)),
                ('prep_fecha', models.DateField()),
                ('prep_foto_cons', models.ImageField(default='noimagen.png', upload_to=basedatos.models.definir_ruta_imagen)),
                ('prep_nombre_resp', models.CharField(max_length=150)),
                ('prep_cedula_resp', models.CharField(max_length=10)),
                ('prep_uuid_creado', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'preparacion',
            },
        ),
        migrations.CreateModel(
            name='Presion',
            fields=[
                ('id_presion', models.AutoField(primary_key=True, serialize=False)),
                ('pres_fecha_creacion', models.DateTimeField()),
                ('pres_nombres', models.CharField(max_length=150)),
                ('pres_min_1', models.PositiveSmallIntegerField()),
                ('pres_min_2', models.PositiveSmallIntegerField()),
                ('pres_min_3', models.PositiveSmallIntegerField()),
                ('pres_max_1', models.PositiveSmallIntegerField()),
                ('pres_max_2', models.PositiveSmallIntegerField()),
                ('pres_max_3', models.PositiveSmallIntegerField()),
                ('pres_prom_min', models.PositiveSmallIntegerField()),
                ('pres_prom_max', models.PositiveSmallIntegerField()),
                ('pres_nombre_resp', models.CharField(max_length=150)),
                ('pres_cedula_resp', models.CharField(max_length=10)),
                ('pres_uuid_creado', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'presion',
            },
        ),
        migrations.AddField(
            model_name='encuesta',
            name='fk_laboratorio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_laboratorio', to='basedatos.Laboratorio'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='fk_medidas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_medidas', to='basedatos.Medidas'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='fk_preparacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_preparacion', to='basedatos.Preparacion'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='fk_presion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_presion', to='basedatos.Presion'),
        ),
    ]