from django.db import models
from actors.models import Actor

# Create your models here.

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

class Movie(models.Model):
    id = models.BigIntegerField(primary_key=True)
    adult = models.BooleanField()
    title = models.CharField(max_length=30)
    original_title = models.CharField(max_length=30, null=True)
    overview = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    tagline = models.TextField() # 영화 소개
    runtime = models.IntegerField()
    release_date = models.DateField()
    backdrop_path = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    status = models.CharField(max_length=20)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name='movies')