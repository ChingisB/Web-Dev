from rest_framework import serializers
from main.models import PaymentDetails


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = "__all__"
