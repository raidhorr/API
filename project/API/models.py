from django.contrib.postgres.fields import ArrayField
from django.db import models
from json import loads, dumps


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


class PerevalImages(models.Model):
    date_added = models.TimeField()
    title = models.TextField()
    data = models.BinaryField()


class PerevalAdded(models.Model):
    add_time = models.TimeField()
    beautyTitle = models.TextField()
    title = models.TextField()
    other_titles = models.TextField()
    connect = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    coords_id = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level_winter = models.TextField()
    level_summer = models.TextField()
    level_autumn = models.TextField()
    level_spring = models.TextField()
    images = ArrayField(models.IntegerField())

    def submitData(self, data):
        try:
            python_data = loads(data)
        except ValueError as ex:
            result_data = {
                "status": 500,
                "message": "Ошибка JSON",
                "id": None
            }
            return dumps(result_data)
