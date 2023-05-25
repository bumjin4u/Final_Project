from django.db import models
from movies.models import Movie
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    movies = models.ManyToManyField(Movie, related_name='tags')