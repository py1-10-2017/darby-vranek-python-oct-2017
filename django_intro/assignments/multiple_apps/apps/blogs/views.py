from django.shortcuts import HttpResponse, redirect


def index(request):
	return HttpResponse('Placeholder to later display the list of blogs')


def new(request):
	return HttpResponse('Placeholder to display a new form to create a new blog')


def create(request):
	return redirect('/blogs')


def show(request, id):
	return HttpResponse('Placeholder to display blog %s' % id)


def edit(request,id):
	return HttpResponse('Placeholder to edit blog %s' % id)


def destroy(request, id):
	return redirect('/blogs')
