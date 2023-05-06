from django.contrib import admin

from core.models import *

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)