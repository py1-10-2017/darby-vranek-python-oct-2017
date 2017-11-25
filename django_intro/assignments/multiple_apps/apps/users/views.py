from django.shortcuts import render, HttpResponse

def register(request):
	return HttpResponse('placeholder to create a new user record')


def login(request):
	return HttpResponse('placeholder for users to log in')


def show(request):
	return HttpResponse('placeholder to display all users')
