# Generated by Django 4.2.20 on 2025-03-10 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagadurias', '0002_pagaduria_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagaduria',
            old_name='departamentos',
            new_name='departamento',
        ),
        migrations.RenameField(
            model_name='pagaduria',
            old_name='fecha_creacion',
            new_name='fechaCreacion',
        ),
        migrations.RenameField(
            model_name='pagaduria',
            old_name='razon_social',
            new_name='razonSocial',
        ),
    ]
