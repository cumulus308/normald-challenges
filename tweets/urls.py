from django.urls import path
from .views import tweet_list


urlpatterns = [
    path("", tweet_list, name="tweet_list"),
]
