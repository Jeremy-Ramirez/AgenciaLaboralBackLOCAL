# Generated by Django 3.2.6 on 2021-09-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tipoempresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipoempresa',
            options={'verbose_name': 'Tipoempresa', 'verbose_name_plural': 'Tipoempresas'},
        ),
        migrations.AlterField(
            model_name='tipoempresa',
            name='descripcion',
            field=models.CharField(max_length=45, null=True, unique=True),
        ),
    ]