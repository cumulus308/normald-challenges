from rest_framework import serializers
from .models import Tweet, Like
from users.models import User
from rest_framework.serializers import ModelSerializer


class TweetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    payload = serializers.CharField(max_length=180)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.payload = validated_data.get("payload", instance.payload)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.save()
        return instance


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
