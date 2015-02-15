from django.db import models

NEWS_CATEGORY = (
	('NR', 'News Reports'),
	('GN', 'Group News'),
	('AR', 'Archives'),
)

class NewsItem(models.Model):
	content = models.TextField()
	year = models.IntegerField()
	month = models.IntegerField()
	category = models.CharField(max_length=8, null=True, blank=True, choices=NEWS_CATEGORY)

