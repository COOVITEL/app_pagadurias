# Generated by Django 5.1.6 on 2025-03-21 14:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagadurias', '0002_pagaduria_tokencontrol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagaduria',
            name='tokenControl',
            field=models.UUIDField(blank=True, default=uuid.UUID('4885c86d-74d6-4936-b1f3-3cc43205aeaf'), editable=False, null=True),
        ),
    ]
