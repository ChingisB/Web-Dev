from rest_framework import serializers
from main.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('id', 'image')
