from django.db import models


class Tweet(models.Model):
    payload = models.CharField(max_length=180)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payload

    def like_count(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} likes {self.tweet}"
