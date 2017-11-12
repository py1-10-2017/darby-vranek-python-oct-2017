from django.shortcuts import redirect, render
import time

def index(request):
	return render(request, 'words/index.html')


def add_word(request):
	if not 'records' in request.session:
		request.session['records'] = list()
	style_class = request.POST['radio_color']
	new_record = {
		'word': request.POST['new_word'],
		'style_class': style_class,
		'timestamp': time.strftime('%I:%M:%S%p, %B %d %Y', time.localtime())
	}
	print request.session['records']
	request.session['records'].append(new_record)
	print request.session['records']
	return redirect('/session_words')

def clear_session(request):
	request.session['records'] = list()
	return redirect('/session_words')
