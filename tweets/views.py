from django.shortcuts import render
from .models import Tweet, Like


def tweet_list(request):
    tweets = Tweet.objects.all()

    return render(request, "tweets/list.html", {"tweets": tweets})
