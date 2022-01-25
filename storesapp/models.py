from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255, unique=True)
    city = models.CharField(verbose_name='Город', max_length=80,default='Город')
    address = models.CharField(verbose_name='Адрес', max_length=255,default='Адрес')
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return self.name
