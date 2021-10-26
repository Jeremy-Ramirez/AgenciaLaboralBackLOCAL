# Generated by Django 3.2.7 on 2021-10-01 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tipoempresa', '0002_auto_20210927_1817'),
        ('Actividadeconomica', '0003_alter_actividadeconomica_descripcion'),
        ('Tipopersona', '0003_alter_tipopersona_descripcion'),
        ('Ramaactividad', '0003_alter_ramaactividad_descripcion'),
        ('Sector', '0003_alter_sector_descripcion'),
        ('Tipodocumento', '0002_auto_20210927_1817'),
        ('Empresa', '0004_auto_20210928_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='actividadeconomica_idactividadeconomica',
            field=models.ForeignKey(db_column='actividadEconomica_idactividadEconomica', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Actividadeconomica.actividadeconomica'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ramaactividad_idramaactividad',
            field=models.ForeignKey(db_column='ramaActividad_idramaActividad', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Ramaactividad.ramaactividad'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='sector_idsector',
            field=models.ForeignKey(db_column='sector_idSector', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Sector.sector'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='tipodocumento_idtipodocumento',
            field=models.ForeignKey(db_column='tipoDocumento_idtipoDocumento', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Tipodocumento.tipodocumento'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='tipoempresa_idtipoempresa',
            field=models.ForeignKey(db_column='tipoEmpresa_idtipoEmpresa', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Tipoempresa.tipoempresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='tipopersona_idtipopersona',
            field=models.ForeignKey(db_column='tipoPersona_idtipoPersona', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Tipopersona.tipopersona'),
        ),
    ]
