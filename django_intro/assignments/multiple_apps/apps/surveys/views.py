from django.shortcuts import HttpResponse, redirect


def index(request):
	return HttpResponse('placeholder to display all the surveys created')


def new(request):
	return HttpResponse('placeholder for users to add a new server')
