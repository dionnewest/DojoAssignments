from flask import Flask, render_template, request, redirect, session
from random import *
from time import gmtime, strftime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/color', methods=['POST'])
def color():
	red = request.form['red']
	green = request.form['green']
	blue = request.form['blue']
	return render_template("index.html", red = red, green = green, blue = blue)

app.run(debug= True)
