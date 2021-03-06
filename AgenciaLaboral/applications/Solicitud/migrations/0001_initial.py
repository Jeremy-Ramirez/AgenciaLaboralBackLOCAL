# Generated by Django 3.2.7 on 2021-10-26 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Representanteempresa', '0001_initial'),
        ('Provincia', '0001_initial'),
        ('Tiposolicitud', '0001_initial'),
        ('Estado', '0001_initial'),
        ('Ciudad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('idsolicitud', models.AutoField(db_column='idSolicitud', primary_key=True, serialize=False)),
                ('profesion', models.CharField(blank=True, max_length=45, null=True)),
                ('aniosexperiencia', models.IntegerField(blank=True, db_column='aniosExperiencia', null=True)),
                ('rangoedad', models.CharField(blank=True, db_column='rangoEdad', max_length=45, null=True)),
                ('experticia', models.CharField(blank=True, max_length=45, null=True)),
                ('sueldo', models.FloatField(blank=True, null=True)),
                ('fechainicio', models.DateTimeField(blank=True, db_column='fechaInicio', null=True)),
                ('fechacierre', models.DateTimeField(blank=True, db_column='fechaCierre', null=True)),
                ('cargo', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcioncargo', models.CharField(blank=True, db_column='descripcionCargo', max_length=200, null=True)),
                ('ciudad_idciudad', models.ForeignKey(db_column='ciudad_idCiudad', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Ciudad.ciudad')),
                ('estado_idestado', models.ForeignKey(db_column='Estado_idEstado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Estado.estado')),
                ('provincia_idprovincia', models.ForeignKey(db_column='provincia_idProvincia', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Provincia.provincia')),
                ('representante_idrepresentante', models.ForeignKey(db_column='representante_idrepresentante', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Representanteempresa.representanteempresa')),
                ('tiposolicitud_idtiposolicitud', models.ForeignKey(db_column='TipoSolicitud_idTipoSolicitud', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Tiposolicitud.tiposolicitud')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicituds',
                'db_table': 'solicitud',
            },
        ),
    ]
