# Generated by Django 5.2 on 2025-04-08 16:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagadurias', '0007_alter_pagaduria_tokencontrol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagaduria',
            name='tokenControl',
            field=models.UUIDField(blank=True, default=uuid.UUID('9fcfc646-12a9-4cf9-af77-fd49e0acc228'), editable=False, null=True),
        ),
    ]
