from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt

# Create your models here.

def uni_to_str(mydict):
	data={}
	for key, val in mydict.iteritems():
		data[key] = str(val)
	return data
	# print "*=*=*=*=*=*=*=*=*=*=*=*=*"
	# print data

def ValidateEmail(email):
	try:
		validate_email(email)
		return True
	except ValidationError:
		return False

class UserManager(models.Manager):
	def registration_validator(self, form):
		errors = {}
		data = uni_to_str(form)
		print "*================*"
		print uni_to_str(form)
		email_check = User.manager.filter(email=data['email'])

		if len(data['name']) < 2:
			errors['name'] = "First Name must be at least 2 characters."
		if len(data['alias']) < 2:
			errors['alias'] = "Last Name must be at least 2 characters."
		if not ValidateEmail(data['email']):
			errors['email'] = "Email address is not valid."
		if len(email_check) > 0:
			errors['email'] = "Email address already exist."
		if len(data['password']) < 8:
			errors['password'] = "Password must be at least 8 characters long."
		if data['confirm_password'] != data['password']:
			errors['confirm_password'] = "Passwords must match."
		if len(errors)>0:
			return(False, errors)
		else:
			new_user = User.manager.create(name=data['name'], alias=data['alias'], email=data['email'], password=bcrypt.hashpw(data['password'], bcrypt.gensalt()))
			user = User.manager.get(email=data['email']).name
			return (True, new_user, user)

	def login_validator(self, form):
		errors = {}
		data = uni_to_str(form)
		user_email = data['email']
		
		try:
			email_check = User.manager.filter(email=data['email'])
		except Exception:
			errors['email'] = "Email is not registered"
			return (False, errors)

		if len(email_check)>1:
			password_check = User.manager.get(email=user_email).password

		# if len(email_check) < 0:
		# 	errors['email'] = "Email address has not been registered."
		if not bcrypt.checkpw(data['password'], password_check.encode()):
			errors['password'] = "Password is incorrect"
		if len(errors)>0:
			return(False, errors)
		else:
			user = User.manager.get(email=data['email']).name
			return (True, User.manager.get(email=user_email).name, user)

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.CharField(max_length=255)
	updated_at = models.CharField(max_length=255)
	manager = UserManager()
	def __repr__(self):
		return "User #{}: Full Name: {}, Alias {}; Email: {}; Password: {}".format(self.id, self.name, self.alias, self.email, self.password)

 