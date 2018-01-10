from django.shortcuts import render, HttpResponse, redirect
from .models import *
from ..travel.models import *

# Create your views here.

def index(req):
	# User.manager.all().delete()
	return render(req, 'login_reg/index.html')

def index2(req):
	# User.manager.all().delete()
	return redirect('/main')

def register(req):
	valid = User.manager.registration_validator(req.POST)
	if valid[0] == False:
		for key, message in valid[1].iteritems():
			messages.error(req, message)
		return redirect('/main')
	else:
		req.session['user_name'] = valid[2]
		req.session['user_id'] = valid[3]
		req.session['message'] = "You have successfully registered!"
		return redirect('/travel')

def login(req):
	valid = User.manager.login_validator(req.POST)
	if valid[0] == False:
		for key, message in valid[1].iteritems():
			messages.error(req, message)
		return redirect('/main')
	else:
		req.session['user_name'] = valid[1]
		req.session['user_id'] = valid[2]
		req.session['message'] = "You have successfully logged in!"
		return redirect('/travel')

def travel(req):
	all_trips = Trip.manager.all()
	user = User.manager.get(id=req.session['user_id'])
	users_trips = user.trips.all().order_by('date_from')
	others_trips = set(all_trips) - set(users_trips)
	# others_trips = others_trips.order_by('date_from')
	# others_trips = Trip.manager.exclude(travelers = req.session['user_id']).order_by('date_from')
	content = {
		'user_name':req.session['user_name'],
		'message':req.session['message'],
		'user_id':req.session['user_id'], 
		'all_trips':all_trips,
		'users_trips':users_trips,
		'others_trips':others_trips
	}
	return render(req, 'travel/success.html', content)