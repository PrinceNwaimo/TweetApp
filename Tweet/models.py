from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    tweet = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This is our toString in java
        return f"{self.tweet}{self.time_stamp}"

    def get_absolute_url(self):
        # A way of getting the address for our post
        return reverse('tweet-details', args=[str(self.pk)])

