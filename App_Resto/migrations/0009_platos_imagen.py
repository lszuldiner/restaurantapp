# Generated by Django 4.0.6 on 2022-08-18 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Resto', '0008_rename_pasta_platos_delete_regularpizza_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='platos',
            name='imagen',
            field=models.ImageField(default='', upload_to='assets/img'),
        ),
    ]
