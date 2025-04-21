from django.contrib import admin
from .models import Product,Category,Price
# Register your models here.

admin.site.register(Product)
admin.site.register(Price)
admin.site.register(Category)
