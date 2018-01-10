from django.shortcuts import render, HttpResponse, redirect
from random import *
from time import gmtime, strftime

def index(request):
	if 'count' in request.session:
		request.session['count'] = request.session['count']
	else:
		request.session['count'] = 0
	if 'message' in request.session:
		request.session['message'] = request.session['message']
	else:
		request.session['message'] = ""
	return render(request, 'ninja_gold/index.html')

def gold(request):
	request.session['count'] = 0
	request.session['message'] = ""
	return redirect('/')

def farm(request):
	gold = randint(10,20)
	request.session['message'] = request.session['message'] + "You earned " + str(gold) + " pieces of gold."+strftime("%Y-%m-%d %H:%M:%S")+"&#13;&#10;"
	request.session['count'] += gold
	return redirect('/')

def cave(request):
	gold = randint(5,10)
	request.session['message'] = request.session['message'] + "You earned " + str(gold) + " pieces of gold."+strftime("%Y-%m-%d %H:%M:%S")+"&#13;&#10;"
	request.session['count'] += gold
	return redirect('/')

def house(request):
	gold = randint(2,5)
	request.session['message'] = request.session['message'] + "You earned " + str(gold) + " pieces of gold."+strftime("%Y-%m-%d %H:%M:%S")+"&#13;&#10;"
	request.session['count'] += gold
	return redirect('/')

def casino(request):
	gold = randint(-50,50)
	request.session['message'] = request.session['message'] + "You earned " + str(gold) + " pieces of gold."+strftime("%Y-%m-%d %H:%M:%S")+"&#13;&#10;"
	request.session['count'] += gold
	return redirect('/')
