#OPTION A

from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt
import time
import datetime 

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
		email_check = User.manager.filter(email=data['email'])
		accredidation_check = User.manager.filter(accredidation_number=data['accredidation_number'])
		if len(data['first_name']) < 2:
			errors['first_name'] = "First Name must be at least 2 characters."
		if len(data['last_name']) < 2:
			errors['last_name'] = "Last Name must be at least 2 characters."
		if not ValidateEmail(data['email']):
			errors['email'] = "Email address is not valid."
		if len(email_check) > 0:
			errors['email'] = "Email address already exist."
		if data['accredidation_number'] < 5:
			errors['accredidation_number'] = "Please enter a valid MDE tracking number."
		if len(accredidation_check) > 0:
			errors['accredidation_number'] = "Accredidation number already exist."
		if len(data['password']) < 8:
			errors['password'] = "Password must be at least 8 characters long."
		if data['confirm_password'] != data['password']:
			errors['confirm_password'] = "Passwords must match."
		if data['date_of_birth'] == "":
			errors['date_of_birth'] = "Please enter a valid date"
		else:
			date_of_birth = data['date_of_birth']
			date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
			now = datetime.date.today()
			if date_of_birth > now:
				errors['date_of_birth'] = "Your birthday cannot be in the future"
		if len(errors)>0:
			return(False, errors)
		else:
			new_user = User.manager.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], accredidation_number=data['accredidation_number'], password=bcrypt.hashpw(data['password'], bcrypt.gensalt()), date_of_birth=data['date_of_birth'])
			user_name = User.manager.get(email=data['email']).first_name
			user_id = User.manager.get(email=data['email']).id
			return (True, new_user, user_name, user_id)

	def login_validator(self, form):
		errors = {}
		data = uni_to_str(form)
		user_email = data['email']
		try:
			email_check = User.manager.filter(email=data['email'])
			password_check = User.manager.get(email=user_email).password
		except Exception:
			errors['email'] = "Email is not registered"
			return (False, errors)
		if len(email_check)>1:
			password_check = User.manager.get(email=user_email).password
		if len(email_check) < 0:
			errors['email'] = "Email address has not been registered."
		if not bcrypt.checkpw(data['password'], password_check.encode()):
			errors['password'] = "Password is incorrect"
		if len(errors)>0:
			return(False, errors)
		else:
			all_users = User.manager.all().order_by('last_name')
			user_name = User.manager.get(email=data['email']).first_name
			user_id = User.manager.get(email=data['email']).id
			return (True, User.manager.get(email=user_email).first_name, user_name, user_id)

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	accredidation_number = models.CharField(max_length=15)
	password = models.CharField(max_length=255)
	date_of_birth = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	manager = UserManager()
	def __repr__(self):
		return "User #{}: Full Name: {}, Alias {}; Email: {}; Password: {}".format(self.id, self.name, self.alias, self.email, self.password)
