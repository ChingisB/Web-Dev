from django.db import models
from django.contrib.auth import get_user_model
from main.models.product import Product


User = get_user_model()


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        app_label = 'main'
