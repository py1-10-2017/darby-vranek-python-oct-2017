from flask import Flask, redirect, request, render_template, session
app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
	if 'count' in session:
		session['count'] += 1
	else:
		session['count'] = 1
	return render_template('index.html', count=session['count'])


app.run(debug=True)
