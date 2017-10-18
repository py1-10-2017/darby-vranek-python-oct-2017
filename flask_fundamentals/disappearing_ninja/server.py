from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/ninja/<color>')
def display_ninja(color):
	if color == 'blue':
		return render_template('ninja.html', img_src= url_for('static', filename='img/leonardo.jpg'))
	elif color == 'orange':
		return render_template('ninja.html', img_src= url_for('static', filename='img/michelangelo.jpg'))
	elif color == 'red':
		return render_template('ninja.html', img_src= url_for('static', filename='img/raphael.jpg'))
	elif color == 'purple':
		return render_template('ninja.html', img_src= url_for('static', filename='img/donatello.jpg'))
	else:
		return render_template('ninja.html', img_src= url_for('static', filename='img/notapril.jpg'))



app.run(debug=True)
