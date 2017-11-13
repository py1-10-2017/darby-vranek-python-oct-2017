from django.shortcuts import redirect, render
import datetime

def index(request):
	return render(request, 'words/index.html')


def add_word(request):
	if not 'records' in request.session:
		request.session['records'] = list()
	style_class = request.POST['radio_color']
	if 'big_font' in request.POST:
		style_class = 'big_%s' % style_class
	new_record = {
		'word': request.POST['new_word'],
		'style_class': style_class,
		'timestamp': datetime.datetime.now().strftime('%I:%M:%S%p, %B %d %Y')
	}
	request.session['records'].insert(0, new_record)
	request.session.modified = True
	return redirect('/session_words')

def clear_session(request):
	request.session['records'] = list()
	return redirect('/session_words')
