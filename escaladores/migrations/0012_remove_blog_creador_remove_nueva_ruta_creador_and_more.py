# Generated by Django 4.2.6 on 2023-11-25 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escaladores', '0011_alter_blog_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='creador',
        ),
        migrations.RemoveField(
            model_name='nueva_ruta',
            name='creador',
        ),
        migrations.RemoveField(
            model_name='nuevo_bloque',
            name='creador',
        ),
        migrations.RemoveField(
            model_name='nuevo_escalador',
            name='creador',
        ),
    ]
