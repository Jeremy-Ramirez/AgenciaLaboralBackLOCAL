# Generated by Django 3.2.6 on 2021-09-28 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Provincia', '0002_alter_provincia_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincia',
            name='nombreprovincia',
            field=models.CharField(db_column='nombreProvincia', max_length=45, null=True, unique=True),
        ),
    ]