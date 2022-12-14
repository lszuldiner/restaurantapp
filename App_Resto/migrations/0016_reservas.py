# Generated by Django 4.0.6 on 2022-08-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Resto', '0015_alter_productos_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('numero_personas', models.IntegerField()),
                ('dia', models.DateField()),
                ('horario', models.TimeField()),
            ],
        ),
    ]
