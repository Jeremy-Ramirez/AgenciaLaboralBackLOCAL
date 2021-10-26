# Generated by Django 3.2.6 on 2021-08-26 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarjetaEmpresa',
            fields=[
                ('idtarjeta_empresa', models.IntegerField(db_column='idTarjeta-Empresa', primary_key=True, serialize=False)),
                ('numerotarjeta', models.CharField(blank=True, db_column='numeroTarjeta', max_length=45, null=True)),
                ('tiptarjeta', models.CharField(blank=True, db_column='tipTarjeta', max_length=45, null=True)),
                ('empresa_idempresa', models.ForeignKey(db_column='Empresa_idEmpresa', on_delete=django.db.models.deletion.DO_NOTHING, to='Empresa.empresa')),
            ],
            options={
                'db_table': 'tarjeta-empresa',
            },
        ),
    ]