from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/test')
def test():
	return render_template("test.html")

@app.route('/user', methods=['POST'])
def create_user1():
	print "New Button Pressed"
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	return redirect('/test')

@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info"
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	return redirect('/show')

@app.route('/show')
def show_user():
	return render_template('users.html')

app.run(debug= True)