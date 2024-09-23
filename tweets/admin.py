from django.contrib import admin
from .models import Tweet, Like


class TweetAdmin(admin.ModelAdmin):
    like = Tweet.likes.count()
    list_display = ("payload", "user", "created_at", "updated_at", "like")
