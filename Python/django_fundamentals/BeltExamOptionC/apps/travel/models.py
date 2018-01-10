from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import *
from django.contrib import messages
import time
import datetime 

# Create your models here.

def uni_to_str(mydict):
	data={}
	for key, val in mydict.iteritems():
		data[key] = str(val)
	return data

class TripManager(models.Manager): 
	def create_trip(self, form, user_id):
		errors = {}
		data = uni_to_str(form) 
		
		date_to = data['date_to']
		
		if data['date_from'] == "":
			errors['date_from'] = "Please enter a valid date"
		else:
			date_from = data['date_from']
			date_from = datetime.datetime.strptime(date_from, "%Y-%m-%d").date()
			now = datetime.date.today()
			if date_from < now:
				errors['date_to'] = "Cannot schedule a trip before today"
		if data['date_to'] == "":
			errors['date_to'] = "Please enter a valid date"
		else:
			date_to = data['date_to']
			date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d").date()
			if date_to < date_from:
				errors['date_'] = "Cannot end a trip before it starts"
		if len(data['destination']) < 2:
			errors['destination'] = "Destination must be at least two characters"
		if len(data['description']) < 2:
			errors['description'] = "Description must be at least two characters"
		if len(errors)>0:
			return (False, errors)
		else:
			traveler = User.manager.get(id=user_id)
			new_trip = Trip.manager.create(destination=data['destination'], description=data['description'], created_by=traveler, date_from=data['date_from'], date_to=data['date_to'])
			trip_id = new_trip.id
			trip = Trip.manager.get(id=trip_id)
			traveler.trips.add(new_trip)
			return (True, new_trip, trip_id, trip)
	def join_trip(self, user_id, trip_id):
		traveler = User.manager.get(id=user_id)
		joined_trip = Trip.manager.get(id=trip_id)
		joined_trip.travelers.add(traveler)
		return (joined_trip)
	def remove_trip(self, user_id, trip_id):
		traveler = User.manager.get(id=user_id)
		removed_trip = Trip.manager.get(id=trip_id)
		removed_trip.travelers.remove(traveler)
		return (removed_trip)
	def destination(self, trip_id):
		destination = Trip.manager.get(id=trip_id)
		return destination


class Trip(models.Model):
	destination = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	date_from = models.DateField()
	date_to = models.DateField()
	created_by = models.ForeignKey(User, related_name='created_trips')
	travelers = models.ManyToManyField(User, related_name='trips')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	manager = TripManager()
	def __repr__(self):
		return "Trip #{}: Destination: {}, Description {}; Travel Date From: {}; Travel Date To: {}".format(self.id, self.destination, self.description, self.date_from, self.date_to)
