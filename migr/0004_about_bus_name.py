# Generated by Django 4.1.3 on 2022-11-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_about_travel_about_travels'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='bus_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
