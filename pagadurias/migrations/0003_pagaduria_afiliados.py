# Generated by Django 4.2.7 on 2025-02-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagadurias', '0002_pagaduria_cdats_pagaduria_coviahorro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagaduria',
            name='afiliados',
            field=models.IntegerField(default=0, verbose_name='Número de Afiliados'),
        ),
    ]
