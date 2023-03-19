from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        app_label = 'main'
