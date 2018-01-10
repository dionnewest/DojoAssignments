from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'count' in session:
		session['count'] = session['count'] + 1
	else:
		session['count'] = 0
	return render_template("index.html")

@app.route('/level1', methods=['POST'])
def level1():
	session['count'] = session['count'] + 1
	return redirect('/')

@app.route('/level2', methods=['POST'])
def level2():
	session['count'] = 0
	return redirect('/')

app.run(debug= True)