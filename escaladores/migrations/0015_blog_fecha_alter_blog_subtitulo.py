# Generated by Django 4.2.6 on 2023-11-25 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escaladores', '0014_remove_blog_fech'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
