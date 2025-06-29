# Generated by Django 4.2.20 on 2025-04-23 16:44

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pagadurias', '0010_rename_secursalespgaduria_sucursalespagaduria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagaduria',
            name='asesores',
            field=models.ManyToManyField(related_name='pagaduria', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagaduria',
            name='estadoOperaciones',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pagaduria',
            name='tokenControl',
            field=models.UUIDField(blank=True, default=uuid.UUID('bb352c75-8a45-49d5-b0d1-8610175ac971'), editable=False, null=True),
        ),
    ]
