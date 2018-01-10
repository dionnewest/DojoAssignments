#OPTION A
from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.

def index(req):
	# User.manager.all().delete()
	return render(req, 'login_reg/index.html')

def logout(req):
	req.session.flush()
	return redirect('/main')

def index2(req):
	# User.manager.all().delete()
	return redirect('/main')

def register(req):
	valid = User.manager.registration_validator(req.POST)
	if valid[0] == False:
		for key, message in valid[1].iteritems():
			messages.error(req, message)
		return redirect('/')
	else:
		req.session['user_name'] = valid[2]
		req.session['user_id'] = valid[3]
		req.session['message'] = "You have successfully registered!"
		return redirect('/success')

def login(req):
	valid = User.manager.login_validator(req.POST)
	if valid[0] == False:
		for key, message in valid[1].iteritems():
			messages.error(req, message)
		return redirect('/')
	else:
		req.session['user_name'] = valid[2]
		req.session['user_id'] = valid[3]
		req.session['message'] = "You have successfully logged in!"
		return redirect('/success')

def success(req):
	if 'user_id' not in req.session:
		return redirect ('/main')
	content = {
		'user_name':req.session['user_name'],
		'user_id':req.session['user_id'],
		'message':req.session['message'],
	}
	return render(req, 'login_reg/success.html', content)

def add_friend(req, user_id, friend_id):
	# Friend.objects.all().delete()
	valid = User.manager.add_friend(user_id, friend_id) 
	if valid[0] == False:
		for key, message in valid[1].iteritems():
			messages.error(req, message)
		return redirect('/success')
	valid = User.manager.add_friend(friend_id, user_id) 
	if valid[0] == False:
		for key, message in valid[1].iteritems():
			messages.error(req, message)
		return redirect('/success')
	else:
		all_friends = Friend.objects.all()
		user = User.manager.get(id=req.session['user_id'])
		all_users = User.manager.all()
		users_friends = user.friend.all()
		print "A new friend has been added"
	return redirect ('/success')

def remove_friend(req, user_id, friend_id):
	current_user = User.manager.get(id=user_id)
	other_user = User.manager.get(id=friend_id)
	relationship_id = Friend.objects.get(user=current_user, friend=other_user).delete()
	relationship_id = Friend.objects.get(user=other_user, friend=current_user).delete()
	# Friend.objects.get(id=relationship_id).delete()
	return redirect ('/success')




