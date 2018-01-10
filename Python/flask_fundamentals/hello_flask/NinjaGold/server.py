from flask import Flask, render_template, request, redirect, session
from random import *
from time import gmtime, strftime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'gold' in session:
		session['gold'] = session['gold']
	else:
		session['gold'] = 0
	if 'message' in session:
		session['message'] = session['message']
	else:
		session['message'] =""
	return render_template("index.html", message=session['message'], gold=session['gold'])

# @app.route('/process_money', methods=['POST'])
# def process_money():
# 	session['gold'] = 0
# 	session['message'] = ""
# 	return redirect('/')

@app.route('/farm', methods=['POST'])
def farm():
	coins = randint(10,20)
	session['gold'] += coins
	session['message'] = session['message'] + "Earned "+str(coins)+" pieces of gold from the farm! "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"&#13;&#10;"
	return redirect('/')

@app.route('/cave', methods=['POST'])
def cave():
	coins = randint(5,10)
	session['gold'] += coins
	session['message'] = session['message'] + "Earned "+str(coins)+" pieces of gold from the cave! "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"&#13;&#10;"
	return redirect('/')

@app.route('/house', methods=['POST'])
def house():
	coins = randint(2,5)
	session['gold'] += coins
	session['message'] = session['message'] + "Earned "+str(coins)+" pieces of gold from the house! "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"&#13;&#10;"
	return redirect('/')

@app.route('/casino', methods=['POST'])
def casino():
	coins = randint(-50,50)
	session['gold'] += coins
	if coins >= 0:
		session['message'] = session['message'] + "Earned "+str(coins)+" pieces of gold from the casino! "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"&#13;&#10;"
	elif coins < 0:
		session['message'] = session['message'] + "Loss "+str(coins)+" pieces of gold from the casino! "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"&#13;&#10;"
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['gold'] = 0
	session['message'] = ""
	return redirect('/')

app.run(debug= True)