from flask import Flask, render_template, redirect, request, session, redirect
import random
import time
import math


app = Flask(__name__)
app.secret_key = "SecretKeyWhootWhoooooot!"


@app.route('/')
def index():
	if not 'gold' in session:
		session['gold'] = 0
		session['activity_log'] = list()
	return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
	location = request.form['location']
	if location == 'farm':
		process_location(location, 10, 20)
	elif location == 'cave':
		process_location(location, 5, 10)
	elif location == 'house':
		process_location(location, 2, 5)
	else:
		process_location(location, -50, 50)
	return redirect('/')


def process_location(location, min, max):
	reward = random.randrange(min, max+1)
	session['gold'] += reward
	if reward > 0:
		session['activity_log'].insert(0, ['positive', 'Earned {} gold from the {}! ({})'.format(reward, location, time.strftime('%Y/%m/%d - %I:%M %p', time.localtime()))])
	else:
		session['activity_log'].insert(0, ['negative', 'Entered a casino and lost {} gold... Ouch... ({})'.format(int(math.fabs(reward)), time.strftime('%Y/%m/%d - %I:%M %p', time.localtime()))])

app.run(debug=True)
