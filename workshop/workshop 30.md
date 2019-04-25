from django.db import models


class Hashtag(models.Model):
    content = models.TextField()


class Post():
    title = models.TextField()
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, blank=True)