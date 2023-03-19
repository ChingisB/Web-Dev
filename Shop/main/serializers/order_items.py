from rest_framework import serializers
from .order_details import OrderDetailsSerialzer
from .product import ProductSerializer
from main.models import OrderItems


class OrderItemsSerializer(serializers.ModelSerializer):
    order = OrderDetailsSerialzer(many=True)
    product = ProductSerializer(many=True)

    class Meta:
        model = OrderItems
        fields = "__all__"
