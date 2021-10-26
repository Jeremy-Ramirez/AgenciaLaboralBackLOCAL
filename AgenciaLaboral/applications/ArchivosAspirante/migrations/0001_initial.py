# Generated by Django 3.2.7 on 2021-10-06 00:52

import applications.ArchivosAspirante.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Aspirante', '0006_alter_aspirante_videopresentacion'),
        ('Usuario', '0004_auto_20211003_1659'),
        ('CategoriaDocumento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='archivosAspirantes',
            fields=[
                ('idarchivosaspirante', models.AutoField(db_column='idArchivosAspirante', primary_key=True, serialize=False)),
                ('nombredocumento', models.CharField(blank=True, db_column='nombreDocumento', max_length=45, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to=applications.ArchivosAspirante.models.nameFile)),
                ('fechacreacion', models.DateField(blank=True, db_column='fechaCreacion', null=True)),
                ('aspirante_idaspirante', models.ForeignKey(db_column='aspirante_idaspirante', on_delete=django.db.models.deletion.DO_NOTHING, to='Aspirante.aspirante')),
                ('categoriaDocumento_idcategoriadocumento', models.ForeignKey(db_column='CategoriaDocumento_idCategoriaDocumento', on_delete=django.db.models.deletion.DO_NOTHING, to='CategoriaDocumento.categoriadocumento')),
                ('usuario_idusuario', models.ForeignKey(db_column='usuario_idusuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Usuario.usuario')),
            ],
            options={
                'db_table': 'archivosaspirante',
            },
        ),
    ]