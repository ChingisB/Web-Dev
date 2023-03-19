from django.db import models
from main.models.product import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'main'
