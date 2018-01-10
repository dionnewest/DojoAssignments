from flask import Flask, render_template, request, redirect, session
from random import *
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'number' in session:
		session['guess'] = session['guess']
	else:
		session['guess'] = randint(1,100)
	return render_template("index.html")

@app.route('/number', methods=['POST'])
def number():
	session['number'] = int(request.form['number'])
	if session['number'] > session['guess']:
		message = "The number you guessed was too high, try again."
	elif session['number'] < session['guess']:
		message = "The number you guessed was too low, try again."
	else:
		message = "You guessed correct!"
	session['message'] = message
	print message, session['number'], session['guess']
	return redirect('/')

@app.route('/reset', methods=['POST'])
def level1():
	session['guess'] = randint(1,100)
	return redirect('/')

app.run(debug= True)