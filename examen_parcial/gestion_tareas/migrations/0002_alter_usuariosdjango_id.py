# Generated by Django 4.1.3 on 2022-11-28 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariosdjango',
            name='id',
            field=models.IntegerField(default='', primary_key='true', serialize=False),
        ),
    ]