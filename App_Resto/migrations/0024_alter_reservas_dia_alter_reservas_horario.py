# Generated by Django 4.0.6 on 2022-09-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Resto', '0023_productos_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='dia',
            field=models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('domingo', 'Domingo')], max_length=9),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='horario',
            field=models.CharField(choices=[('20:00', '8:00PM'), ('21:00', '9:00PM'), ('22:00', '10:00PM'), ('23:00', '11:00PM'), ('24:00', '12:00PM')], max_length=7),
        ),
    ]
