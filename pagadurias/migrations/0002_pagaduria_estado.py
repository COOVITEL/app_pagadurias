# Generated by Django 4.2.20 on 2025-03-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagadurias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagaduria',
            name='estado',
            field=models.CharField(default='Por aprobar', max_length=200),
        ),
    ]
