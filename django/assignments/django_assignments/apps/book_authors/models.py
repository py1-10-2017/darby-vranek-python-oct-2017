from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	notes = models.TextField(default='')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s %s: %s' % (self.first_name, self.last_name, self.email)

class Book(models.Model):
	authors = models.ManyToManyField(Author, related_name='books')
	name = models.CharField(max_length=255)
	desc = models.TextField(default='')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		string = '%s' % self.name
		authors = self.authors.all()
		if authors:
			string = '%s by %s %s' % (string, authors[0].first_name, authors[0].last_name)
			if len(authors) > 1:
				for i in range(1, len(authors)):
					string += ', %s %s' % (authors[i].first_name, authors[i].last_name)
		return string
