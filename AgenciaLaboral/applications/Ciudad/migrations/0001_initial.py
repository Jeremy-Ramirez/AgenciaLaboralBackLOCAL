# Generated by Django 3.2.6 on 2021-08-26 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Provincia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('idciudad', models.IntegerField(db_column='idCiudad', primary_key=True, serialize=False)),
                ('nombreciudad', models.CharField(blank=True, db_column='nombreCiudad', max_length=45, null=True)),
                ('provincia_idprovincia', models.ForeignKey(db_column='Provincia_idProvincia', on_delete=django.db.models.deletion.DO_NOTHING, to='Provincia.provincia')),
            ],
            options={
                'db_table': 'ciudad',
            },
        ),
    ]
