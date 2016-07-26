from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime

class ArtistProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(default='art/placeholder.jpg')
    join_date = models.DateField('date joined', default=timezone.now)
    bio = models.TextField(max_length=250, default='')

    def __str__(self):
        return self.user.username


class Gallery(models.Model):
    """
    Contains art pieces
    """
    name = models.CharField(max_length=200, default='')
    artist = models.ForeignKey('ArtistProfile', on_delete=models.CASCADE)
    pub_date = models.DateField('date published', default=timezone.now)
    description = models.TextField(max_length=1000, default='')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ArtPiece(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published', default=timezone.now)
    image = models.ImageField()
    artist = models.ForeignKey('ArtistProfile', on_delete=models.CASCADE)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.title
