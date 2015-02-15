from django.db import models

# Create your models here.
class Collaborator(models.Model):
	name = models.CharField(max_length = 128)
	association = models.CharField(max_length = 128)
	list_order = models.PositiveIntegerField()	# Larger number in list_order indicates higher on the list

class Funding(models.Model):
	name = models.CharField(max_length = 128)
	url = models.URLField(null=True, blank=True)
	image = models.ImageField("Institute Profile Image", upload_to="images/resources/funding/", null=True, blank=True)
	list_order = models.PositiveIntegerField()	# Larger number in list_order indicates higher on the list

