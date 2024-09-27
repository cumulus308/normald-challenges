from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tweet
from users.models import User
from .serializers import TweetSerializer


class TweetList(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


class UserTweetList(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("User does not exist")

        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
