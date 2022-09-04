from django.db import models

# Статус заявки
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name="Название статуса")

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


# Заказы
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    order_name = models.CharField(max_length=200, verbose_name="Имя")
    order_phone = models.CharField(max_length=50, verbose_name="Телефон")
    order_service_name = models.CharField(max_length=200, verbose_name="Название услуги")
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"