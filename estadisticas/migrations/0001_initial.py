# Generated by Django 5.1.6 on 2025-03-03 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Generación')),
                ('total_creditos', models.IntegerField(default=0, verbose_name='Total de Créditos')),
                ('total_cdats', models.IntegerField(default=0, verbose_name='Total de CDATs')),
                ('total_coviahorro', models.IntegerField(default=0, verbose_name='Total de Coviahorro')),
                ('operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estadisticas', to='operaciones.operacion')),
            ],
        ),
    ]
