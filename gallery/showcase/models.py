from django.db import models
from django.utils import timezone

import datetime


class Gallery(models.Model):
    """
    Contains art pieces
    """
    name = models.CharField(max_length=200, default='')
    artist = models.CharField(max_length=100, default='')
    pub_date = models.DateField('date published', default=timezone.now)
    description = models.TextField(max_length=1000, default='')
    rating = models.IntegerField(default=0.0)

    def __str__(self):
        return self.name


class ArtPiece(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published', default=timezone.now)
    image = models.ImageField()
    artist = models.CharField(max_length=100)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
