from rest_framework import serializers
from main.models import ShoppingSession
from .user import UserSerializer
from .cart_item import CartItemSerializer


class ShoppingSessionSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    cart = CartItemSerializer(many=True)

    class Meta:
        model = ShoppingSession
        fields = "__all__"
