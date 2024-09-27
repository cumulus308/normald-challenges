from django.urls import path
from .views import TweetList, UserTweetList

urlpatterns = [
    path("api/v1/tweets", TweetList.as_view(), name="api_tweet_list"),
    path(
        "api/v1/users/<int:user_id>/tweets",
        UserTweetList.as_view(),
        name="api_user_tweets",
    ),
]
