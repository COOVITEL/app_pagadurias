# Generated by Django 5.2 on 2025-04-08 16:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagadurias', '0006_alter_pagaduria_tokencontrol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagaduria',
            name='tokenControl',
            field=models.UUIDField(blank=True, default=uuid.UUID('9d04cc82-3158-4010-bea5-172f2c8d1c9a'), editable=False, null=True),
        ),
    ]
