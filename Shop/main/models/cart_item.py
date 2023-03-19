from django.db import models
from main.models.shopping_session import ShoppingSession
from main.models.product import Product


class CartItem(models.Model):
    shopping_session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        app_label = 'main'
