from django.db import models
from django.utils import timezone
from datetime import timedelta


class Product(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название товара")
    category = models.CharField(max_length=255, verbose_name="Категория")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Статус активности")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    @property
    def orders_last_month(self):
        """
        Возвращает количество заказов за прошлый месяц.
        """
        now = timezone.now()
        first_day_last_month = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
        last_day_last_month = now.replace(day=1) - timedelta(days=1)
        return self.orders.filter(created_at__gte=first_day_last_month, created_at__lte=last_day_last_month).count()

    @property
    def orders_this_month(self):
        """
        Возвращает количество заказов за текущий месяц с 1-го числа.
        """
        now = timezone.now()
        first_day_this_month = now.replace(day=1)
        return self.orders.filter(created_at__gte=first_day_this_month).count()

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order for {self.product.title} on {self.created_at}"
