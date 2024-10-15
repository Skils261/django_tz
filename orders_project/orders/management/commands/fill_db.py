from django.core.management.base import BaseCommand
from orders.models import Product, Order
from random import randint
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Заполняет базу данных начальными данными'

    def handle(self, *args, **kwargs):
        # Создание начальных продуктов
        products = [
            {"title": "Телевизор", "category": "Электроника", "price": 500.00},
            {"title": "Пылесос", "category": "Техника для дома", "price": 150.00},
            {"title": "Микроволновка", "category": "Техника для дома", "price": 100.00},
            {"title": "Холодильник", "category": "Бытовая техника", "price": 800.00},
        ]

        for prod in products:
            product = Product.objects.create(
                title=prod['title'],
                category=prod['category'],
                status='active',
                price=prod['price']
            )
            # Генерация случайных заказов для каждого продукта
            for _ in range(randint(1, 5)):  # Случайное количество заказов
                Order.objects.create(
                    product=product,
                    quantity=randint(1, 3),  # Случайное количество товаров в заказе
                    created_at=timezone.now() - timedelta(days=randint(31, 60))  # Случайная дата в последние 2 месяца
                )

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены!'))
