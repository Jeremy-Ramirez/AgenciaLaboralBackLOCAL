# Generated by Django 3.2.7 on 2021-10-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ramaactividad',
            fields=[
                ('idramaactividad', models.AutoField(db_column='idramaActividad', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=45, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Ramaactividad',
                'verbose_name_plural': 'Ramaactividads',
                'db_table': 'ramaactividad',
            },
        ),
    ]
