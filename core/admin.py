from django.contrib import admin

from core.models import Product, ProductCategory, Client, Order

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)