# Generated by Django 4.2.6 on 2023-11-25 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escaladores', '0012_remove_blog_creador_remove_nueva_ruta_creador_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='fecha',
            new_name='fech',
        ),
    ]
