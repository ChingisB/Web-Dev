from rest_framework import serializers
from main.models import UserInfo
from .user import UserSerializer


class UserInfoSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserInfo
        fields = "__all__"
