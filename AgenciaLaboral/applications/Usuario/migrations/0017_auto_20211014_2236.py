# Generated by Django 3.2.7 on 2021-10-15 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0016_auto_20211014_2222'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='password',
            new_name='contrasenia',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]
