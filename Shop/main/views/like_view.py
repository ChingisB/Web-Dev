from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from main.models import Product, Like


@api_view(['POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def like_view(request, product_id, like_id=None):
    if request.method == 'POST':
        user = request.user
        product = Product.objects.filter(id=product_id).first()
        Like.objects.create(user=user, product=product)
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        like = get_object_or_404(Like, id=like_id)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
