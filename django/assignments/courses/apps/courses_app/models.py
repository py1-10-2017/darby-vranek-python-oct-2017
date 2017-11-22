from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return '%s: %s' % (self.name, self.description)
