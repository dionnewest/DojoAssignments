from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.

def index(req):
	return render(req, 'travel/success.html')

def destination(req, trip_id):
	trip = Trip.manager.destination(trip_id)
	destination = trip.destination
	created_by_name = trip.created_by.name
	created_by_id = trip.created_by.id
	description = trip.description
	date_from = trip.date_from
	date_to = trip.date_to
	all_travelers = trip.travelers.exclude(id=created_by_id)
	context = {
		'destination':destination,
		'created_by_name':created_by_name,
		'description':description,
		'date_from':date_from,
		'date_to':date_to,
		'all_travelers':all_travelers
	}
	return render(req, 'travel/destination.html', context)

def add(req):
	trip = Trip.manager.create_trip(req.POST, req.session['user_id'])
	if trip[0] == False:
		for key, message in trip[1].iteritems():
			messages.error(req, message)
		return redirect('/travel/add')
	# else:
	# 	req.session['trip_id'] = trip[2]
	return redirect('/travel')

def add_page(req):
	# Trip.manager.all().delete()
	return render(req, 'travel/add.html')

def join(req, trip_id):
	joined_trip = Trip.manager.join_trip(req.session['user_id'], trip_id)
	return redirect('/travel')

def remove(req, trip_id):
	remove_trip = Trip.manager.remove_trip(req.session['user_id'], trip_id)
	return redirect('/travel')