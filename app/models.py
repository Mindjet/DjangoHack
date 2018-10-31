from django.db import models


# Create your models here.

class Hero(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    position = models.CharField(max_length=30)
    health = models.IntegerField()
    armour = models.IntegerField()
    shield = models.IntegerField()
    real_name = models.CharField(max_length=20)
    age = models.IntegerField()
    height = models.IntegerField()
    affiliation = models.CharField(max_length=50)
    base_of_operation = models.CharField(max_length=50)
    avatar = models.URLField()
    bio = models.CharField(max_length=200)
