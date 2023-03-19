from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from main.permissions import AdminPermission
from main.serializers import UserSerializer


User = get_user_model()


@authentication_classes([TokenAuthentication])
@method_decorator(permission_required([IsAuthenticated, AdminPermission]), name="get")
@method_decorator(permission_required([IsAuthenticated, AdminPermission]), name="post")
@method_decorator(permission_required([IsAuthenticated, AdminPermission]), name="delete")
class StaffView(APIView):
    def get(self, request):
        data = User.objects.filter(is_staff=True).all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(request.data)
        if serializer.is_valid():
            serializer.save(is_staff=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, staff_id):
        staff = get_object_or_404(User, id=staff_id, is_staff=True)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)