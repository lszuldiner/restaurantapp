# Generated by Django 4.0.6 on 2022-09-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Resto', '0020_remove_reservas_user_is_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='tipo',
            field=models.CharField(default=None, max_length=30),
        ),
    ]