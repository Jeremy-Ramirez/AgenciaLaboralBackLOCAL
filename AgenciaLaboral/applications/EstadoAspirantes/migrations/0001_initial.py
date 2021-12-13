# Generated by Django 3.2.7 on 2021-12-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoAspirantes',
            fields=[
                ('idestadoaspirantes', models.AutoField(db_column='idEstadoAspirantes', primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, db_column='Estado', max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'EstadoAspirantes',
                'verbose_name_plural': 'EstadoAspirantes',
                'db_table': 'estadoaspirantes',
            },
        ),
    ]