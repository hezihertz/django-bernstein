from django.db import models
from django.forms import ModelForm

BG_CHOICE = (
	('Education', 'Education'),
	('Appointments', 'Professional Appointments'),
	('Honors', 'Honors'),
	('Lectureships', 'Named Lectureships'),
	('Interests', 'Recent Research Interests'),
)

class Background(models.Model):
	year_start = models.IntegerField(null=True, blank=True)
	year_end = models.IntegerField(null=True, blank=True)
	title = models.CharField(max_length = 256)
	url = models.URLField(null=True, blank=True)
	category = models.CharField(max_length = 16, null=True, blank=True, choices=BG_CHOICE)


class BackgroundForm(ModelForm):
	class Meta:
		model = Background
		fields = ['year_start', 'year_end', 'title', 'url', 'category']

