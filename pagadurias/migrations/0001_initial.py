# Generated by Django 5.1.6 on 2025-03-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagaduria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre de la Pagaduría')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('razonSocial', models.CharField(max_length=200)),
                ('sigla', models.CharField(max_length=200)),
                ('nit', models.CharField(max_length=200)),
                ('tipoEmpresa', models.CharField(choices=[('Pública', 'Pública'), ('Descentralizada', 'Descentralizada'), ('Privada', 'Privada'), ('Sin ánimo de lucro', 'Sin ánimo de lucro')], max_length=100, verbose_name='Tipo de Empresa')),
                ('actividadEconomica', models.CharField(max_length=200)),
                ('estado', models.CharField(blank=True, default='Por aprobar', max_length=200, null=True)),
                ('departamento', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=500)),
                ('totalEmpleados', models.IntegerField()),
                ('empleadosIndefinidos', models.IntegerField()),
                ('empleadosFijo', models.IntegerField()),
                ('empleadosObraLabor', models.IntegerField()),
                ('empleadosOtros', models.IntegerField()),
                ('empleadosSalario1y2', models.IntegerField()),
                ('empleadosSalario2y4', models.IntegerField()),
                ('empleadosSalariomax4', models.IntegerField()),
                ('nombreRepresentante', models.CharField(max_length=300)),
                ('numeroCedulaRepresentante', models.IntegerField()),
                ('correoRepresentante', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('cedulaRepresentante', models.FileField(upload_to='files/')),
                ('visacionLibranza', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=5)),
                ('visacionMedio', models.CharField(choices=[('Correo', 'Correo'), ('Fisico', 'Fisico')], max_length=20)),
                ('maxDescuentoNomina', models.FloatField()),
                ('fechaMaxEnvioCuentaCobro', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30')], max_length=10)),
                ('encargadoVisacionNombre', models.CharField(max_length=200)),
                ('encargadoVisacionCargo', models.CharField(max_length=200)),
                ('encargadoVisacionCorreo', models.EmailField(max_length=254)),
                ('encargadoVisacionTelefono', models.IntegerField()),
                ('encargadoVisacionDireccion', models.CharField(max_length=400)),
                ('encargadoEnvioCuentaNombre', models.CharField(max_length=200)),
                ('encargadoEnvioCuentaCargo', models.CharField(max_length=200)),
                ('encargadoEnvioCuentaCorreo', models.EmailField(max_length=254)),
                ('encargadoEnvioCuentaTelefono', models.IntegerField()),
                ('encargadoEnvioCuentaDireccion', models.CharField(max_length=400)),
                ('convenio', models.FileField(upload_to='files/')),
                ('formulariovinculacion', models.FileField(upload_to='files/')),
                ('tarjetasFirma', models.FileField(upload_to='files/')),
                ('rut', models.FileField(upload_to='files/')),
                ('camaraComercio', models.FileField(upload_to='files/')),
                ('estadosFinancieros', models.FileField(upload_to='files/')),
                ('declaracionRenta', models.FileField(upload_to='files/')),
                ('centrales', models.FileField(upload_to='files/')),
                ('composicionAccionaria', models.FileField(upload_to='files/')),
            ],
        ),
    ]
