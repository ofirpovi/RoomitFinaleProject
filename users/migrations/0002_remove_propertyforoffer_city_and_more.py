# Generated by Django 4.1.7 on 2023-06-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyforoffer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='propertyforoffer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='propertyforoffer',
            name='neighborhood',
        ),
        migrations.AddField(
            model_name='propertyforoffer',
            name='Location',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hospitality',
            field=models.CharField(blank=True, choices=[('L', 'Love'), ('N', 'Prefer not')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, choices=[('F', 'Full-time job'), ('S', 'Student'), ('P', 'Part-time job'), ('D', "Doesn't matter")], max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('In a relationship', 'In a relationship'), ('D', "Doesn't matter")], max_length=20),
        ),
    ]
