from django.db import models


class PaymentDetails(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    provider = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        app_label = 'main'
