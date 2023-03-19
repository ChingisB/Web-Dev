from rest_framework import serializers
from main.models import OrderDetails
from .user import UserSerializer


class OrderDetailsSerialzer(serializers.ModelSerializer):
    user = UserSerializer(many=True)

    class Meta:
        model = OrderDetails
        fields = "__all__"
