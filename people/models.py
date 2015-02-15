from django.db import models

TITLE_CHOICES = (
	('GS', 'Graduate Student'),
	('PF', 'Postdoctoral Fellow'),
	('US', 'Undergraduate'),
	('VS', 'Visiting Scholar'),
	('RS', 'Research Scientist'),
	('LM', 'Laboratory Manager'),
	('LA', 'Laboratory Assistant'),
	('T', 'Technician'),
	('SS', 'Summer Student'),
)

TITLE_CHOICES_FORMER = (
	('GS', 'Graduate Student'),
	('PF', 'Postdoctoral Fellow'),
	('US', 'Undergraduate'),
	('VS', 'Visiting Scholar'),
	('RA', 'Research Assistant'),
)

TITLE_CHOICES_PERSONAL = (
	('Dr.', 'Dr.'),
	('Prof.', 'Prof.'),
)

class CurrentMember(models.Model):
	first_name = models.CharField(max_length = 32)
	middle_name = models.CharField(max_length = 32, null=True, blank=True)
	last_name = models.CharField(max_length = 32)
	img_height = models.PositiveIntegerField(default=100)
	img_width = models.PositiveIntegerField(default=80)
	picture = models.ImageField("Headshot", upload_to="images/headshots/", height_field='img_height', width_field='img_width', blank=True, null=True)
	work_title = models.CharField(max_length = 8, blank=True, choices=TITLE_CHOICES)
	personal_title = models.CharField(max_length = 8, null=True, blank=True, choices=TITLE_CHOICES_PERSONAL)
	work_number = models.CharField(max_length = 16, default='617-496-8654')
	email = models.EmailField(max_length = 32, null=True, blank=True)

	cell_number = models.CharField(max_length = 16, blank=True)
	home_number = models.CharField(max_length = 16, blank=True)
	address = models.CharField(max_length = 256, blank=True)

	# On Python 3: def __str__(self):
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

	def _get_full_name(self):
		if self.middle_name:
			return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)
		else:
			return '%s %s' % (self.first_name, self.last_name)
	full_name = property(_get_full_name)


class FormerMember(models.Model):
	first_name = models.CharField(max_length = 32)
	middle_name = models.CharField(max_length = 32, null=True, blank=True)
	last_name = models.CharField(max_length = 32)
	lab_period = models.CharField(max_length = 32)
	current_association = models.CharField(max_length = 256, null=True, blank=True)
	current_website = models.URLField(null=True, blank=True)
	work_title = models.CharField(max_length = 8, choices=TITLE_CHOICES_FORMER)
	personal_title = models.CharField(max_length = 8, null=True, blank=True, choices=TITLE_CHOICES_PERSONAL)

	# On Python 3: def __str__(self):
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
