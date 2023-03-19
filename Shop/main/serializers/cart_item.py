from rest_framework import serializers
from main.models import CartItem
from .product import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=True)

    class Meta:
        model = CartItem
        fields = ('id', 'product')
