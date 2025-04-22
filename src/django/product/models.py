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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider = models.ForeignKey('provider.Provider', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'





