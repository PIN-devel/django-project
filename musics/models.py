from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    date = models.DateField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_musics')


class Artist(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_artists')


class Member(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    artist = models.ForeignKey("Artist", on_delete=models.SET_NULL, null=True)


class Comment(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    music = models.ForeignKey("Music", on_delete=models.CASCADE)