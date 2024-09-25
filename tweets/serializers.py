from rest_framework.serializers import ModelSerializer
from .models import Tweet, Like


class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
