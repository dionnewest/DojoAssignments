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
			new_user = User.manager.create(name=data['name'], alias=data['alias'], email=data['email'], password=bcrypt.hashpw(data['password'], bcrypt.gensalt()), date_of_birth=data['date_of_birth'])
			user_name = User.manager.get(email=data['email']).name
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
			all_users = User.manager.all().order_by('alias')
			user_name = User.manager.get(email=data['email']).name
			user_id = User.manager.get(email=data['email']).id
			return (True, User.manager.get(email=user_email).name, user_name, user_id)
	def add_friend(self, user_id, friend_id):
		errors = {}
		current_user = User.manager.get(id=user_id)
		other_user = User.manager.get(id=friend_id)
		try:
			friend_check = current_user.friend.get(friend_id=friend_id)
			errors['add_friend']="You are already friends with this person"
		except Exception:
			new_friend = Friend.objects.create(user=current_user, friend=other_user)
		if len(errors)>0:
			return(False, errors)
		else:
			print "=============="
			all_friends = Friend.objects.all()
			print all_friends
			print "=============="
			return (True, all_friends)
	# def remove_friend(self, user_id, friend_id):
		# current_user = User.manager.get(id=user_id)
		# other_user = User.manager.get(id=friend_id)
		# Friend.objects.delete(user=current_user, friend=other_user)


class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	date_of_birth = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	manager = UserManager()
	def __repr__(self):
		return "User #{}: Full Name: {}, Alias {}; Email: {}; Password: {}".format(self.id, self.name, self.alias, self.email, self.password)

class Friend(models.Model):
	user = models.ForeignKey(User, related_name="friend")
	friend = models.ForeignKey(User, related_name="user")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# manager = UserManager()
	def __repr__(self):
		return "Relationship #{}: User id is: {}, Friend id is {}".format(self.id, self.user_id, self.friend_id)
 