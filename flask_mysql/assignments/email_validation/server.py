from flask import Flask, flash, render_template, request, redirect
from mysqlconnection import MySQLConnector
import re


app = Flask(__name__)
app.secret_key = 'SECRETKEYHEREEEEEE'
mysql = MySQLConnector(app, 'email_validation')

@app.route('/', methods=["GET"])
def index():
	return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():
	if email_is_valid(request.form['email']):
		mysql.query_db("INSERT INTO users (email) VALUES ('%s')" % request.form['email'])
		return render_template('emails.html', new_email=request.form['email'], email_addresses=mysql.query_db("SELECT * FROM users"))
	else:
		flash('Email is not valid!')
		return redirect('/')


def email_is_valid(email):
	return re.match(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$', email)


app.run(debug=True)
