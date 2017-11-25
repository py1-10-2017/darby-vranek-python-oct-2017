from __future__ import unicode_literals
from django.db import models
from collections import namedtuple
import bcrypt
import re

error_message = namedtuple('ErrorMessage', 'field message')
re_email = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')



class UserManager(models.Manager):
	def validate(self, post):
		messages = list()
		if len(post['first_name']) < 2:
			messages.append(error_message('first_name', 'First name must be at least 2 characters long'))
		if not re.match(r'[A-Za-z\s-]+', post['first_name']):
			messages.append(error_message('first_name', 'First name contains invalid characters'))
		if len(post['last_name']) < 2:
			messages.append(error_message('last_name', 'Last name must be at least 2 characters long'))
		if not re.match(r'[A-Za-z\s-]+', post['last_name']):
			messages.append(error_message('last_name', 'Last name contains invalid characters'))
		if not post['email']:
			messages.append(error_message('email', 'Email is required'))
		elif not re_email.match(post['email']):
			messages.append(error_message('email', 'Email contains invalid characters'))
		elif len(User.objects.filter(email=post['email'])) != 0:
			messages.append(error_message('email', 'Email is already registered'))
		if len(post['password']) < 8:
			messages.append(error_message('password', 'Password must be at least 8 characters long'))
		elif post['password'] != post['confirm_password']:
			messages.append(error_message('password', 'Passwords do not match'))
		return messages


	def log_in(self, post):
		error_messages = list()
		if not User.objects.filter(email=post['email']):
			error_messages.append(error_message('login_email', 'Email has not been registered'))
		elif not bcrypt.checkpw(post['password'].encode(), User.objects.get(email=post['email']).password.encode()):
			error_message.append(error_message['login_password'], 'Incorrect password')
		return error_messages



class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	def __str__(self):
		return '%s %s - %s' % (self.first_name, self.last_name, self.email)
