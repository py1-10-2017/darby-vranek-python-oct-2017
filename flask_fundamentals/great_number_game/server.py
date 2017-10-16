from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'secretWord'
@app.route('/')
def index():
	if not 'number' in session:
		session['number'] = random.randrange(1, 101)
	return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
	session['guess'] = int(request.form['guess'])
	if session['guess'] > session['number']:
		session['guess_message'] = 'Too high!'
		session['background_color'] = 'red'
	elif session['guess'] < session['number']:
		session['guess_message'] = 'Too low!'
		session['background_color'] = 'red'
	else:
		session['guess_message'] = str(session['number']) + ' was the number!'
		session['background_color'] = 'green'
	return redirect('/')

@app.route('/reset', methods=['GET'])
def reset():
	session['number'] = random.randrange(1, 101)
	session.pop('guess')
	return render_template('index.html')

app.run(debug=True)
