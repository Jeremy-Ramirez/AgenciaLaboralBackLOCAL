# Generated by Django 3.2.7 on 2021-10-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitud', '0007_auto_20211029_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fechacierre',
            field=models.DateField(blank=True, db_column='fechaCierre', null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fechainicio',
            field=models.DateField(blank=True, db_column='fechaInicio', null=True),
        ),
    ]
