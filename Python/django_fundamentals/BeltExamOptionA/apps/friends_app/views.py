from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def index(req):
	# User.manager.all().delete()
	return render(req, 'login_reg/index.html')

def user(req, user_id):
	if 'user_id' not in req.session:
		return redirect ('/main')
	user = User.manager.get(id=user_id)
	content = {
		'user_alias':user.alias,
		'user_name':user.name,
		'user_email':user.email
	}
	return render(req, 'friends_app/user.html', content)

