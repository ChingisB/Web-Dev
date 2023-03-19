from django.db import models


class Inventory(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        app_label = 'main'
