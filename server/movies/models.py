from django.db import models

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    
class Actor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    deathday = models.DateField(null=True)
    profile_path = models.TextField(null=True)

class Movie(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    overview = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    tagline = models.TextField() # 영화 소개
    runtime = models.IntegerField()
    release_date = models.DateField()
    backdrop_path = models.TextField()
    poster_path = models.TextField()
    status = models.CharField(max_length=20)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name='movies')