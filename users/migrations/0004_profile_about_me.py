# Generated by Django 4.1.7 on 2023-05-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_shelter_nerbay_propertyforoffer_shelter_nearby_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default=''),
        ),
    ]
