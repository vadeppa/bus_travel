# Generated by Django 4.1.3 on 2022-11-25 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_about_bus_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('bus_name', models.CharField(max_length=200)),
                ('vehicle_num', models.CharField(max_length=200)),
                ('driver_no', models.CharField(max_length=200)),
                ('start_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0)),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('destination_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.destination')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('sex', models.CharField(choices=[('male', 'male'), ('Female', 'Female'), ('other', 'other')], max_length=200)),
                ('aadhar_no', models.IntegerField(default=True, null=True)),
                ('bus_name', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.busdetails')),
            ],
        ),
        migrations.AddField(
            model_name='busdetails',
            name='destination_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.destination'),
        ),
    ]