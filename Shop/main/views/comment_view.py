from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from main.models import Product, Comment
from main.serializers import CommentSerializer, CommentCreateSerializer


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_view(request, product_id, comment_id=None):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'GET':
        data = Comment.objects.filter(product=product)
        serializer = CommentSerializer(data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, product=product)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
