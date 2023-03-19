from rest_framework import serializers
from main.models import Comment
from .user import UserInfoBriefSerializer


class CommentSerializer(serializers.ModelSerializer):

    user = UserInfoBriefSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'text')

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text')
