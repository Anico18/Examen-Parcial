# Generated by Django 4.1.3 on 2022-11-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuariosDjango',
            fields=[
                ('id', models.IntegerField(default='', max_length=64, primary_key='true', serialize=False)),
                ('nombre', models.CharField(default='', max_length=64)),
                ('apellido', models.CharField(default='', max_length=64)),
                ('tarea', models.CharField(default='', max_length=128)),
                ('fecha', models.DateField(default='', max_length=64)),
            ],
        ),
    ]
