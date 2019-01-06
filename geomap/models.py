from django.contrib.gis.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)
    okato_code = models.CharField(max_length=12)
    area = models.FloatField()
    mpoly = models.MultiPolygonField()

    @property
    def point_nums(self):
        point_nums = {}
        for rent in self.get_rents():
            if rent.type in point_nums:
                point_nums[rent.type] += 1
            else:
                point_nums[rent.type] = 1
        return point_nums

    @property
    def points(self):
        points = {}
        for rent in self.get_rents():
            if rent.type in points:
                points[rent.type] += rent.num
            else:
                points[rent.type] = rent.num
        return points

    def get_rents(self):
        return Rent.objects.filter(mpoint__intersects=self.mpoly)

    def __str__(self):
        return self.name


class Rent(models.Model):
    type = models.CharField(max_length=81)
    num = models.IntegerField()
    mpoint = models.MultiPointField()

    def __str__(self):
        return self.type
