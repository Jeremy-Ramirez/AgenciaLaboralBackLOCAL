# Generated by Django 3.2.6 on 2021-08-26 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Formapago', '0001_initial'),
        ('Empresa', '0001_initial'),
        ('Estado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('idfactura', models.IntegerField(db_column='idFactura', primary_key=True, serialize=False)),
                ('numfactura', models.CharField(blank=True, db_column='numFactura', max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido', models.CharField(blank=True, max_length=45, null=True)),
                ('fechaemision', models.DateTimeField(blank=True, db_column='fechaEmision', null=True)),
                ('direccion', models.CharField(blank=True, max_length=45, null=True)),
                ('telefono', models.CharField(blank=True, max_length=45, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('subtotal', models.FloatField(blank=True, null=True)),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('iva', models.FloatField(blank=True, db_column='IVA', null=True)),
                ('ivatotal', models.FloatField(blank=True, db_column='IVAtotal', null=True)),
                ('codigotransaccion', models.CharField(blank=True, db_column='codigoTransaccion', max_length=45, null=True)),
                ('empresa_idempresa', models.ForeignKey(db_column='Empresa_idEmpresa', on_delete=django.db.models.deletion.DO_NOTHING, to='Empresa.empresa')),
                ('estado_idestado', models.ForeignKey(db_column='Estado_idEstado', on_delete=django.db.models.deletion.DO_NOTHING, to='Estado.estado')),
                ('formapago_idformapago', models.ForeignKey(db_column='FormaPago_idFormaPago', on_delete=django.db.models.deletion.DO_NOTHING, to='Formapago.formapago')),
            ],
            options={
                'db_table': 'factura',
            },
        ),
    ]