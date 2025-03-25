# Generated by Django 4.2.19 on 2025-03-25 20:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pagadurias', '0003_alter_pagaduria_actividadeconomica_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagaduria',
            name='numeroCedulaRepresentante',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pagaduria',
            name='tokenControl',
            field=models.UUIDField(blank=True, default=uuid.UUID('efa8afa1-e8bd-4e74-ac02-09ddca693e1a'), editable=False, null=True),
        ),
    ]
