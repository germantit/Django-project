from django.db import models
from .utils import *
import datetime


class Flat(models.Model):
    street = models.CharField(max_length=250, blank=True, verbose_name='Улица')
    house_number = models.IntegerField(blank=True, null=True, verbose_name='Номер дома')
    flat_number = models.IntegerField(verbose_name='Номер квартиры')
    slug = models.SlugField(blank=True, verbose_name='Слаг')
    level = models.IntegerField(verbose_name='Этаж')
    room = models.IntegerField(verbose_name='Кол-во комнат')
    square = models.FloatField(verbose_name='Площадь')
    price = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='Цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='Номер телефона')
    prev_img = models.ImageField(upload_to='flats/', blank=True, verbose_name='Превью')

    def __str__(self):
        return '%s' % self.street

    def save(self, *args, **kwargs):
        if not self.slug:
            street = from_cyrillic_to_eng(str(self.street))
            self.slug = street + '_' + str(self.house_number) + '_' + str(self.flat_number)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class FlatGallery(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, blank=True, verbose_name='Квартира')
    gal_img = models.ImageField(upload_to='flats/gallery/', blank=True, verbose_name='Фотография')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class BuyOrder(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, blank=True, verbose_name='Квартира')
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    date = models.DateTimeField(blank=True, null=True, verbose_name='Дата')

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заявка на покупку квартиры'
        verbose_name_plural = 'Заявки на покупку квартир'

