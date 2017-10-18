from flask import Flask, flash, render_template, request, redirect
app = Flask(__name__)
app.secret_key = 'SECRETKEYHEREEEEEE'

@app.route('/', methods=["GET"])
def index():
	return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
	your_name = request.form['name']
	if len(your_name) == 0:
		flash('Name must not be left blank!')
	location = request.form['location']
	fave_language = request.form['fave_language']
	comment = request.form['comment']
	if len(comment) == 0:
		flash('Comment must not be left blank!')
	if len(your_name) > 0 and len(comment) > 0:
		return render_template('result.html', name=your_name, dojo_location=location, fave_language=fave_language, comment=comment)
	else:
		return redirect('/')

app.run(debug=True)
