# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacion',
            name='inf_fecha_nac',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='preparacion',
            name='prep_foto_cons',
            field=models.ImageField(blank=True, null=True, upload_to='preparacion/consentimientos'),
        ),
    ]