from rest_framework import serializers
from main.models import UserPayment
from .user import UserSerializer


class UserPaymentSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=True)

    class Meta:
        model = UserPayment
        fields = "__all__"
