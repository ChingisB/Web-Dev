from rest_framework import serializers
from main.models import Product, ProductImage
from .inventory import InventorySerializer
from .discount import DiscountSerializer
from .product_image import ProductImageSerializer
from .rating import RatingSerializer
from .category import CategorySerializer
from .vendor import VendorSerializer
from .product_image import ProductImageSerializer
from .comment import CommentSerializer


class ProductSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer()
    discount = DiscountSerializer()
    image = serializers.SerializerMethodField()
    category = CategorySerializer()
    vendor = VendorSerializer()
    rating = RatingSerializer()

    class Meta:
        model = Product
        fields = "__all__"
    
    def get_image(self, obj):
        image = ProductImage.objects.filter(product=obj).first()
        image_serializer = ProductImageSerializer(instance=image)
        return image_serializer.data


class ProductDetailsSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer()
    discount = DiscountSerializer()
    category = CategorySerializer()
    vendor = VendorSerializer()
    rating = RatingSerializer()
    images = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"

    def get_images(self, obj):
        images_queryset = ProductImage.objects.filter(product=obj)
        images_serializer = ProductImageSerializer(instance=images_queryset, many=True)
        return images_serializer.data
