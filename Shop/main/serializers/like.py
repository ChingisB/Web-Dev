from rest_framework import serializers
from main.models import Like
from .user import UserSerializer
from .product import ProductSerializer


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    product = ProductSerializer(many=True)

    class Meta:
        model = Like
        fields = "__all__"