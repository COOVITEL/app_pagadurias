from django.db import migrations

def update_estados(apps, schema_editor):
    CitaProgramada = apps.get_model('citas', 'CitaProgramada')
    # Actualizar los estados existentes
    CitaProgramada.objects.filter(estado='programada').update(estado='Programada')
    CitaProgramada.objects.filter(estado='completada').update(estado='Completada')
    CitaProgramada.objects.filter(estado='cancelada').update(estado='Cancelada')

class Migration(migrations.Migration):
    dependencies = [
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_estados),
    ]
