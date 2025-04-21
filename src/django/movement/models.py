from django.db import models

# Create your models here.

class Movement(models.Model):
    type_movement = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_id = models.ForeignKey('product.Product',on_delete=models.CASCADE)

    class Meta:
        db_table = 'movement'