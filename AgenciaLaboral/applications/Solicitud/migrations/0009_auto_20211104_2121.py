# Generated by Django 3.2.7 on 2021-11-05 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profesiones', '0001_initial'),
        ('Solicitud', '0008_auto_20211029_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='profesion',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='profesiones_idprofesiones',
            field=models.ForeignKey(db_column='Profesiones_idProfesiones', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Profesiones.profesiones'),
        ),
    ]
