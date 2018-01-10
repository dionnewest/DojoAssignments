from flask import Flask, render_template, request, redirect, session
from random import *
from time import gmtime, strftime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ordinal', methods=['POST'])
def ordinal():
	x = request.form['number']
	z = str(x[len(x)-1])
	if len(x) > 1:
		y = str(x[len(x)-2]+x[len(x)-1])
	else:
		y = "0"
	print z
	print y
	if z == "1" and y != "11":
		print str(x)+"st" 
	elif z == "2" and y != "12":
		print str(x)+"nd"
	elif z == "3" and y != "13":
		print str(x)+"rd"
	else:
		print str(x)+"th"
	return redirect('/')

app.run(debug=True)