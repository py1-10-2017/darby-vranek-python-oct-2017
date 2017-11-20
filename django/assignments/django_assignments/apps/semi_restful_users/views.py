from django.shortcuts import redirect, render
from .models import User


def index(request):
	return render(request, 'semi_restful_users/index.html', context={ 'users': User.objects.all() })


def new_user(request):
	return render(request, 'semi_restful_users/new_user.html')


def create_user(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	User.objects.create(first_name=first_name, last_name=last_name, email=email)
	return redirect('/users/%s/' % User.objects.last().id)


def edit_user(request, id):
	return render(request, 'semi_restful_users/edit_user.html', context={'user': User.objects.get(id=id)})


def show_user(request, id):
	return render(request, 'semi_restful_users/show_user.html', context={'user': User.objects.get(id=id)})


def destroy_user(request, id):
	User.objects.get(id=id).delete()
	return redirect('/users')


def update(request):
	user = User.objects.get(id=request.POST['id'])
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.email = request.POST['email']
	user.save()
	return redirect('/users/%s' % user.id)
