# Generated by Django 3.2.9 on 2022-01-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
