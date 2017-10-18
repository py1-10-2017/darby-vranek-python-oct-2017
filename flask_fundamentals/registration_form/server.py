from flask import Flask, flash, render_template, request, redirect
import re
app = Flask(__name__)
app.secret_key = "SecretKey"


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
	valid = True
	email = request.form['email']
	if len(email) == 0 or not re.match(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$', email):
		valid = False
		flash('Email must not be left blank and must be valid!')
	first_name = request.form['first_name']
	if len(first_name) == 0 or not re.match(r'^[a-zA-Z -]+$', first_name):
		valid = False
		flash('First name must not be blank and must contain only letters, spaces, and dashes!')
	last_name = request.form['last_name']
	if len(last_name) == 0 or not re.match(r'^[a-zA-Z -]+$', last_name):
		valid = False
		flash('Last name must not be blank and must contain only letters, spaces, and dashes!')
	if len(request.form['password']) == 0 or not request.form['password'] == request.form['confirm_password']:
		valid = False
		flash('Passwords must match and must not be left blank!')
	return redirect('/')

app.run(debug=True)
