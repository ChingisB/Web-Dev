import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from main.models import Vendor
from main.serializers import VendorSerializer
from main.permissions import StaffPermission


@method_decorator(permission_required([StaffPermission, IsAuthenticated]), name='post')
@method_decorator(permission_required([StaffPermission, IsAuthenticated]), name='put')
@method_decorator(permission_required([StaffPermission, IsAuthenticated]), name='delete')
class VendorView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                vendor = Vendor.objects.get(id=id)
            except Vendor.DoesNotExist:
                return Response({"error": "No category with such ID"}, 
                                status=status.HTTP_404_NOT_FOUND)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        vendor = Vendor.objects.filter(id=id).first()
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            vendor.name = serializer['name']
            vendor.description = serializer['description']
            vendor.modified_at = datetime.datetime.now()
            vendor.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            category = Vendor.objects.filter(id=id).first()
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
