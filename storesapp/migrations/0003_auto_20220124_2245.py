# Generated by Django 3.2.9 on 2022-01-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storesapp', '0002_store_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='city',
            field=models.CharField(default='Город', max_length=80, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(default='Адрес', max_length=255, verbose_name='Адрес'),
        ),
    ]
