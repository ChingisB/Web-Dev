import datetime
from rest_framework import serializers
from main.models import Inventory


class InventorySerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()
    deleted_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Inventory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.name)
        instance.modified_at = datetime.datetime.now()
        instance.save()
        return instance
