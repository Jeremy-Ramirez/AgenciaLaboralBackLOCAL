# Generated by Django 3.2.6 on 2021-09-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tipopersona', '0002_alter_tipopersona_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipopersona',
            name='descripcion',
            field=models.CharField(max_length=45, null=True, unique=True),
        ),
    ]
