# Generated by Django 4.0.6 on 2022-07-30 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Resto', '0002_clientes_pedidos_platos_delete_consulta'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Platos',
            new_name='Productos',
        ),
    ]
