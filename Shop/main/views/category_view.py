import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import authentication_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from main.models import Category
from main.serializers import CategorySerializer
from main.permissions import StaffPermission


@authentication_classes([TokenAuthentication])
@method_decorator(permission_required([StaffPermission, IsAuthenticated]), name='post')
@method_decorator(permission_required([StaffPermission, IsAuthenticated]), name='put')
@method_decorator(permission_required([StaffPermission, IsAuthenticated]), name='delete')

class CategoryView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                category = Category.objects.get(id=id)
            except Category.DoesNotExist:
                return Response({"error": "No category with such ID"}, status=404)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        category = Category.objects.filter(id=id).first()
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category.name = serializer['name']
            category.description = serializer['description']
            category.modified_at = datetime.datetime.now()
            category.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            category = Category.objects.filter(id=id).first()
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
