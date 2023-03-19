from django.db import models
from main.models.product import Product


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        app_label = 'main'
