from django.db import models

# Create your models here.
class Actor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    deathday = models.DateField(null=True)
    profile_path = models.TextField(null=True)