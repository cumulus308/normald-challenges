from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/tweets", views.tweet_list, name="tweet_list"),
    path(
        "api/v1/users/<int:user_id>/tweets",
        views.user_tweet_list,
        name="user_tweet_list",
    ),
]
