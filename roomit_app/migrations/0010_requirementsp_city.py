# Generated by Django 4.2 on 2023-04-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomit_app', '0009_rename_roommates_id_requirementsp_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementsp',
            name='City',
            field=models.CharField(default='', max_length=25),
        ),
    ]