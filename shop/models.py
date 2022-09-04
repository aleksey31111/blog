from django.db import models
from django.urls import reverse


class Shop(models.Model):
    thing = models.CharField(max_length=300, verbose_name="Название")
    slug = models.SlugField(max_length=300, db_index=True, verbose_name='URL')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    foto = models.ImageField(upload_to='photos/%Y', blank=True, verbose_name='Фото')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    time = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_available = models.BooleanField(default=False, verbose_name="Есть в наличие")
    col = models.IntegerField(verbose_name="Количество")

    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.thing

    def get_absolut_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Товар магазина"
        verbose_name_plural = "Товары магазина"
        ordering = ['-time']


class Category(models.Model):
    name = models.CharField(max_length=300, db_index=True, verbose_name="Категоря")
    slug = models.SlugField(max_length=300, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SellThing(models.Model):
    name = models.CharField(max_length=300, verbose_name="Имя владельца продаваемого товара")
    thing = models.CharField(max_length=300, verbose_name="Название продаваемого товара")

    foto = models.ImageField(upload_to='photos_sell_thing/%Y', blank=True, verbose_name='Фото')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    passport = models.TextField(verbose_name="Паспортные данные")
    time = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    time_safe = models.DateField(verbose_name="Время появления у вас этой вещи")
    place = models.CharField(max_length=300, verbose_name="Место хранения этой вещи")
    defect_out = models.CharField(max_length=300, verbose_name="Повреждения внешние")
    defect_in = models.CharField(max_length=300, verbose_name="Работоспособность продаваемого устройства")
    is_available = models.BooleanField(default=False, verbose_name="Есть в наличие")
    numbers_thing = models.IntegerField(verbose_name="Количество устройств")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")


    def __str__(self):
        return self.thing

    class Meta:
        verbose_name = "Продажа вещи"
        verbose_name_plural = "Продажа вещей"

