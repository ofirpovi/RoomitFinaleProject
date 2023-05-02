# Generated by Django 4.2 on 2023-04-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomit_app', '0007_alter_requirementsp_requirement_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementsp',
            name='Country',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MaxRent',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MaxRoommates',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MaxRooms',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MinRent',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MinRoommates',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MinRooms',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MinShowers',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MinToilets',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='Neighborhood',
            field=models.CharField(default='', max_length=25),
        ),
    ]