from django.db import models
from django.contrib.auth import get_user_model
from main.models.payment_details import PaymentDetails


User = get_user_model()


class OrderDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=8)
    payment = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        app_label = 'main'
