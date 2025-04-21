from django.db import models
from django.conf import settings


# Create your models here.
class Category(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

class Product(models.Model):
    name = models.CharField(max_length=30)
    stock = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider_id = models.IntegerField()
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'

class Price(models.Model):
    actual_price = models.IntegerField()
    new_price = models.IntegerField()
    previous_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'price'





