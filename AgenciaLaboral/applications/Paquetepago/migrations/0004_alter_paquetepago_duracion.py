# Generated by Django 3.2.7 on 2021-12-17 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paquetepago', '0003_auto_20211216_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquetepago',
            name='duracion',
            field=models.DurationField(blank=True, null=True),
        ),
    ]