from django.db import models
from main.models.order_details import OrderDetails
from main.models.product import Product


class OrderItems(models.Model):
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        app_label = 'main'
