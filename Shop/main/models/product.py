from django.db import models
from main.models.inventory import Inventory
from main.models.discount import Discount
from main.models.category import Category
from main.models.vendor import Vendor


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        app_label = 'main'
