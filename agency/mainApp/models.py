from django.db import models
import datetime
from .utils import *


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(blank=True, verbose_name='Слаг/Slug')
    description = models.TextField(max_length=215, verbose_name='Краткое описание')
    date = models.DateTimeField(blank=True, verbose_name='Дата')
    views = models.PositiveIntegerField(default=0, blank=True, verbose_name='Кол-во просмотров')
    time_to_read = models.IntegerField(blank=True, verbose_name='Время для прочтения')
    text = models.TextField(verbose_name='Текст статьи')
    img = models.ImageField(upload_to='article/', verbose_name='Фотография статьи', null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.title))
        if not self.date:
            self.date = datetime.datetime.now()
        self.time_to_read = reading_time(str(self.text))
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, verbose_name='Статья')
    name = models.CharField(max_length=50, verbose_name='Имя')
    comment = models.TextField(verbose_name='Текст комментария')
    date = models.DateTimeField(blank=True, verbose_name='Дата')

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.name

    def article_title(self):
        article_title = self.article.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Feedback(models.Model):
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
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'


class Review(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    message = models.TextField(verbose_name='Отзыв пользователя')
    date = models.DateTimeField(blank=True, null=True, verbose_name='Дата')

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
