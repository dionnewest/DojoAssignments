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
		print data
		email_check = User.manager.filter(email=data['email'])

		if len(data['first_name']) < 2:
			errors['first_name'] = "First Name must be at least 2 characters."
		if len(data['last_name']) < 2:
			errors['last_name'] = "Last Name must be at least 2 characters."
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
			new_user = self.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=bcrypt.hashpw(data['password'], bcrypt.gensalt()))
			user = User.manager.get(email=data['email']).first_name
			return (True, new_user, user)

	def login_validator(self, form):
		errors = {}
		data = uni_to_str(form)
		email_check = User.manager.filter(email=data['email'])
		user_email = data['email']
		password_check = User.manager.get(email=user_email).password

		if len(email_check) < 0:
			errors['email'] = "Email address has not been registered."
		if not bcrypt.checkpw(data['password'], password_check.encode()):
			errors['password'] = "Password is incorrect"
		# if not bcrypt.checkpw(data['password'],user.password.encode()):
  #           flag = True
  #           errors['password'] = "Invalid credentials"
		if len(errors)>0:
			return(False, errors)
		else:
			user = User.manager.get(email=data['email']).first_name
			return (True, User.manager.get(email=user_email).first_name, user)

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.CharField(max_length=255)
	updated_at = models.CharField(max_length=255)
	manager = UserManager()
	def __repr__(self):
		return "User #{}: Full Name: {} {}; Email: {}; Password: {}".format(self.id, self.first_name, self.last_name, self.email, self.password)

 