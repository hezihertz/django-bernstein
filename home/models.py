from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class Hit(models.Model):
	date = models.DateTimeField(auto_now=True)
	ip_addr = models.CharField(max_length = 32, blank=True, null=True)
	user_agent = models.CharField(max_length = 256, blank=True, null=True)
