from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	age = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return ('First name: %s\nLast name: %s\nEmail address: %s\nAge: %s\nCreated at: %s\nUpdated at: %s\n' % (self.first_name, self.last_name, self.email_address, self.age, self.created_at, self.updated_at))
