# Generated by Django 3.2.9 on 2022-01-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование')),
                ('address', models.CharField(max_length=255, unique=True, verbose_name='Адрес')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('lat', models.FloatField(verbose_name='Широта')),
            ],
        ),
    ]