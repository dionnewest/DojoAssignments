from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def results():
	if len(request.form['name'])< 1 or len(request.form['location']) < 1 or len(request.form['language']) < 1:
		flash("all fields must be completed.")
		name = request.form['name']
		location = request.form['location']
		language = request.form['language']
		comment = request.form['comment']
		return render_template('index.html', name = name, location = location, language = language, comment = comment)
	else:
		flash("success")
		name = request.form['name']
		location = request.form['location']
		language = request.form['language']
		comment = request.form['comment']
		return render_template('result.html', name = name, location = location, language = language, comment = comment)

@app.route('/', methods = ['POST'])
def go_back():
	go_back = request.form['go_back']
	return render_template('index.html')

app.run(debug=True)