# Generated by Django 4.2 on 2023-04-18 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roomit_app', '0012_alter_requirementsp_city_alter_requirementsp_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequirementsR',
            fields=[
                ('Requirement_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Occupation', models.CharField(blank=True, choices=[('F', 'Full-time job'), ('S', 'Student'), ('P', 'Part-time job'), ('D', "Doesn't matter"), ('empty', '---')], max_length=30)),
                ('MinAge', models.IntegerField(blank=True, default=None, null=True)),
                ('MaxAge', models.IntegerField(blank=True, default=None, null=True)),
                ('Gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Not Defined')], max_length=10)),
                ('Smoker', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally'), ('Socially', 'Socially')], max_length=15)),
                ('Diet', models.CharField(blank=True, choices=[('Carnivore', 'Carnivore'), ('Pescetarian', 'Pescetarian'), ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Raw Veganism', 'Raw Veganism')], max_length=15)),
                ('Kosher', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=15)),
                ('Status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('In a relationship', 'In a relationship'), ('D', "Doesn't matter")], default='empty', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
