from django.db import models
from django.utils import timezone

import datetime


class Gallery(models.Model):
    """
    Contains art pieces
    """
    name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class ArtPiece(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    image = models.ImageField()
    artist = models.CharField(max_length=100)
    gallery = models.ForeignKey('Gallery', default=0)

    def __str__(self):
        return self.title
