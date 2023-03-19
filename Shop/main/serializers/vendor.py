from rest_framework import serializers
from main.models import Vendor


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'description')
