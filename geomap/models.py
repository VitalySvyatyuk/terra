from django.contrib.gis.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)
    okato_code = models.CharField(max_length=12)
    area = models.FloatField()
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name


class Rent(models.Model):
    type = models.CharField(max_length=81)
    num = models.IntegerField()
    mpoint = models.MultiPointField()

    def __str__(self):
        return self.type
