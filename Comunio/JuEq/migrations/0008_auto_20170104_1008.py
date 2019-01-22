# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-04 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JuEq', '0007_partido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='derrotas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='empates',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='goles_contra',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='goles_favor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='partidos_jugados',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='victorias',
            field=models.IntegerField(default=0),
        ),
    ]
