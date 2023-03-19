from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Product
from main.serializers import ProductSerializer

class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            try:
                product = Product.objects.get(id=id)
            except Product.DoesNotExist:
                return Response({"error": "No product with such ID"}, status=404)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = ProductSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, post):
        pass
