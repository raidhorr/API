from django.db import models


class User(models.Model):
    email = models.TextField()
    phone = models.TextField()
    fam = models.TextField()
    name = models.TextField()
    otc = models.TextField()


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


