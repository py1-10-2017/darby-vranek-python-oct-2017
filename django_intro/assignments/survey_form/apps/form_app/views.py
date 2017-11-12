from django.shortcuts import render, redirect
from django.utils.encoding import smart_text

def index(request):
	return render(request, 'form_app/index.html')


def process(request):
	if 'submit_count' in request.session:
		request.session['submit_count'] += 1
	else:
		request.session['submit_count'] = 1
	print type(request.POST['name'])
	print type(request.POST['comment'])
	request.session['submit_count'] = request.session['submit_count']
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return redirect('/result')


def show_result(request, context=None):
	return render(request, 'form_app/result.html', context)
