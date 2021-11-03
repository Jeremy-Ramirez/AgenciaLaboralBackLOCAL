# Generated by Django 3.2.6 on 2021-11-03 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aspirante', '0002_alter_aspirante_profesiones_idprofesiones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspirante',
            name='campolaboral',
            field=models.CharField(blank=True, db_column='campoLaboral', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='aspirante',
            name='experiencialaboral',
            field=models.CharField(blank=True, db_column='experienciaLaboral', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='aspirante',
            name='experticia',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='aspirante',
            name='posibilidadviajar',
            field=models.CharField(blank=True, db_column='posibilidadViajar', max_length=5, null=True),
        ),
    ]
