# Generated by Django 3.2.7 on 2021-10-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idrol', models.IntegerField(db_column='idRol', primary_key=True, serialize=False)),
                ('nombrerol', models.CharField(blank=True, db_column='nombreRol', max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'rol',
            },
        ),
    ]
