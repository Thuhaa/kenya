from django.contrib.gis.db import models


class Stations(models.Model):
	name = models.CharField(null=True, blank=True, max_length=20)
	station = models.CharField(null=True, blank=True, max_length=20)
	northings = models.FloatFileld()
	eastings = models.FloatField()
	geom = models.PointField()

	def __str__(self):
		return self.name
