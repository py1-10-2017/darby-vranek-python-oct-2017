from django.shortcuts import render, redirect
from .models import *

def index(request):
	return render(request, 'courses_app/index.html', context={'courses': Course.objects.all()})


def add_course(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')

def destroy(request, id):
	return render(request, 'courses_app/delete_course.html', context={'course': Course.objects.get(id=id)})


def remove(request, id):
	Course.objects.get(id=id).delete()
	return redirect('/')
