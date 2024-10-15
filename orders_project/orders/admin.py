from django.contrib import admin
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'status', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
