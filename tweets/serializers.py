from rest_framework import serializers
from .models import Tweet, Like
from users.models import User
from rest_framework.serializers import ModelSerializer


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["id", "payload", "user_id", "created_at"]


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
