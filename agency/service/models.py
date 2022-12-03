from django.db import models
from .utils import *
import datetime


class Complex(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(blank=True, verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание')
    lat = models.FloatField(blank=True, null=True, verbose_name='Широта')
    lon = models.FloatField(blank=True, null=True, verbose_name='Долгота')
    img = models.ImageField(upload_to='complex/', verbose_name='Превью')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Жилой комплекс'
        verbose_name_plural = 'Жилые комплексы'


class ComplexGallery(models.Model):
    complex = models.ForeignKey(Complex, on_delete=models.CASCADE, blank=True, verbose_name='Название ЖК')
    gal_img = models.ImageField(upload_to='complex/gallery/', blank=True, verbose_name='Фотография')

    def __str__(self):
        return '%s' % self.complex.name

    class Meta:
        verbose_name = 'Фотография ЖК'
        verbose_name_plural = 'Фотографии ЖК'


class House(models.Model):
    complex = models.ForeignKey(Complex, on_delete=models.CASCADE, blank=True, verbose_name='Комплекс')
    house_number = models.IntegerField(verbose_name='Номер дома')
    num_complex = models.IntegerField(verbose_name='Номер дома по счёту в этом комплексе', blank=True, null=True)

    def __str__(self):
        return '%s дом №%s' % (self.complex.name, self.house_number)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'


class Apartment(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, blank=True, verbose_name='Дом')
    apartment_number = models.IntegerField(verbose_name='Номер')
    level = models.IntegerField(verbose_name='Этаж')
    room = models.IntegerField(verbose_name='Кол-во комнат')
    square = models.FloatField(verbose_name='Площадь')
    finishing = models.BooleanField(default=False, verbose_name='Отделка')
    price_m = models.DecimalField(max_digits=7, decimal_places=1, verbose_name='Цена за м2')
    price_total = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='Цена за объект')
    plan_img = models.ImageField(upload_to='complex/apartment/', verbose_name='Планировка')
    num_house = models.IntegerField(verbose_name='Номер квартиры по счёту в этом комплексе', blank=True, null=True)

    def __str__(self):
        return '%s' % self.apartment_number

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class SaleOrder(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    message = models.TextField(verbose_name='Сообщение пользователя')
    date = models.DateTimeField(blank=True, null=True, verbose_name='Дата')

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заявка на продажу квартиры'
        verbose_name_plural = 'Заявки на продажу квартир'
