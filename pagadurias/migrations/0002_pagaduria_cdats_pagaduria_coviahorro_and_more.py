# Generated by Django 5.1.6 on 2025-02-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagadurias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagaduria',
            name='cdats',
            field=models.IntegerField(default=0, verbose_name='Número de CDATs'),
        ),
        migrations.AddField(
            model_name='pagaduria',
            name='coviahorro',
            field=models.IntegerField(default=0, verbose_name='Número de Coviahorro'),
        ),
        migrations.AddField(
            model_name='pagaduria',
            name='creditos',
            field=models.IntegerField(default=0, verbose_name='Número de Créditos'),
        ),
    ]
