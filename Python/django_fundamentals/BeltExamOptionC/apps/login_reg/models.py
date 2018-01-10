from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt

# Create your models here.

def uni_to_str(mydict):
	data={}
	for key, val in mydict.iteritems():
		data[key] = str(val)
	return data

class UserManager(models.Manager):
	def registration_validator(self, form):
		errors = {}
		data = uni_to_str(form)
		user_check = User.manager.filter(user=data['user'])

		if len(data['name']) < 2:
			errors['name'] = "Name must be at least 2 characters."
		if len(data['user']) < 2:
			errors['user'] = "Username must be at least 2 characters."
		if len(user_check) > 0:
			errors['user'] = "Username already exist."
		if len(data['password']) < 8:
			errors['password'] = "Password must be at least 8 characters long."
		if data['confirm_password'] != data['password']:
			errors['confirm_password'] = "Passwords must match."
		if len(errors)>0:
			return(False, errors)
		else:
			new_user = User.manager.create(name=data['name'], user=data['user'], password=bcrypt.hashpw(data['password'], bcrypt.gensalt()))
			user_name = new_user.name
			user_id = new_user.id
			return (True, new_user, user_name, user_id)
			

	def login_validator(self, form):
		errors = {}
		data = uni_to_str(form)
		username = data['user']
		try:
			password_check = User.manager.get(user=username).password
		except Exception:
			errors['user'] = "Username is not registered"
			return (False, errors)
		if not bcrypt.checkpw(data['password'], password_check.encode()):
			errors['password'] = "Password is incorrect"
			return(False, errors)
		else:
			user_name = User.manager.get(user=data['user']).name
			user_id = User.manager.get(user=data['user']).id
			return (True, user_name, user_id)
		

class User(models.Model):
	name = models.CharField(max_length=255)
	user = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	manager = UserManager()
	def __repr__(self):
		return "User #{}: Full Name: {}, user {}; Password: {}".format(self.id, self.name, self.user, self.password)

 