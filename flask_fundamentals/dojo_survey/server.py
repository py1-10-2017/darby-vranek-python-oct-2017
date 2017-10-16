from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
	return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
	your_name = request.form['name']
	location = request.form['location']
	fave_language = request.form['fave_language']
	comment = request.form['comment']
	return render_template('result.html', name=your_name, dojo_location=location, fave_language=fave_language, comment=comment)

app.run(debug=True)
