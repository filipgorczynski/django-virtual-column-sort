# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 14:33
from __future__ import unicode_literals

from django.db import migrations, models


def populate_db(apps, schema_editor):
    CaseWhen = apps.get_model('casewhen', 'CaseWhen')
    records = CaseWhen.objects.all().count()
    initial = [
        'Beerinesses',
        'Bebeerines',
        'Bebeerine',
        'Beeriness',
        'Beer',
        'Beers',
        'Beery',
        'Ambeers',
        'Bebeerus',
        'Beerier',
        'Ambeer',
    ]
    for name in initial:
        CaseWhen(name=name).save()

class Migration(migrations.Migration):

    dependencies = [
        ('casewhen', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]
