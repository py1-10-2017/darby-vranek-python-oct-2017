from django.shortcuts import redirect, render
import random
import datetime

# Create your views here.

def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 0
	if not 'activity_log' in request.session:
		request.session['activity_log'] = list()
	return render(request, 'ninja_gold/index.html')


def process_money(request):
	location = request.POST['location']
	if location == 'farm':
		min = 10
		max = 20
	elif location == 'cave':
		min = 5
		max = 10
	elif location == 'house':
		min = 2
		max = 5
	else:
		min = -50
		max = 50
	gold_earned = random.randint(min, max + 1)
	request.session['gold'] += gold_earned
	if gold_earned > 0:
		color = 'green'
		desc = 'Earned %s from the %s!' % (gold_earned, location)
	else:
		color = 'red'
		desc = 'Entered a casino and lost %s gold... Ouch...' % gold_earned
	request.session['activity_log'].insert(0, { 'color': color, 'desc': desc, 'timestamp': datetime.datetime.now().strftime('%I:%M:%S%p, %B %d %Y') })
	request.session.modified = True
	return redirect('/')
