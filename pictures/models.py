from django.db import models

# Create your models here.
class GroupPhoto(models.Model):
	list_order = models.PositiveIntegerField()
	thumbnail = models.ImageField("Thumbnail", upload_to="images/groupphotos/thumbnails/")
	full_image = models.ImageField("Full Size Image", upload_to="images/groupphotos/full/")

class Poster(models.Model):
	list_order = models.PositiveIntegerField()
	year = models.PositiveIntegerField()
	thumbnail = models.ImageField("Thumbnail", upload_to="images/posters/thumbnails/")
	full_image = models.ImageField("Full Size Image", upload_to="images/posters/full/")

