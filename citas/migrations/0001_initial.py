# Generated by Django 5.2 on 2025-04-02 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Asesor',
                'verbose_name_plural': 'Asesores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pagaduria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Pagaduría',
                'verbose_name_plural': 'Pagadurías',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='CitaProgramada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asesor', models.CharField(max_length=255, verbose_name='Asesor')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('estado', models.CharField(choices=[('Programada', 'Programada'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')], default='programada', max_length=20, verbose_name='Estado')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
                ('notas', models.TextField(blank=True, null=True, verbose_name='Notas')),
                ('pagaduria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.pagaduria', verbose_name='Pagaduría')),
            ],
            options={
                'verbose_name': 'Cita Programada',
                'verbose_name_plural': 'Citas Programadas',
                'ordering': ['-fecha', '-hora'],
                'unique_together': {('fecha', 'hora')},
            },
        ),
    ]
