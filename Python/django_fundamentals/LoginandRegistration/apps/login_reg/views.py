from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.

def index(req):
	# User.manager.all().delete()
	return render(req, 'login_reg/index.html')

def register(req):
	valid = User.manager.registration_validator(req.POST)
	if valid[0] == False:
		for key, message in valid[1].iteritems():
			messages.error(req, message)
		return redirect('/')
	else:
		req.session['user'] = valid[2]
		req.session['message'] = "You have successfully registered!"
		return redirect('/success')

def login(req):
	valid = User.manager.login_validator(req.POST)
	if valid[0] == False:
		for key, message in valid[1].iteritems():
			messages.error(req, message)
		return redirect('/')
	else:
		req.session['user'] = valid[2]
		req.session['message'] = "You have successfully logged in!"
		return redirect('/success')

def success(req):
	content = {
		'user':req.session['user'],
		'message':req.session['message']
	}
	return render(req, 'login_reg/success.html', content)