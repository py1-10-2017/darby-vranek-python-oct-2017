from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User
import bcrypt


def log_errors(request, errors):
	for message in errors:
		messages.add_message(request, messages.ERROR, message.message, extra_tags=message.field)


def index(request):
	return render(request, 'login_register/index.html')


def register(request):
	post = request.POST
	error_messages = User.objects.validate(post)
	if error_messages:
		log_errors(request, error_messages)
		return redirect('/')
	else:
		User.objects.create(
			first_name=post['first_name'],
			last_name=post['last_name'],
			email=post['email'],
			password=bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())
		)
		request.session['logged_in'] = User.objects.last().id
		return redirect('/success/')


def success(request):
	return render(request, 'login_register/success.html', context={'name': User.objects.get(id=request.session['logged_in']).first_name})


def log_in(request):
	error_messages = User.objects.log_in(request.POST)
	if error_messages:
		log_errors(request, error_messages)
		return redirect('/')
	else:
		request.session['logged_in'] = User.objects.get(email=request.POST['email']).id
		return redirect('/success')
