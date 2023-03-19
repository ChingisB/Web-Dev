from rest_framework import serializers
from django.db.models import Avg
from main.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = ('rating')

    def get_rating(self, obj):
        return obj.product.rating_set.aggregate(Avg('rating'))['rating__avg']
