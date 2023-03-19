from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserInfoBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        return user
