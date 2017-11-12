from django.shortcuts import render
from django.utils.crypto import get_random_string

def index(request):
	if not 'count' in request.session:
		request.session['count'] = 1
	else:
		request.session['count'] += 1
	context = {
		'attempt_count': request.session['count'],
		'random_word': get_random_string(length=14).upper()
	}
	return render(request, 'random_word/index.html', context)
