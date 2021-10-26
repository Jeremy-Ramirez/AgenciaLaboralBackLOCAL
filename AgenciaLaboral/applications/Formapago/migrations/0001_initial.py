# Generated by Django 3.2.6 on 2021-08-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formapago',
            fields=[
                ('idformapago', models.IntegerField(db_column='idFormaPago', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'formapago',
            },
        ),
    ]