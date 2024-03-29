# Generated by Django 5.0.3 on 2024-03-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('consulting_date', models.DateField()),
                ('doctor_name', models.CharField(max_length=100)),
                ('diagnosis', models.TextField()),
                ('prescription', models.TextField()),
            ],
        ),
    ]
